from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from salary_calculator_functions import fill_in
import time
# Specify the path to chromedriver using the Service class
s = Service('/usr/local/bin/chromedriver')

# Initialize the Chrome WebDriver with the service object
driver = webdriver.Chrome(service=s)

# Open the webpage
driver.get("https://www.thesalarycalculator.co.uk/salary.php")

# Wait for the radio button to be clickable

# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'cl-consent__btn') and contains(@class, 'cl-consent-node-a') and @data-role='b_agree']"))).click()

try:
    # Array of salary values to iterate over
    salaries = [str(x) for x in range(10000, 175001, 500)]

    # Loop through each salary, input it, and print the captured value
    for salary in salaries:
        takehome_value = fill_in(driver, salary)
        print("Captured Value for salary", salary, ":", takehome_value)

finally:
    # Keep the browser window open for 10 seconds
    # You can change the sleep time as needed or remove these lines if you want to close the browser immediately
    time.sleep(1)
    driver.quit()

