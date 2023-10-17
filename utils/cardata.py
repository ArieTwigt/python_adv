import requests
import pandas as pd
from utils import COLUMNS_LIST, DF_DTYPES, DF_COLNAMES
import datetime
import re

class CarDataCollection:


    def add_to_collection(self, CarData):
        self.car_list
        pass

class CarData:

    # default attributes
    rdw_endpoint = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
    steps = []
    status = "New"
    data = pd.DataFrame()

    # define the initalization
    def __init__(self, brand: str,
                       color: str=None) -> None:
        '''
        Initiaze a CarData object:

        * brand
        * color
        '''
        self.brand = brand
        self.color = color
        self.steps.append("Initialized")


    def change_brand(self, new_brand: str) -> None:
        print(f"Old name {self.brand}")
        self.brand = new_brand
        print(f"New name {self.brand}")


    # method for importing data from the RDW API
    def import_car_brand_rdw(self) -> None:
        '''
        Extract car data from the RDW (Basisregistratie voertuigen)

        Return list of cars
        '''

        # uppercase the brand name
        selected_brand_upper = self.brand.upper()

        # define the endpoint
        endpoint = f"{self.rdw_endpoint}?merk={selected_brand_upper}"

        # execute the request
        response = requests.get(endpoint)

        # check the response status code
        if response.status_code != 200:
            print("Something went wrong")
            sys.exit()

        # get the data from the response
        cars_list = response.json()

        # check if the list is not empty
        if len(cars_list) == 0:
            print(f"No cars found for {selected_brand}")
            sys.exit()

        # conver the list to a DataFrame
        cars_df = pd.DataFrame(cars_list)

        # add the data to the data attribute
        self.data = cars_df

        # add to the steps
        self.steps.append("Imported car data")

    
    def select_columns(self, *args: str):
        '''
        Returns the DataFrame with only the specified columns


        '''
        # get the cars_df
        cars_df = self.data

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
        
        self.data = cars_df_subset

        # add to the steps
        self.steps.append("Selected columns")


    def convert_cars_df_data_types(self, **kwargs):
        '''
        Specify the data types for the cars dataset
        '''
        # initiate the cars_df value
        cars_df = self.data

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


        # return the result to the object
        self.data = cars_df

        # add to the steps
        self.steps.append("Change data types")


    # method for grouping the data
    def group_car_data(self, *args):
        '''
        Group and summarize the dataset
        '''

        # get the data
        cars_df = self.data

        # get the args
        if len(args) != 0:
            group_columns = list(args)
        else: # default value
            group_columns =['handelsbenaming']

        # group and aggregate the data
        selected_colours = ['ZWART', 'GRIJS']
        cars_df_grouped = (cars_df
                           .query("eerste_kleur == @selected_colours")
                           .assign(totaal_catalogusprijs = lambda x: x['catalogusprijs'])
                           .assign(eerst_geregistreerd = lambda x: x['datum_tenaamstelling'])
                           .groupby(group_columns)
                           .agg({"catalogusprijs": "mean",
                                 "totaal_catalogusprijs": "sum", 
                                 "datum_tenaamstelling": "max",
                                 "eerst_geregistreerd": "min"})
                           .reset_index()
                           .rename(columns={"catalogusprijs": "gemiddelde_prijs",
                                            "handelsbenaming": "model",
                                            "datum_tenaamstelling": "laatst_geregistreerd"})
                           .assign(totaal_dagen = lambda x: (x['laatst_geregistreerd'] -
                                                             x['eerst_geregistreerd']).dt.days
                                                            )
                           .assign(merk = lambda x: x['model'].str.split(" ").str[0])
                           .assign(model = lambda x: x['model'].str.split(" ").str[1:].str.join(" "))
                           .assign(jaar = lambda x: x['laatst_geregistreerd'].dt.strftime("%Y"))
                           .assign(maand = lambda x: x['laatst_geregistreerd'].dt.strftime("%B"))
                           .query("totaal_dagen > 0")
                           .sort_values(by="gemiddelde_prijs", ascending=False)
                           .dropna()
                           .reindex(['merk', 'model', 'eerste_kleur', 'gemiddelde_prijs', 'totaal_dagen', 'jaar', 'maand'], axis=1)
                           )

        # save it to the object
        self.data = cars_df_grouped

        # append to the steps
        self.steps.append("Grouped data")


    def __repr__(self) -> str:

        return f"""
                Brand: {self.brand}
                Steps: {self.steps}
                Data: 

                {self.data.head()}
                
                """
