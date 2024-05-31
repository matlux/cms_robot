

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def fill_in(driver, amount):

    # "//input[@class='hero__input' and @type='number' and @step='any' and @min='0.01' and @name='salary']"
    input_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                      "//input[@class='hero__input' and @type='number' and @step='any' and @min='0.01' and @name='salary']")))
    # input_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[class(@type, 'hero__input') and contains(@type, 'number') and contains(@name, 'salary')]")))
    input_element.clear()
    input_element.send_keys(amount)
    # input_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "taxcode")))
    # input_element.clear()
    # input_element.send_keys("20000")

    input_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located(
        (By.XPATH, "//input[contains(@type, 'submit') and contains(@value, 'Calculate')]")))
    driver.execute_script("arguments[0].click();", input_element)
    driver.implicitly_wait(0.5)
    takehome_value = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//td[@class='results__cell results__cell--overlined takehome']"
        ))
    ).text
    return takehome_value

def fill_in_fast(driver, amount):
    driver.get("https://child-maintenance.dwp.gov.uk/calculate/details/will-you-be-paying-or-receiving-child-maintenance-payments")

    # Wait for the radio button to be clickable

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='f-payingOrReceiving']"))).click()
    # Wait for the Continue button to be clickable
    continue_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button")))
    driver.execute_script("arguments[0].click();", continue_button)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='f-makingPayments-2']"))).click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='f-benefits-2']"))).click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='f-receiveIncome']"))).click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))

    input_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "f-amount")))
    input_element.clear()
    input_element.send_keys(amount)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='f-frequency-3']"))).click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))


    input_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "f-totalChildren")))
    input_element.click()
    input_element.clear()
    input_element.send_keys("3")
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))


    input_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "f-childName0")))
    input_element.clear()
    input_element.send_keys("A")

    input_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "f-childName1")))
    input_element.clear()
    input_element.send_keys("B")

    input_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "f-childName2")))
    input_element.clear()
    input_element.send_keys("C")

    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='f-howManyNights']"))).click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='f-howManyNights']"))).click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='f-howManyNights']"))).click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='f-howManyChildren']"))).click()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "continue-button"))))

