from utils.import_functions import import_car_brand_rdw
from utils.transform_functions import convert_cars_list_to_df, \
                                      convert_cars_df_data_types, \
                                      select_columns_cars_df, \
                                      change_cars_df_colnames, \
                                      change_cars_df_na_values
from utils.exploration_functions import cars_df_exploration
from datetime import date


if __name__ == '__main__':
    

    # specify the brand
    selected_brand = input("Insert a brand:\n")

    # get the list of cars
    cars_list = import_car_brand_rdw(selected_brand)

    # convert the cars_list to a pandas DataFrame, and apply modifications
    cars_df = convert_cars_list_to_df(cars_list)

    # specify the columns we need
    cars_df = select_columns_cars_df(cars_df)

    # explore the data set
    cars_df_exploration(cars_df)

    # specify the right data types
    cars_df = convert_cars_df_data_types(cars_df)

    # change the column names
    cars_df = change_cars_df_colnames(cars_df)

    # change the na values
    cars_df = change_cars_df_na_values(cars_df)
    pass