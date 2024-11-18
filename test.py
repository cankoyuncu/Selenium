from selenium import webdriver
from selenium.webdriver.common.by import Service

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")