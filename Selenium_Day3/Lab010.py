import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.positive

def test_cura_login():

    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_btn = driver.find_element(By.CSS_SELECTOR,"#btn-make-appointment")
    make_appointment_btn.click()

    wait = WebDriverWait(driver, 5)
    wait.until(EC.url_contains("https://katalon-demo-cura.herokuapp.com/profile.php#login"))

    # Check if the current URL is the login form URL
    current_url = driver.current_url
    assert current_url == "#appointment"

    driver.close