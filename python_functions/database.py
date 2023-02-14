from pymongo import MongoClient
import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup 
import re
import matplotlib.pyplot as plt


def connect_db (database):
    """
    Connect with your database in MongoDB
    """
    client = MongoClient("localhost:27017")
    db = client["Ironhack"]
    return db.get_collection(f"{database}")

def show_categories (category):
    category = c.distinct(f"{category}")
    print(category)

def get_tech_companies():
    filter_ = {"category_code": {"$regex": "games_video|hardware|network_hosting|software|web"}}
    projection = {"name":1, "_id":0, "category_code":1, "total_money_raised":1, "offices.city":1, "offices.country_code":1 }
    tech_companies = list(c.find(filter_, projection).sort("total_money_raised", -1))
    return tech_companies

def get_tech_companies_cities_and_countries():
    cities = [] 
    for i in range(len(tech_companies)):
        for j in range(len(tech_companies[i]["offices"])):
            cities.append(tech_companies[i]["offices"][j]["city"])
    
    countries = []
    for i in range(len(tech_companies)):
        for j in range(len(tech_companies[i]["offices"])):
            countries.append(tech_companies[i]["offices"][j]["country_code"])
            
    tcompanies = {
    "City": cities,
    "Country": countries
    }

    df = pd.DataFrame(tcompanies)
    return df

def get_text_description(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    tags = soup.find_all("div", attrs={"class": "field-rich-text"})
    text_description = tags[0].getText()
    return text_description

