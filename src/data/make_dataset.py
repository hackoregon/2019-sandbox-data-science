#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__author__ == "Katy McKinney-Bock, katy.mckinney-bock@hackoregon.org"


import click
import logging
import geopandas as gpd
# from pathlib import Path
# from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


class SandboxCleaner():
    """
    This class acts as a cleaning pipeline for Sandbox datasets.

    Arguments:
        input_url: requires API endpoint or other url containing geospatial dataset
        ID: requires a dataset ID from the sandbox data inventory. See inventory.py to
            explore the Sandbox data inventory.

    Methods:
        import_data: Reads files into a geopandas GeoDataFrame from url.
        write_file: Writes a GeoDataFrame to a GeoJSON file using the fiona driver.
                    Puts the file in ../../data/processed/
        write_to_S3: Not yet finished. Will write a geopandas GeoDataFrame to GeoJSON
                     and put into the 2019-sandbox S3 bucket for processed data.

    #TODO: write a method for checking the coordinate system as EPSG 4326, and
           converting if needed.

    """
    def __init__(self, input_url, ID):
        self.data = gpd.GeoDataFrame()
        self.url = input_url
        self.ID = ID

    def import_data(self):
        self.data = gpd.read_file(self.url)
        return(self.data)

    def write_file(self):
        prefix = '../../data/processed/'
        path ='{}/dataset{}.geojson'.format(prefix, self.ID)
        self.data.to_file(path, driver='GeoJSON')

    def write_to_S3(self):
        pass



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    # project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())

    # main()
