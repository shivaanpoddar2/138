from selenium import webdriver 
from bs4 import BeautifulSoup 
import time 
import csv
start_URL="https://en.wikipedia.org/wiki/List_of_animated_feature_films_of_the_2020s"

browser = webdriver.Chrome("C:/Users/Neha/Desktop/python/Scraping/chromedriver.exe")
browser.get(start_URL)
time.sleep(10)
def scrape():
    headers = ["Title", "Country", "Director", "Studio", "Animation_Technique","Notes"]
    movie_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tbody_tag in soup.find_all("tbody", attrs={"class", "wikitable sortable jquery-tablesorter"}):
        tr_tags = tbody_tag.find_all("tr")
        for td_tags in tr_tags.find_all("td"):
            console.log('reading')
            
scrape()