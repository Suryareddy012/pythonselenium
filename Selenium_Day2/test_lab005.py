
import pytest
import allure

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("vwo_test_login")
@allure.description("verify that vwo page is logged in")

def test_vwo_login():

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()
    sleep(5)
    #assert driver.current_url == "https://app.vwo.com/#/login"
    vwo_email_address = driver.find_element(By.ID,"login-username")
    vwo_email_address.send_keys("admin@admin.com")
    vwo_password = driver.find_element(By.ID, "login-password")
    vwo_password.send_keys("admin123")
    sleep(3)
    driver.find_element(By.ID, "login-submit").click()
    sleep(5)
    driver.close()