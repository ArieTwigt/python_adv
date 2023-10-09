from typing import List
import pandas as pd


def convert_cars_list_to_df(cars_list: List) -> pd.DataFrame:
    '''
    Convert the list to a Pandas DataFrame
    '''

    # conver the list to a DataFrame
    cars_df = pd.DataFrame(cars_list)
    
    return cars_df