from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path)

def scrape():
    
    # --------- NASA Mars News ---------
    browser = init_browser()
    url = "https://mars.nasa.gov/news"
    browser.visit(url)

    time.sleep(2)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    news = soup.find("div", class_="list_text")
    news_title = news.find("div", class_="content_title").text
    news_p = news.find("div",class_="article_teaser_body").text

    # Close the browser after scraping
    browser.quit()


    # --------- JPL Mars Space Images - Featured Image ---------
    browser = init_browser()
    mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(mars_image_url)

    time.sleep(2)

    mars_image_html = browser.html
    soup_mars_image = bs(mars_image_html, "html.parser")

    thread = soup_mars_image.find("article", class_="carousel_item")["style"]

    featured_image_url = "https://www.jpl.nasa.gov" + thread.replace("background-image: url('","").replace("');","")

    browser.quit()


    # --------- Mars Facts ---------
    browser = init_browser()
    mars_facts_url = "https://space-facts.com/mars/"

    # Add try/except for error handling    
    try:
        # Scrape the facts table into a dataframe
        mars_table = pd.read_html(mars_facts_url)   
        # Create dataframe using index to grab first table
        mars_facts = mars_table[0]
    except BaseException:
        return None
    
    # Rename columns
    mars_facts.columns = ["Description", ""]

    # Generate html table from dataframe
    mars_table = mars_facts.to_html(header=None,index=False)

    # Strip newlines to clean up table
    mars_table.replace("\n", "")

    browser.quit()

    # --------- Mars Hemispheres ---------
    browser = init_browser()
    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)

    time.sleep(2)

    mars_hemispheres_html = browser.html
    soup_mars_hemispheres = bs(mars_hemispheres_html)

    mars_images = soup_mars_hemispheres.find("div", class_= "collapsible results")

    # Dictionary for hemisphere image url strings and titles
    full_res_url_dict = {}
    for x in range(4):
        full_res_url = "https://astrogeology.usgs.gov/" + mars_images.find_all("div", class_= "item")[x].find("a")["href"]
        full_res_name = mars_images.find_all("div", class_="item")[x].find("div", class_= "description").find("h3").text
        full_res_url_dict[full_res_name] = full_res_url

    # List of hemisphere images and corresponding titles to append to dictionary
    hemisphere_image_urls = []
    for key, value in full_res_url_dict.items():
        browser.visit(value)
        full_image_html = browser.html
        full_image_soup = bs(full_image_html)
        full_res_url = full_image_soup.find("div", class_= "downloads").find("a")["href"]
        hemisphere_image_urls.append({"title":key, "img_url": full_res_url})  

    browser.quit()
    
    # Store all variables in a dictionary
    mars_mission_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_table": mars_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    # Return all results
    return mars_mission_data
