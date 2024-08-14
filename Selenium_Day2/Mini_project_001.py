import pytest
import allure

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("test_login")
@allure.description("test_login")

def test_make_appointment():

    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    sleep(4)
    driver.find_element(By.ID, "btn-make-appointment").click()
    sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    sleep(3)
    driver.find_element(By.ID, "btn-login").click()
    sleep(5)
    make_appointment = driver.find_element(By.TAG_NAME,"h2")
    assert make_appointment.text == "Make Appointment"
    driver.close()