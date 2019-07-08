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
import make_dataset


def make_049():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).

        Function for dataset 049, fema_floodhazard

        Note: the class SandboxCleaner from make_dataset.py duplicates this functionality
              in a more general class. This function is deprecated.
    """
    logger = logging.getLogger(__name__)
    logger.info('making processed data set from raw data for ID: 049')

    if 'GeoJSON' not in fiona.supported_drivers.keys():
        raise ValueError("GeoJSON driver not in fiona.supported_drivers!")

    url = 'https://opendata.arcgis.com/datasets/c0d05bcc4524492899e61923d98f604f_116.geojson'
    dat049 = gpd.read_file(url)
    print("The CRS system is {}".format(dat049.crs))
    print('writing GeoJSON to ../../data/processed/dataset049.geojson')
    dat049.head().to_file("../../data/processed/dataset049.geojson", driver='GeoJSON')



if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # make_049()

    url049 = 'https://opendata.arcgis.com/datasets/c0d05bcc4524492899e61923d98f604f_116.geojson'
    ID_given = '049'
    print("using {} to make dataset {}".format(url049, ID_given))
    test = make_dataset.SandboxCleaner(input_url=url049, ID=ID_given)

    print('making processed data set from raw data for ID: 049')
    test.import_data()

    print('writing GeoJSON to ../../data/processed/dataset049.geojson')
    test.write_file()
