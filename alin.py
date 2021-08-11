from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from requests_html import HTMLSession, AsyncHTMLSession
import time 
# import config 
#NEED TO CREATE A CONFIG FILE WHICH STORES CARD DETAILS, PASSWORDS ETC


"""
SITE WE'RE CHOOSING 

"""
base_url = 'https://rdxsports.co.uk/'

def get_item():
    homepage = base_url + "/fitness/weightlifting-belts/leather-belts/"
    session = HTMLSession()
    connector = session.get(homepage)
    products = connector.html.find("#shop-scroller",first=True).find("li")
    return products, session
