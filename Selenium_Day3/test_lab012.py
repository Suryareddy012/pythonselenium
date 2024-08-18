import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType

def test_vwo_login_Negative():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()

    user_email = driver.find_element(By.CSS_SELECTOR, "#login-username")
    user_email.send_keys("admin@admin.com")
    user_password = driver.find_element(By.CSS_SELECTOR, "#login-password")
    user_password.send_keys("admin123")
    sign_in = driver.find_element(By.XPATH, "//span[.='Sign in']")
    sign_in.click()

    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#js-notification-box-msg")))

    # Check if the error message is displayed
    error_message = driver.find_element(By.CSS_SELECTOR, "#js-notification-box-msg")
    assert error_message.is_displayed()
    assert error_message.text == "Your email, password, IP address or location did not match"

    allure.attach(driver.get_screenshot_as_png(), name="test_login_Negative", attachment_type=AttachmentType.PNG)
    driver.quit()
