import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType

@pytest.mark.Negative
def test_login_cura():

    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    driver.find_element(By.XPATH,"//a[@id='btn-make-appointment']").click()

    WebDriverWait(driver, 10).until(EC.url_contains("https://katalon-demo-cura.herokuapp.com/profile.php#login"))

    username_field = driver.find_element(By.XPATH,"//input[@name='username']")
    username_field.send_keys("JohnDoe")
    password_field = driver.find_element(By.XPATH,"//input[@id='txt-password']")
    password_field.send_keys("Surya123")

    driver.find_element(By.XPATH,"//button[@class='btn btn-default']").click()

    error_msg =driver.find_element(By.XPATH,"//p[.='Login failed! Please ensure the username and password are valid.']")
    error_msg.is_displayed()
    error_msg.text == "Login failed! Please ensure the username and password are valid."

    allure.attach(driver.get_screenshot_as_png(), name="test_login_Negative", attachment_type=AttachmentType.PNG)

def test_login_cura_positive():

    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']").click()

    WebDriverWait(driver, 10).until(EC.url_contains("https://katalon-demo-cura.herokuapp.com/profile.php#login"))
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    username_field.send_keys("John Doe")
    password_field = driver.find_element(By.XPATH, "//input[@id='txt-password']")
    password_field.send_keys("ThisIsNotAPassword")

    driver.find_element(By.XPATH, "//button[@class='btn btn-default']").click()

    make_appointment = driver.find_element(By.XPATH,"//a[.='Make Appointment']")
    make_appointment.text == "Make Appointment"

    allure.attach(driver.get_screenshot_as_png(), name="test_login_positive", attachment_type=AttachmentType.PNG)

    driver.close()

