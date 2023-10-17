from typing import List
import pandas as pd
from utils import COLUMNS_LIST, DF_DTYPES, DF_COLNAMES
import datetime


def convert_cars_list_to_df(cars_list: List) -> pd.DataFrame:
    '''
    Convert the list to a Pandas DataFrame
    '''

    # conver the list to a DataFrame
    cars_df = pd.DataFrame(cars_list)
    
    return cars_df


def select_columns_cars_df(cars_df: pd.DataFrame, *args):
    '''
    Returns the DataFrame with only the specified columns


    '''

    # specify the list
    if len(args) == 0:
        columns_list = COLUMNS_LIST
    else:
        columns_list = list(args)

    # check if the columns exist
    for column in columns_list:
        if column not in cars_df.columns:
            print(f"The column {column} not in the DataFrame")
            columns_list.remove(column)


    cars_df_subset = cars_df[columns_list]
    
    return cars_df_subset


def convert_cars_df_data_types(cars_df: pd.DataFrame, **kwargs):
    '''
    Specify the data types for the cars dataset
    '''

    # filter for the available column names
    df_colnames = list(cars_df.columns)

    # check if the keyword args are specified
    if len(kwargs.keys()) == 0:
        df_types = DF_DTYPES
    else:
        df_types = kwargs

    # filter only for the df_types that appear in the DataFrame
    df_types_filtered = {}
    for key, value in df_types.items():
        if key in df_colnames:
            df_types_filtered[key] = value

    for key, value in df_types_filtered.items():
        match value:
            case datetime.date:
                cars_df[key] = pd.to_datetime(cars_df[key], format="%Y%m%d")
            case float():
                cars_df[key] = pd.to_numeric(cars_df[key])
            case _:
                cars_df[key] = cars_df[key].astype(value)


    return cars_df


def change_cars_df_colnames(cars_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Change the column names
    '''

    # change the column names
    cars_df.rename(columns=DF_COLNAMES, inplace=True)
    
    return cars_df


# method for working with empty values
def change_cars_df_na_values(cars_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Change the NA-values
    '''
    # get the original row counts
    row_count = len(cars_df)


    # remove the na values
    if 'catalogusprijs' in cars_df.columns and  'datum_tenaamstelling' in cars_df.columns:
        cars_df.dropna(subset=['catalogusprijs', 'datum_tenaamstelling'], 
                    thresh= 2,
                    inplace=True)

    # get the row count after the filter
    new_row_count = len(cars_df)

    # compare the row counts
    if row_count != new_row_count:
        print(f"Difference in rows: {row_count} -> {new_row_count}")
    else:
        print("No rows removed")
    

    return cars_df