from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    print(driver.session_id)
    print(driver.title)
    assert driver.title == "Google"
    driver.maximize_window()
    sleep(4)
    driver.close()


# pytest Selenium_Day1/test_lab002.py --alluredir=allure_result -s
# allure serve allure_result