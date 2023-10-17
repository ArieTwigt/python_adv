from utils.cardata import CarData

if __name__ == '__main__':
    my_car_data = CarData("audi")
    my_car_data.import_car_brand_rdw()
    my_car_data.select_columns()
    my_car_data.convert_cars_df_data_types()
    my_car_data.group_car_data("handelsbenaming", "eerste_kleur")
    pass
