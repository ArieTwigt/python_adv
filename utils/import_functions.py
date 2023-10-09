import requests
import sys
from typing import List, Dict


def import_car_brand_rdw(selected_brand: str) -> List[Dict]:
    '''
    Extract car data from the RDW (Basisregistratie voertuigen)

    Return list of cars
    '''

    # uppercase the brand name
    selected_brand_upper = selected_brand.upper()

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # check the response status code
    if response.status_code != 200:
        print("Something went wrong")
        sys.exit()

    # get the data from the response
    data = response.json()

    # check if the list is not empty
    if len(data) == 0:
        print(f"No cars found for {selected_brand}")
        sys.exit()

    return data