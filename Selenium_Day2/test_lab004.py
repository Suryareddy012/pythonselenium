
import pytest
import allure

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@allure.title("test_login")
@allure.description("test_login")

def test_login():

    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "btn-make-appointment").click()
    driver.title
    sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.close()
