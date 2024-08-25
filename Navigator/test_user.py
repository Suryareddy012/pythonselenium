import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException
from selenium.common.exceptions import StaleElementReferenceException


def test_user_login():
    driver = webdriver.Edge()
    driver.get("https://a33-d1-navigator.a33.lottery-solutions.net/navigator/#/dashboard")
    driver.maximize_window()

    driver.find_element(By.XPATH,"//button[@class='mat-ripple btn-role-primary']").click()

    driver.find_element(By.CSS_SELECTOR,"#Enter Your Username").send_keys("administrator")
    driver.find_element(By.CSS_SELECTOR,"#Enter Your Password").send_keys("Welcome")
    driver.find_element(By.CSS_SELECTOR,"#Submit").click()

    driver.close()