#!/usr/bin/env python
# coding: utf-8

# In[88]:


# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time
import pprint
import pandas as pd

# setting up pretty print
pp = pprint.PrettyPrinter(indent=2)


# In[89]:


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# # NASA

# In[95]:


# NASA
def scrape_latest_article():
    browser = init_browser()
    
    # setting up pretty print
    pp = pprint.PrettyPrinter(indent=2)
    
     # Visit NASA
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    
    time.sleep(1)
    
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # results are returned as an iterable list
    latest_news = soup.find('li', class_="slide")
    
    # setting the variables
    title_parag = {}
    title_parag["news_title"]= latest_news.find('div', class_= 'content_title').find('a').text
    title_parag["news_p"] = latest_news.find('div', class_= 'article_teaser_body').text
    return title_parag


# # JPL

# In[94]:


# JPL
def scrape_featured_image():
    browser = init_browser()
    
    # setting up pretty print
    pp = pprint.PrettyPrinter(indent=2)
    
     # Visit JPL
    base_url = 'https://www.jpl.nasa.gov'
    url = base_url + '/spaceimages/?search=&category=Mars'
    browser.visit(url)
    
    time.sleep(1)
    
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # finding the featured image
    featured_image = soup.find('article', class_="carousel_item")["style"]
    print(featured_image)
    
    #  url beginning index
    url_index = featured_image.index('url(') + 5
    print(url_index)
    
    # url substring
    url_substring = featured_image[url_index:-3]
    featured_image_url = base_url + url_substring
    return featured_image_url


# # TWITTER

# In[92]:


# Twitter
def scrape_latest_Mars_weather_tweet():
    browser = init_browser()
    
    # setting up pretty print
    pp = pprint.PrettyPrinter(indent=2)
    
     # Visit NASA
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    
    time.sleep(1)
    
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    # results
    latest_Mars_weather_tweet = soup.find('p', class_="tweet-text").text
    return latest_Mars_weather_tweet


# # Mars Facts

# In[97]:


# Mars Facts
def mars_facts():
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    
    # converting table to html
    html_table = df.to_html()
    
    # strip unwanted lines to cleanup table
    html_table.replace('\n', '')

    return html_table.replace('\n', '')
    


# # Mars Hemisphere

# In[93]:


def scrape_Mars_hemisphere():
    browser = init_browser()
    
    # setting up pretty print
    pp = pprint.PrettyPrinter(indent=2)
    
     # Visit JPL
    base_url = 'https://astrogeology.usgs.gov'
    url = base_url + '/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    time.sleep(1)
    
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    
    link_divs = soup.find_all('div', class_="description")
    
    hemisphere_image_urls = []
    
    # looping over the link_divs to get the url for each image
    for div in link_divs:
        browser.visit(base_url + div.find("a")["href"])
    
        time.sleep(1)
    
        # Scrape page into Soup
        html = browser.html
        soup = bs(html, "html.parser")
        
        # creating a dictionary and populating it with the title and image url for the 4 images
        synopsis = {}
        synopsis["title"]= soup.find("h2", class_='title').text
        synopsis["img_url"] = soup.find('div', class_='downloads').find('a')['href']
        hemisphere_image_urls.append(synopsis)
    return hemisphere_image_urls


# In[ ]:


# comprehensive function
def scrape_info():
    mars_dict = {}
    mars_dict["nasa"] = scrape_latest_article()
    mars_dict["jpl"] = scrape_featured_image()
    mars_dict["twitter"] = scrape_latest_Mars_weather_tweet()
    mars_dict["facts"] = mars_facts()
    mars_dict["images"] = scrape_Mars_hemisphere()
    
    return mars_dict
    

