import pytest
import allure

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("test_login")
@allure.description("test_login")

def test_mini_project2():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    sleep(4)
    username =driver.find_element(By.NAME, "username")
    username.send_keys("augtest_040823@idrive.com")
    username.click()

    user_pwd = driver.find_element(By.NAME, "password")
    user_pwd.send_keys("123456")
    user_pwd.click()

    driver.find_element(By.ID, "frm-btn").click()
    sleep(15)
    trial_finished = driver.find_element(By.ID, "trial-finished").is_displayed()
    current_url = driver.current_url

    # Add an Allure screen attachment
    allure_attachment = attachment_type(AttachmentType.PNG)
    allure_attachment.set(driver.get_screenshot_as_png())
    sleep(5)
    driver.close()
