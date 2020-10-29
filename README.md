# Web-Scraping - Mission to Mars
In this assignment, I will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Step 1 - Scraping
I will complete my initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

### NASA Mars News
I will scrape the [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest) and collect the latest News Title and Paragraph Text. Then I will assign the text to variables that I can reference later.

### JPL Mars Space Images - Featured Image
1. Visit the url for [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
2. I will use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called "featured_image_url."

### Mars Facts
1. Visit the [Mars Facts](https://space-facts.com/mars/) webpage and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
2. Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres
1. Visit the [USGS Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) site to obtain high resolution images for each of Mar's hemispheres.
2. I will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
3. I will save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name and then I will use a Python dictionary to store the data using the keys "img_url" and "title."
4. I will append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

## Step 2 - MongoDB and Flask Application
I will use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
1. I will start by converting my Jupyter notebook into a Python script called "scrape_mars.py" with a function called "scrape" that will execute all of my scraping code from above and return one Python dictionary containing all of the scraped data.
2. Next, I will create a route called "/scrape" that will import my "scrape_mars.py" script and call my "scrape" function. I'll store the return value in Mongo as a Python dictionary.
3. I'll create a root route / that will query my Mongo database and pass the mars data into an HTML template to display the data.
4. I'll create a template HTML file called "index.html" that will take the mars data dictionary and display all of the data in the appropriate HTML elements.