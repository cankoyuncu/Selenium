from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")

seckin_madde_alani = driver.find_element(By.ID, "mp-tfa")
seckin_madde_yazisi = seckin_madde_alani.text
print("Haftanin Seckin Maddesi:" +seckin_madde_yazisi)

print("--------------------------------")

biliyor_muydunuz = driver.find_element(By.ID, "mp-bm")
biliyor_muydunuz = biliyor_muydunuz.text
print("Biliyor Muydunuz? " +biliyor_muydunuz)

time.sleep(5)
driver.quit()
