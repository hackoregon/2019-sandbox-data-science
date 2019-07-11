#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__author__ == "Katy McKinney-Bock, katy.mckinney-bock@hackoregon.org"


import click
import logging
import geopandas as gpd, pandas as pd
import boto3
# from pathlib import Path
# from dotenv import find_dotenv, load_dotenv

from inventory import create_filepath

bucket = 'hacko-data-archive'
prefix = '2019-sandbox'
file = 'inventory.csv'
object ='{}/{}'.format(prefix, file)
data = 's3://{}/{}'.format(bucket, object)

inventory = pd.read_csv(data, dtype={'ID': str})
CONFIG = pd.read_csv('config.csv')
ACCESS_KEY = CONFIG['access'].item()
SECRET_KEY = CONFIG['secret'].item()

# @click.command()
# @click.argument('input_filepath', type=click.Path(exists=True))
# @click.argument('output_filepath', type=click.Path())
# def main(input_filepath, output_filepath):
#     """ Runs data processing scripts to turn raw data from (../raw) into
#         cleaned data ready to be analyzed (saved in ../processed).
#     """
#     logger = logging.getLogger(__name__)
#     logger.info('making final data set from raw data')


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
        write_to_S3: Writes a geopandas GeoDataFrame to the 2019-sandbox S3 bucket
                     for processed data, in GeoJSON format.

    #TODO: write a method for checking the coordinate system as EPSG 4326, and
           converting if needed.

    """
    def __init__(self, input_url, ID):
        self.data = gpd.GeoDataFrame()
        self.url = input_url
        self.ID = ID
        self.inventory = inventory
        self.local_path = None

    def import_data(self):
        self.data = gpd.read_file(self.url)
        return(self.data)

    def write_file(self):
        prefix = '../../data/processed/'
        self.local_path ='{}/dataset{}.geojson'.format(prefix, self.ID)
        self.data.to_file(self.local_path, driver='GeoJSON')

    def write_to_S3(self):
        """
        Note: at the moment, the GeoJSON needs to be written locally using write_file() method.
        TODO: build in functionality to skip this step and write the file to GeoJSON directly.
        """
        s3 = boto3.client('s3',
                          aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
        if self.local_path is None:
            prefix = '../../data/processed/'
            self.local_path ='{}/dataset{}.geojson'.format(prefix, self.ID)
        path = create_filepath(inventory_df = inventory, write_to_S3=True, ID=self.ID)
        s3.upload_file(self.local_path, 'hacko-data-archive', path)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    # project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())

    # main()


    test = SandboxCleaner(input_url='test', ID='050')
    test.write_to_S3()
