import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import pytest

options = Options()
options.add_experimental_option("detach", True)

ser_obj = Service(executable_path=ChromeDriverManager().install())
dr=webdriver.Chrome(service=ser_obj, options=options)
dr.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
dr.maximize_window()
time.sleep(3)

dr.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
dr.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
dr.
login=dr.find_element(By.XPATH,"//button[normalize-space()='Login']")
login.click()
time.sleep(3)
print(dr.title)
links=dr.find_elements(By.TAG_NAME,'a')

#links1=dr.find_elements(By.XPATH,'//a')
print(len(links))
for i in links:
    print(i.text)
# for j in links1:
#     print(j.text)
dr.close()