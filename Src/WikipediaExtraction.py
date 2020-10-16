from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from pandas.io.json import json_normalize   
import pandas as pd  
import time
import json
import re

def getFruits():
    my_url = "https://en.wikipedia.org/wiki/List_of_culinary_fruits"
    # Opening up connection, grabbing the page
    UClient =  uReq(my_url)
    time.sleep(3)
    page_html = UClient.read()
    
    # Extract code
    page_soup = soup(page_html,"lxml")
    # Extract tables
    tables = page_soup.find_all("table",{"class", "wikitable sortable"})
    
    fruits = []
    for table in tables:
        for item in table.find_all("a"):
            fruits.append(item.get_text().lower())
    fruits.remove("common name")
    
    return fruits 

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def getVegetables():
    my_url = "https://en.wikipedia.org/wiki/List_of_vegetables"
    # Opening up connection, grabbing the page
    UClient =  uReq(my_url)
    time.sleep(3)
    page_html = UClient.read()
    
    # Extract code
    page_soup = soup(page_html,"lxml")
    # Extract tables
    tables = page_soup.find_all("table")
    
    vegetables = []
    for table in tables:
        for item in table.find_all("a"):
            vegetables.append(item.get_text().lower())
            
    # Cleaning results
    scarti = []

    for item in vegetables:
        separated = item.split("\xa0/")
        if(len(separated)>1):
            scarti.append(item)
            for sep in separated:
                vegetables.append(sep)

    for item in scarti:
        if (item in vegetables):
            vegetables.remove(item)

    for item in vegetables:
        if(hasNumbers(item)):
            vegetables.remove(item)
    return vegetables

def getHerbs():
    my_url = 'https://en.wikipedia.org/wiki/List_of_culinary_herbs_and_spices'
    UClient =  uReq(my_url)
    page_html = UClient.read()

    # Extract code
    page_soup = soup(page_html,"lxml")
    # Extract tables
    tables = page_soup.find_all("li")
    herbs = []
    for item in tables[29:220]:
        herbs.append(item.get_text().split(",")[0].split("(")[0].lower())
    herbs = list(set(herbs))
    herbs.sort()
    
    return herbs