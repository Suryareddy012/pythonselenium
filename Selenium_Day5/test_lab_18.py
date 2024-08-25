import time

import pytest
import allure
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType

def test_js_prompt():

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    js_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    js_prompt.click()
    driver.switch_to.alert.send_keys("Hello World")
    sleep(4)
    driver.switch_to.alert.accept()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="alert_accept", attachment_type=AttachmentType.PNG)
    driver.close()
def test_js_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    js_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    js_prompt.click()
    driver.switch_to.alert.send_keys("Hello World")
    sleep(4)
    driver.switch_to.alert.dismiss()
    time.sleep(2)
    allure.attach(driver.get_screenshot_as_png(), name="alert_dismiss", attachment_type=AttachmentType.PNG)
    driver.close()