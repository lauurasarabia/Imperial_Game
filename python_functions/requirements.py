import geopandas as gpd
from pandas import json_normalize
import requests
import pandas as pd
from shapely.geometry import Point
from dotenv import load_dotenv
from cartoframes.viz import Map, Layer, popup_element, basic_style, default_legend
import os
import json
from pymongo import MongoClient
from pymongo import GEOSPHERE
from palettable.palette import Palette
from geopy.distance import geodesic


def name_coordinates (dict_):
    processed_dict = {"name": dict_["name"],
                     "lat": dict_["geocodes"]["main"]["latitude"],
                     "lon": dict_["geocodes"]["main"]["longitude"]}
    
    return processed_dict

def to_mongo(name, df):
    df.to_json(f"/Users/lauurasarabia/Ironhack/projects/project_3_GeoSpatial/json_mongo/{name}.json")


def schools_newmontgomery(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    sch_newmont = []
    for i in response.json()["results"]:
        sch_newmont.append(name_coordinates(i))
    return pd.DataFrame(sch_newmont)

def airport_newmontgomery(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    airport_newmont = []
    for i in response.json()["results"]:
        airport_newmont.append(name_coordinates(i))
    return pd.DataFrame(airport_newmont)    

def strbucks_newmontgomery(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    strbucks_newmont = []
    for i in response.json()["results"]:
        strbucks_newmont.append(name_coordinates(i))
    return pd.DataFrame(strbucks_newmont)


def vegan_newmontgomery(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    vegan_newmont = []
    for i in response.json()["results"]:
        vegan_newmont.append(name_coordinates(i))
    return pd.DataFrame(vegan_newmont)


def basket_newmontgomery(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    basket_newmont = []
    for i in response.json()["results"]:
        basket_newmont.append(name_coordinates(i))
    return pd.DataFrame(basket_newmont)

def night_newmontgomery(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    night_newmont = []
    for i in response.json()["results"]:
        night_newmont.append(name_coordinates(i))
    return pd.DataFrame(night_newmont)


def add_geometry(df, lat_col="lat", lon_col="lon"):
    return gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[lon_col], df[lat_col]))

def map_newmont(offices_gdf, nmschools_gdf, strbucksnm_gdf, vegannm_gdf, basketnm_gdf, nightnm_gdf):
    from palettable.cartocolors.diverging import TealRose_7
    x = Map([Layer(offices_gdf, basic_style(size=15, opacity=10, color="blue"),legends=default_legend('Offices')),
        Layer(nmschools_gdf, basic_style(size=15, color="#009392"), legends=default_legend("Schools")),
        Layer(strbucksnm_gdf, basic_style(size=15, color="#72aaa1"), legends=default_legend("Starbucks")),
        Layer(vegannm_gdf, basic_style(size=15, color="#e5b9ad"), legends=default_legend("VeganRestaurants")),
        Layer(basketnm_gdf, basic_style(size=15, color="#d98994"), legends=default_legend("Basketball")),
        Layer(nightnm_gdf, basic_style(size=15, color="#d0587e"), legends=default_legend("NightClubs"))], layer_selector=True)
    return x


def schools_mission(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    sch_mission = []
    for i in response.json()["results"]:
        sch_mission.append(name_coordinates(i))
    return pd.DataFrame(sch_mission)


def starbucks_mission(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    strbcks_mission = []
    for i in response.json()["results"]:
        strbcks_mission.append(name_coordinates(i))
    return pd.DataFrame(strbcks_mission)


def vegan_mission(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    vegan_miss = []
    for i in response.json()["results"]:
        vegan_miss.append(name_coordinates(i))
    return pd.DataFrame(vegan_miss)


def basket_mission(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    basket_miss = []
    for i in response.json()["results"]:
        basket_miss.append(name_coordinates(i))
    return pd.DataFrame(basket_miss)


def night_mission(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    night_miss = []
    for i in response.json()["results"]:
        night_miss.append(name_coordinates(i))
    return pd.DataFrame(night_miss)

def map_mission(offices_gdf, schmission_gdf, strbucksmiss_gdf, veganmiss_gdf, basketmiss_gdf, nightmiss_gdf):
    from palettable.cartocolors.diverging import Temps_7
    y = Map([Layer(offices_gdf, basic_style(size=15, opacity=10, color="blue"),legends=default_legend('Offices')),
        Layer(schmission_gdf, basic_style(size=15, color="#009392"), legends=default_legend("Schools")),
        Layer(strbucksmiss_gdf, basic_style(size=15, color="#39b185"), legends=default_legend("Starbucks")),
        Layer(veganmiss_gdf, basic_style(size=15, color="#9ccb86"), legends=default_legend("VeganRestaurants")),
        Layer(basketmiss_gdf, basic_style(size=15, color="#e9e29c"), legends=default_legend("Basketball")),
        Layer(nightmiss_gdf, basic_style(size=15, color="#eeb479"), legends=default_legend("NightClubs"))], layer_selector=True)
    return y



def schools_brannan(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    sch_brannan = []
    for i in response.json()["results"]:
        sch_brannan.append(name_coordinates(i))
    return pd.DataFrame(sch_brannan)


def starbucks_brannan(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    strbcks_brannan = []
    for i in response.json()["results"]:
        strbcks_brannan.append(name_coordinates(i))
    return pd.DataFrame(strbcks_brannan)


def vegan_brannan(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    vegan_brann = []
    for i in response.json()["results"]:
        vegan_brann.append(name_coordinates(i))
    return pd.DataFrame(vegan_brann)


def basket_brannan(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    basket_brann = []
    for i in response.json()["results"]:
        basket_brann.append(name_coordinates(i))
    return pd.DataFrame(basket_brann)


def night_brannan(url):
    url_ = f"{url}"
    headers = {
    "accept": "application/json",
    "Authorization":token
    }
    response = requests.get(url, headers=headers)
    name_coordinates (response.json()["results"][0])
    
    night_brann = []
    for i in response.json()["results"]:
        night_brann.append(name_coordinates(i))
    return pd.DataFrame(night_brann)

def map_brannan(offices_gdf, schoolsbrannan_gdf, strbcksbrannan_gdf, veganbrann_gdf, basketbrann_gdf, nightbrann_gdf):
    from palettable.cartocolors.diverging import Tropic_7
    z = Map([Layer(offices_gdf, basic_style(size=15, opacity=10, color="blue"),legends=default_legend('Offices')),
        Layer(schoolsbrannan_gdf, basic_style(size=15, color="#009B9E"), legends=default_legend("Schools")),
        Layer(strbcksbrannan_gdf, basic_style(size=15, color="#42B7B9"), legends=default_legend("Starbucks")),
        Layer(veganbrann_gdf, basic_style(size=15, color="#A7D3D4"), legends=default_legend("VeganRestaurants")),
        Layer(basketbrann_gdf, basic_style(size=15, color="#E4C1D9"), legends=default_legend("Basketball")),
        Layer(nightbrann_gdf, basic_style(size=15, color="#C75DAB"), legends=default_legend("NightClubs"))], layer_selector=True)
    return z

