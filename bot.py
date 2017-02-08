#!/c/Python27/python

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from random import randint
import time
import sys
import requests
import lxml.html

# Needs to be global for now so functions can access it.
browser=webdriver.Chrome()

# RANDOMLY CHOOSE WORD FROM 'wordlist.txt'
def random_search_word():
    lines = open('wordlist.txt').readlines()
    word = random.choice(lines)
    return word.strip()

def search_google_with_random_word():
    search_bar = browser.find_element_by_name("q") 
    search_bar.send_keys(random_search_word())
    time.sleep(3)
    submit_btn = browser.find_element_by_id("_fZl")    
    submit_btn.click()

def harvest_links_from_page():
    time.sleep(6)
    xpath_objects = browser.find_elements_by_xpath("//a[@href]")
    links = []
    
    for link in xpath_objects:
        links.append(link.get_attribute("href"))
    return links
    

def main():
    browser.get("https://www.google.com")
    browser.maximize_window()
    
    search_google_with_random_word()
    link_array = harvest_links_from_page()
    
    while True:
        count = 0
        
        if count >= len(link_array):
            time.sleep(randint(10,20))
            count = 0 
            search_google_with_random_word()
        
        browser.get(random.choice(link_array))
        time.sleep(randint(10,15))
        count += 1
        # More accurate than 'back' button
        browser.execute_script("window.history.go(-1)")
        time.sleep(5)

if __name__ == '__main__':
    main()

   
    
