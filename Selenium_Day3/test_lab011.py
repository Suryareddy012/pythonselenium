import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from allure_commons.types import AttachmentType
from allure_commons.utils import attachment_type
@pytest.mark.Negative
def test_login_cura():

    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
    driver.maximize_window()

    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("JohnDoe")
    password_field.send_keys("Surya123")

    driver.find_element(By.CLASS_NAME, "//button[@class='btn btn-default']").click()

    # Wait for the login error message to be visible
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#Login failed! Please ensure the username and password are valid.")))

    # Check if the login error message is displayed
    error_mes = driver.find_element(By.CSS_SELECTOR,
                                    "#Login failed! Please ensure the username and password are valid.")
    assert error_mes.is_displayed()
    assert error_mes.text == "Login failed! Please ensure the username and password are valid."

    # Close the webdriver
    driver.quit()