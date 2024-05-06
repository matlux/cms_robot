from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from cms_functions import fill_in
# Specify the path to chromedriver using the Service class
s = Service('/usr/local/bin/chromedriver')

# Initialize the Chrome WebDriver with the service object
driver = webdriver.Chrome(service=s)




try:
    fill_in(driver, "30000")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Keep the browser window open for 10 seconds
    # You can change the sleep time as needed or remove these lines if you want to close the browser immediately
    import time
    time.sleep(10)
    driver.quit()
