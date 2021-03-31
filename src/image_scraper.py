import selenium
from selenium import webdriver
import time
import os
import requests
import io
from PIL import Image, ImageChops
import hashlib
import numpy as np
from plant_info_generator import plant_info_generator

# Image Scraper for the USDA plants database
# Made by Dylan Walker 3/31/2021
# All of the above Python modules required as well as chrome driver corresponding to your chrome version (found in About Google Chrome in the top right dropdown under help)
# Link to ChromeDriver download(also in github): https://chromedriver.chromium.org/downloads


# Specify your path to your ChromeDriver exe here
DRIVER_PATH = 'Image Scraper/chromedriver.exe'


# Gets each image url from the website by first navigating to the images tab and then clicking on each image. Also sorts out non-plant (specifically non gallery urls) images.
def fetch_image_urls(query, max_links_to_fetch, wd, sleep_between_interactions):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)

        # build the google query

    search_url = "https://plants.sc.egov.usda.gov/core/profile?symbol={q}"

    # load the page
    wd.get(search_url.format(q=query))

    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        image_tab = wd.find_elements_by_name('#tabImages')
        print(image_tab)
        image_tab[0].click()
        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_css_selector("img")
        number_results = len(thumbnail_results)

        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")

        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls
            actual_images = wd.find_elements_by_css_selector('img')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    if "/gallery/" in actual_image.get_attribute('src'):
                        image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        # move the result startpoint further down
        results_start = len(thumbnail_results)

    return image_urls


# Specify your desired save path here (the program will automatically create a folder and put all of the images inside of it)
path = 'Image Scraper'


# Downloads each image using the image urls found by fetch_image_urls as a jpg
def persist_image(folder_path, url):
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
            file_path = os.path.join(folder_path, hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
            with open(file_path, 'wb') as f:
                image.save(f, "JPEG", quality=85)
            print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")


# Combines persist_image and fetch_image_urls to search for each image url and download it. Search_term is the plant ID in the URL or in the database
def search_and_download(search_term, driver_path=DRIVER_PATH, target_path=path, number_images=1):
    target_folder = os.path.join(target_path, '_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)

    for elem in res:
        persist_image(target_folder, elem)


# Change the argument here to whatever plant ID that you want to search
plant_names = plant_info_generator(r'data\plants_usda_selected_features.txt')
for name in plant_names[1:10]: # just for testing
    search_and_download(name)