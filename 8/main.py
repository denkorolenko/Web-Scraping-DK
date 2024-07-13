import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def parse_jon_marksandspencer():
    site = 'https://jobs.marksandspencer.com/job-search'

    # Define Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    # Define paths
    user_home_dir = os.path.expanduser("~")
    chrome_binary_path = os.path.join(user_home_dir, "chrome-linux64", "chrome")
    chromedriver_path = os.path.join(user_home_dir, "chromedriver-linux64", "chromedriver")

    # Set binary location and service
    chrome_options.binary_location = chrome_binary_path
    service = Service(chromedriver_path)

    result = []
    max_page_counter = 2

    # Initialize Chrome WebDriver
    with webdriver.Chrome(service=service, options=chrome_options) as driver:
        while max_page_counter:
            max_page_counter -= 1

            driver.get(site)

            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ais-Hits-item')))

            jobs = driver.find_elements(By.CLASS_NAME, 'ais-Hits-item')
            for job in jobs:
                title = job.find_element(By.TAG_NAME, 'h3').text
                url = job.find_element(By.TAG_NAME, 'a').get_attribute('href')
                result.append({
                    'title': title,
                    'url': url,
                })

            next_btn = driver.find_element(By.XPATH, '//a[@aria-label="Next"]')
            if next_btn:
                site = next_btn.get_attribute('href')
            else:
                break

    with open('jobs_selenium.json', 'w') as f:
        json.dump(result, f, indent=4)

if __name__ == '__main__':
    parse_jon_marksandspencer()
