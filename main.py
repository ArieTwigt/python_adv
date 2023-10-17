from utils.cardata import CarData

if __name__ == '__main__':
    # get the input
    selection = input("Insert a brand:\n")
    my_car_data = CarData(selection)
    my_car_data.import_car_brand_rdw()
    my_car_data.select_columns()
    my_car_data.convert_cars_df_data_types()
    my_car_data.run_car_objects()
    my_car_data.run_model_objects()
    my_car_data.export_data()
    my_car_data.generate_brand_model_hiearchy()
    pass
