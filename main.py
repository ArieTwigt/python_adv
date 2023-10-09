from utils.import_functions import import_car_brand_rdw
from utils.transform_functions import convert_cars_list_to_df


if __name__ == '__main__':
    # specify the brand
    selected_brand = input("Insert a brand:\n")

    # get the list of cars
    cars_list = import_car_brand_rdw(selected_brand)

    # convert the cars_list to a pandas DataFrame, and apply modifications
    cars_df = convert_cars_list_to_df(cars_list)

    # transform the dataset in the right format
    pass