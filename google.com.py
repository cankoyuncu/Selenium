from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Chrome sürücüsünü otomatik olarak yönet
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.google.com")
driver.maximize_window()
aramakutusu = driver.find_element(By.NAME, "q")
aramakutusu.send_keys("python")
# driver.find_element(By.XPATH, '//*[@id="APjFqb"]').click()
driver.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b").click()

time.sleep(5)
