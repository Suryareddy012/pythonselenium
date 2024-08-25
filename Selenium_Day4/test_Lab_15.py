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

def test_search_result():

    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()

    try:
        # StaleElementReferenceException
        textarea = driver.find_element(By.NAME, "q")
        driver.refresh()
        # Document HTML might change  - refresh
        # element - textarea -> might be case that it is not available now.
        # // Refresh, Navigate other Page, change in DOM elements (Ajax Calls) - VueJS, AngularJS

        # to fix the code we can add a logic
        textarea.send_keys("the testing academy")
        print("End of the program")
    except StaleElementReferenceException as see:
        # stale element reference
        print(see)
        print("Stale element reference")

    driver.close()