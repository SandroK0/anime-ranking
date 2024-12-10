'''

 This Script Scrapes Data From IMDB

'''


import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import csv

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Start the browser maximized
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)

file_name = 'anime_data1.csv'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


url = "https://www.imdb.com/list/ls026392856/?view=detailed"
driver.get(url)

# Define variables to store data
anime_data = []

# Scroll and scrape loop
while True:
    # Wait for content to load
    time.sleep(2)

    # Find all anime title elements
    anime_elements = driver.find_elements(
        By.CSS_SELECTOR, 'div.sc-2bfd043a-3.jpWwpQ.dli-parent')

    for anime in anime_elements:
        try:
            # Anime title
            title_element = anime.find_element(
                By.CSS_SELECTOR, "a.ipc-title-link-wrapper")
            title = " ".join(title_element.text.split(" ")[1:])

            anime_page = title_element.get_attribute("href")

            # Get the anime image url from anime page
            content = requests.get(anime_page, headers=headers)
            content = BeautifulSoup(content.text, 'html.parser')
            image_element = content.find("img", class_="ipc-image")
            image_url = image_element.get("srcset").split(",")[0]

            # Anime description
            desc_element = anime.find_element(
                By.CSS_SELECTOR, "div.ipc-html-content-inner-div"
            )
            desc = desc_element.text

            # Meta Data
            meta_data_items = anime.find_elements(
                By.CSS_SELECTOR, "span.dli-title-metadata-item"
            )

            years = meta_data_items[0].text
            eps = meta_data_items[1].text

            # Avoid duplicates
            if title not in [a["title"] for a in anime_data]:
                anime_data.append(
                    {"title": title, "years": years, "eps": eps, "desc": desc, "image": image_url, "id": str(uuid.uuid4())[:6]})
        except Exception as e:
            print("Error fetching anime title:", e)

    # Scroll to the bottom to load more content
    previous_height = driver.execute_script(
        "return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for new content to load
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Break if no new content is loaded
    if new_height == previous_height:
        break

# Output the collected anime titles
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file, fieldnames=["id", "title", "years", "eps", "desc", "image"])

    # Write the header
    writer.writeheader()

    # Write the anime data
    writer.writerows(anime_data)

print(f"Data written to {file_name}")

driver.quit()
