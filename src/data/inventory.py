#!/usr/bin/env python

# __author__ == "Katy McKinney-Bock, katy.mckinney-bock@hackoregon.org"

# This is a quick script to explore the sandbox S3 inventory for `s3://hacko-data-archive/2019-sandbox/data`,
# and return filepaths for processed files.
#
# Notes:
# -     At the moment, this script assumes that there is only one processed file for each indexed dataset.
#       It is likely that one dataset may have multiple processed files.
#           TODO: add each processed file_name as a list to the sandbox inventory,
#           and build functionality for returning all items in a list of file_names.
# -     If there is no `processed_filename` specified, get_all_processed_filepaths() and create_filepath()
#       both return the prefix up to the `processed` tag by default.
#       Set `has_filepath=False` to return only filepaths with processed files.
# -     TODO: add functionality for working with S3 tags.

import pandas as pd
import s3fs

bucket = 'hacko-data-archive'
prefix = '2019-sandbox'
file = 'inventory.csv'

object ='{}/{}'.format(prefix, file)
data = 's3://{}/{}'.format(bucket, object)

inventory = pd.read_csv(data, dtype={'ID': str})

def create_filepath(inventory_df, has_filepath=True, write_to_S3=False, **kwargs):
    """
    This function creates a filepath to read processed data from the S3 bucket,
    provided with the sandbox data inventory and an ID or short name.

    Currently hard-coded default set to the 2019-sandbox object in the hacko-data-archive AWS S3 bucket.

    Arguments:
        inventory_df = A pandas dataframe in the style of a Sandbox inventory file, with ID and short_name columns
                       (use pd.read_csv(data, dtype={'ID': str}) to read in the dataset)
        ID = 3-digit ID number associated with a sandbox dataset, with leading zeros
        short_name = a string associated with the short name for a sandbox dataset
        has_filepath = To be used (True) if you want the full inventory, even if a filename for the processed
                       file is not present. When True, retursn the prefix even without a filename
                       for all files in the inventory. For a shorter list of only processed files, use False.
        write_to_S3 = To be used if a dataframe is being written to S3, and a new filepath needs to be created
                         or written over.
    """
    ID_given = kwargs.get('ID', None)
    short_name_given = kwargs.get('short_name', None)

    if ID_given is None and short_name_given is None:
        raise ValueError("No ID or short_name was provided to create the filepath.")
    elif ID_given is None:
        ID_given = inventory_df.loc[inventory_df['short_name'] == short_name]['ID'].item()
    elif short_name_given is None:
        short_name_given = inventory_df.loc[inventory_df['ID'] == ID_given]['short_name'].item()
    elif ID_given is not None and short_name_given is not None:
        pass

    bucket = 'hacko-data-archive'
    prefix = '2019-sandbox/data'
    proc = 'processed'


    if write_to_S3:
        file_name = 'dataset'+str(ID_given)+'.geojson'
        object ='{}/{}/{}/{}/{}'.format(prefix, ID_given, short_name_given, proc, file_name)
        data = 's3://{}/{}'.format(bucket, object)

        return(data)

    else:
        if has_filepath:
            if pd.isnull(inventory_df.loc[inventory_df['ID'] == ID_given]['processed_filename'].item()):
                file_name = ""
            else:
                file_name = inventory_df.loc[inventory_df['ID'] == ID_given]['processed_filename'].item()

            object ='{}/{}/{}/{}/{}'.format(prefix, ID_given, short_name_given, proc, file_name)
            data = 's3://{}/{}'.format(bucket, object)

            return(data)
        else:
            if pd.isnull(inventory_df.loc[inventory_df['ID'] == ID_given]['processed_filename'].item()):
                file_name = ""
                object ='{}/{}/{}/{}/{}'.format(prefix, ID_given, short_name_given, proc, file_name)
                data = ''
            else:
                file_name = inventory_df.loc[inventory_df['ID'] == ID_given]['processed_filename'].item()
                object ='{}/{}/{}/{}/{}'.format(prefix, ID_given, short_name_given, proc, file_name)
                data = 's3://{}/{}'.format(bucket, object)

            return(data)






def get_all_processed_filepaths(inventory_df, has_filepath=True):
    """
    This function returns a list of filepaths of processed data from the S3 bucket for all IDs,
    provided with the sandbox data inventory.

    Arguments:
        inventory_df = A pandas dataframe in the style of a Sandbox inventory file, with ID and short_name columns
                       (use pd.read_csv(data, dtype={'ID': str}) to read in the dataset)
        has_filepath = If True (default), then filepath prefixes will be generated up to `/processed`,
                        but no filename will be included. If false, only prefixes with full paths will be included
                        (i.e. those that have a processed file name provided).

    """
    path_list = []
    if has_filepath:
        for row in inventory_df.itertuples():
            ID_forrow = row.ID
            path_forrow = create_filepath(inventory_df, ID=ID_forrow)
            path_list.append(path_forrow)
        return(path_list)
    else:
        for row in inventory_df.itertuples():
            ID_forrow = row.ID
            path_forrow = create_filepath(inventory_df, has_filepath=False, ID=ID_forrow)
            if path_forrow == "":
                pass
            else:
                path_list.append(path_forrow)
        return(path_list)


if __name__ == "__main__":
    # TODO: use argparser to ask for an ID with this script.
    print("Here is the filepath for the ID you requested:")
    path = create_filepath(inventory_df = inventory, has_filepath=False, ID='050')
    print(path)
    print("\n")

    current_S3_data = get_all_processed_filepaths(inventory, has_filepath=True)
    print("Here is the current inventory of processed Sandbox data files:")
    for row in current_S3_data:
        print(row)
    print("\n")
