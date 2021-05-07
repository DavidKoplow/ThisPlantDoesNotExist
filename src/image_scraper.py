import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import os
import requests
import io
from PIL import Image, ImageChops, ImageFilter
import hashlib
import numpy as np
from plant_info_generator import plant_info_generator
import xml.etree.ElementTree as ET

# Image Scraper for the USDA plants database
# Made by Dylan Walker 3/31/2021
# All of the above Python modules required as well as chrome driver corresponding to your chrome version (found in About Google Chrome in the top right dropdown under help)
# Link to ChromeDriver download(also in github): https://chromedriver.chromium.org/downloads


# Specify your path to your ChromeDriver exe here
DRIVER_PATH = 'ThisPlantDoesNotExist\src\Image Scraper\geckodriver.exe'
#firefox_options = Options() 
#firefox_options.add_experimental_option("detach", True)


# Gets each image url from the website by first navigating to the images tab and then clicking on each image. Also sorts out non-plant (specifically non gallery urls) images.
def fetch_image_urls(query, max_links_to_fetch, wd):
    search_url = 'https://plantsservices.sc.egov.usda.gov/api/PlantProfile?symbol={q}'
    search = search_url.format(q=query)
    #print (search)
    wd.execute_script('''window.open("https://google.com", "_blank");''')
    wd.switch_to.window(wd.window_handles[1])
    wd.get(search)
    #print (wd.window_handles)
    wd.maximize_window()
    lines = WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.TAG_NAME, "AcceptedId")))
    tag_url = "https://plantsservices.sc.egov.usda.gov/api/PlantImages?plantId={q}"
    wd.get(tag_url.format(q=lines.text))
    image_urls = set()
    image_count = 0
    results_start = 0
    thumbnail_results = wd.find_elements_by_tag_name("StandardSizeImageLibraryPath")
    number_results = len(thumbnail_results)
    print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
    for img in thumbnail_results[results_start:number_results]:
        image_url = "https://plants.sc.egov.usda.gov{q}"
        image_urls.add(image_url.format(q=img.text))
        image_count = len(image_urls)
    print(f"Found: {len(image_urls)} image links, done!")
            
    results_start = len(thumbnail_results)
    #close tab
    wd.close()  
    wd.switch_to.window(wd.window_handles[0])
    return image_urls


# Specify your desired save path here (the program will automatically create a folder and put all of the images inside of it)
path = 'data'


# Downloads each image using the image urls found by fetch_image_urls as a jpg
def persist_image(folder_path, url, plant_name, iter):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')

        rgb = image.split()
        largest_diff_pixels = ImageChops.difference(rgb[0], rgb[1]).getextrema()[1] + \
                              ImageChops.difference(rgb[0], rgb[2]).getextrema()[1]
        if (largest_diff_pixels > 50):
            im3=rgb[2].resize((1,1))
            if(im3.getpixel((0,0))<140):
                file_path = os.path.join(folder_path, plant_name + '_' + str(iter) + '.jpg')
                with open(file_path, 'wb') as f:
                    image.save(f, "JPEG", quality=85)
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")

# Combines persist_image and fetch_image_urls to search for each image url and download it. Search_term is the plant ID in the URL or in the database
def search_and_download(search_term, driver_path=DRIVER_PATH, target_path=path, number_images=1):
    target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    res = fetch_image_urls(search_term, number_images, wd=wd)
    i = 0
    for elem in res:
        persist_image(target_folder, elem, search_term, i)
        i += 1

plant_names = plant_info_generator(r'ThisPlantDoesNotExist\src\data\plants_usda_selected_features.txt')
fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
wd= webdriver.Firefox(executable_path=DRIVER_PATH, options=fireFoxOptions)
wd.get('http://thisplantdoesntexist.surge.sh/?fbclid=IwAR0xw5B239O_v7GpT0w_qCeBDCJUCXvIWU3X6NIVy0va77sjWqpCb0cJtms')

for name in plant_names:
    search_and_download(name)
    print(name)
wd.close()