import pytest
from utils.cardata import CarData
import datetime
import numpy
import os

# constants that will be used for each test


# define the tests: Happy Flow
def test_car_data_content():
    car_data = CarData(brand="audi")
    car_data.import_car_brand_rdw()
    assert car_data.brand == "audi"
    assert len(car_data.data) > 0


def test_car_data_columns():
    car_data = CarData(brand="audi")
    car_data.import_car_brand_rdw()
    car_data.select_columns('kenteken', 'merk', 'handelsbenaming')
    assert list(car_data.data.columns) == ['kenteken', 'merk', 'handelsbenaming']

    car_data = CarData(brand="bmw")
    car_data.import_car_brand_rdw()
    car_data.select_columns('pascal', 'merk', 'handelsbenaming', 'arie')
    assert list(car_data.data.columns) == ['merk', 'handelsbenaming']
    assert 'handelsbenaming' in list(car_data.data.columns)


def test_car_data_data_types():
    car_data = CarData(brand="bmw")
    car_data.import_car_brand_rdw()
    car_data.select_columns()
    car_data.convert_cars_df_data_types()
    assert type(car_data.data['datum_tenaamstelling'].values[0]) == numpy.datetime64
    assert type(car_data.data['catalogusprijs'].values[0]) == numpy.float64


def test_car_data_export():
    car_data = CarData("hyundai")
    car_data.import_car_brand_rdw()
    car_data.select_columns()
    car_data.convert_cars_df_data_types()
    car_data.run_car_objects()
    car_data.run_model_objects()
    car_data.export_data()
    test_folder_file_path = "data/hyundai/hyundai.csv"
    assert os.path.exists(test_folder_file_path)


# For wrong requests
def test_car_data_content_wrong():
    car_data = CarData(brand="arie")
    with pytest.raises(ValueError):
        car_data.import_car_brand_rdw()


def test_car_data_columns():
    car_data = CarData(brand="audi")
    car_data.import_car_brand_rdw()
    car_data.select_columns('kenteken', 'merk', 'handelsbenaming', 'arie')
    assert list(car_data.data.columns) == ['kenteken', 'merk', 'handelsbenaming']
