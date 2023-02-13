import geopandas as gdp
from pandas import json_normalize
import requests
import pandas as pd
from dotenv import load_dotenv
from cartoframes.viz import Map, Layer, popup_element
import os
import json
from pymongo import MongoClient
from pymongo import GEOSPHERE

def name_coordinates (dict_):
    processed_dict = {"name": dict_["name"],
                     "lat": dict_["geocodes"]["main"]["latitude"],
                     "lon": dict_["geocodes"]["main"]["longitude"]}
    
    return processed_dict


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

 

