import requests
import pickle
import csv
import pandas as pd

import moscow

ADDRESS = "https://nominatim.openstreetmap.org/search"

def get_geojson_list(addresses):
    '''
    return:
    dict ->
    dict_keys(['place_id', 'licence', 'osm_type', 'osm_id', 'lat', 'lon', 'class', 'type', 'place_rank', 'importance', 'addresstype', 'name', 'display_name', 'boundingbox', 'geojson']) 
    '''
    geojson_list = []
    params ={
        "polygon_geojson": 1,
        "format": "json",
        "q": ''
    }
    for address in addresses:        
        params['q'] = address
        if not address:
            print('Not address ("")')
            continue
        response = requests.get(ADDRESS, params=params)
        print("Region {region}. Status code {status}".format(status=response.status_code,
                                                             region=address))
        if response.status_code == 200:
            json = response.json()
            geojson_list.append(json[0])
    return geojson_list

def save_pickle(data, file:str):
    with open(file, 'wb') as data_file:
        pickle.dump(data, data_file)

def load_pickle(file):
    with open(file, 'rb') as data_file:
        return pickle.load(data_file)
    
def save_to_csv(data, file_name):
    label = list(data[0].keys())
    pd_frame = pd.DataFrame(
        data,
        columns=label
    )
    pd_frame.to_csv(file_name, encoding='UTF-8', sep=';')
            
def pandas_xlsx(data, file_name):
    label = list(data[0].keys())
    pd_frame = pd.DataFrame(
        data,
        columns=label
    )
    pd_frame.to_excel(file_name)

def convert_to_short_data(data):
    short_data = []
    for one_object in data:
        object_dict = {
            'name': one_object['name'],
            'osm_id': one_object['osm_id'],
            "geojson": one_object['geojson']['coordinates']
        }
        short_data.append(object_dict)
    return short_data

def main():    
    moscow_city = get_geojson_list(moscow.moscow_city)
    moscow_city = convert_to_short_data(moscow_city)
    save_pickle(moscow_city, 'moscow_city')
    
    moscow_city_districts = get_geojson_list(moscow.moscow_city_districts)
    moscow_city_districts = convert_to_short_data(moscow_city_districts)
    save_pickle(moscow_city_districts, 'moscow_city_districts')
    
    moscow_area = get_geojson_list(moscow.moscow_area)
    moscow_area = convert_to_short_data(moscow_area)
    save_pickle(moscow_area, 'moscow_area')
    
    moscow_area_districts = get_geojson_list(moscow.moscow_area_districts)
    moscow_area_districts = convert_to_short_data(moscow_area_districts)
    save_pickle(moscow_area_districts, 'moscow_area_districts')
    
    moscow_city = load_pickle('moscow_city')
    moscow_city_districts = load_pickle('moscow_city_districts')
    moscow_area = load_pickle('moscow_area')
    moscow_area_districts = load_pickle('moscow_area_districts')
    
    save_to_csv(moscow_city, 'moscow_city.csv')
    save_to_csv(moscow_city_districts, 'moscow_city_districts.csv')
    save_to_csv(moscow_area, 'moscow_area.csv')
    save_to_csv(moscow_area_districts, 'moscow_area_districts.csv')
    
    pandas_xlsx(moscow_city, 'moscow_city.xlsx')
    pandas_xlsx(moscow_city_districts, 'moscow_city_districts.xlsx')
    pandas_xlsx(moscow_area, 'moscow_area.xlsx')
    pandas_xlsx(moscow_area_districts, 'moscow_area_districts.xlsx')
    
if __name__ == "__main__":
    main()