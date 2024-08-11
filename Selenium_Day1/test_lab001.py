from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(4)
driver.close()