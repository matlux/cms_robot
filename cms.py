from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cms_functions import fill_in
import time
# Specify the path to chromedriver using the Service class
s = Service('/usr/local/bin/chromedriver')

# Initialize the Chrome WebDriver with the service object
driver = webdriver.Chrome(service=s)




try:
    # Array of salary values to iterate over
    salaries = [str(x) for x in range(74500, 175001, 500)]

    # Loop through each salary, input it, and print the captured value
    for salary in salaries:
        cms_value = fill_in(driver, salary)
        print("Captured Value for salary", salary, ":", cms_value)


finally:
    # Keep the browser window open for 10 seconds
    # You can change the sleep time as needed or remove these lines if you want to close the browser immediately
    time.sleep(100)
    driver.quit()
