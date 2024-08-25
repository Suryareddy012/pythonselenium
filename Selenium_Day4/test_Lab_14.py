import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException

def test_vwo_login():

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    try:
        driver.find_element(By.ID, "ID")
    except NoSuchElementException :
        print("No Such Element is available")
    finally:
        print("End of Program")
    driver.close()


