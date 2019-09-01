#!/usr/bin/env python

#__author__ == "Katy McKinney-Bock, katy.mckinney-bock@hackoregon.org"

# TODO: refactor all of the make_dataset_000.py files into a single make_dataset.py file.
# Will need to be able to use click or argparse so that a list of IDs
# for sandbox datasets will make only those datasets, and not others.
# Alternatively, keep each make_dataset_000.py file separate, and create workflows around
# loading different sets of data.
#
#        TODO: have each function check the sandbox inventory to see if processed dataset is already available.
#              if not, pull from external source.

import logging, fiona
import geopandas as gpd
import pandas as pd
import make_dataset
import pathlib
import psycopg2




if __name__ == '__main__':

    ###### JOIN THESE DATASETS
    # read excel files into pd dataframe
    # TODO: Get the excel files from S3; for now they are in the local folder.

    FILEPATH_apr12 = "../../data/raw/NCDB_Sample_Database_All_Tracts_12apr2019.xlsx"
    FILEPATH_jun10 ="../../data/raw/NCDB_Sample_Population_10jun2019.xlsx"

    ncdb_sample_apr12 = pd.read_excel(FILEPATH_apr12, dtype={"Geo_FIPS":str})
    ncdb_sample_jun10 = pd.read_excel(FILEPATH_jun10, dtype={"Geo_FIPS":str})

    apr12_columns = ['Geo_FIPS', 'MetroName',
                    'WhiteShare_90', 'WhiteShare_00', 'WhiteShare_10', 'WhiteShare_17',
                    'BlackShare_90', 'BlackShare_00', 'BlackShare_10', 'BlackShare_17',
                    'HispShare_90', 'HispShare_00', 'HispShare_10', 'HispShare_17',
                    'AsOthShare_90', 'AsOthShare_00', 'AsOthShare_10', 'AsOthShare_17',

                    'ChInc_9017', 'ChInc_0017','ChInc_1017',
                    'MedInc_90','MedInc_00','MedInc_10','MedInc_17',

                    'MetMedInc_90','MetMedInc_00','MetMedInc_10','MetMedInc_17',
                    'MetChInc_9017', 'MetChInc_9000','MetChInc_0010','MetChInc_0017','MetChInc_1017',

                    'PovRate_90', 'PovRate_00', 'PovRate_10','PovRate_17',

                    'RentCBShare_90','RentCBShare_00','RentCBShare_10','RentCBShare_17',
                    'MetRentCBShare_90','MetRentCBShare_00','MetRentCBShare_10','MetRentCBShare_17',

                    'MetChRentCBShare_9017','MetChRentCBShare_9000','MetChRentCBShare_0010',
                    'MetChRentCBShare_0017','MetChRentCBShare_1017',

                    'ChRent_9017', 'ChRent_0017', 'ChRent_1017',
                    'MetChRent__9017', 'MetChRent__9000', 'MetChRent__0010', 'MetChRent__0017','MetChRent__1017',

                    'ChBachShare_9017', 'ChBachShare_0017', 'ChBachShare_1017',

                    'MetChBachShare_9017', 'MetChBachShare_9000', 'MetChBachShare_0010', 'MetChBachShare_0017',
                    'MetChBachShare_1017',

                    'MedHomeVal_90', 'MedHomeVal_00','MedHomeVal_10','MedHomeVal_17',
                    'MedRentVal_90','MedRentVal_00','MedRentVal_10','MedRentVal_17',
                    'OwnShare_90','OwnShare_00','OwnShare_10','OwnShare_17',
                    'BachShare_90','BachShare_00','BachShare_10','BachShare_17']

    ncdb_subsample_apr12 = ncdb_sample_apr12[apr12_columns]

    # join excel files by FIPS into one dataframe
    ncdb_total_subsample = pd.merge(ncdb_subsample_apr12, ncdb_sample_jun10, on="Geo_FIPS")


    # read census TRACTS for PDX, DC into gpd
    # TODO: figure out how to make this replicable without connecting to my local database; might hit the transportation API.
    con = psycopg2.connect(database="census_gis2", user="mckbock", host="localhost", options=f'-c search_path=census_gis')
    sql = "select * from tl_2019_11_tract"
    DCtracts = gpd.GeoDataFrame.from_postgis(sql, con, geom_col="wkb_geometry")
    DCmetro = DCtracts[['geoid','wkb_geometry']]

    pdxmetro = gpd.read_file("../../data/raw/census_tract_boundaries.geojson", driver="GeoJSON")


    # do a spatial join on FIPS code to get subset for PDX DC with geom for census tract boundaries
    pdx_ncdb_subsample = pdxmetro.merge(ncdb_total_subsample, how='left', right_on='Geo_FIPS', left_on='geoid')
    pdx_ncdb_subsample = pdx_ncdb_subsample.drop(columns='Geo_FIPS')

    dc_ncdb_subsample = DCmetro.merge(ncdb_total_subsample, how='left', right_on='Geo_FIPS', left_on='geoid')
    dc_ncdb_subsample = dc_ncdb_subsample.drop(columns='Geo_FIPS')

    # write to file
    # TODO: write to S3 processed folder

    pdx_ncdb_subsample.to_file('../../data/processed/dataset045_pdx.geojson', driver='GeoJSON')
    dc_ncdb_subsample.to_file('../../data/processed/dataset045_dc.geojson', driver='GeoJSON')
