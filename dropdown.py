import time
from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

ser_obj = Service(executable_path=ChromeDriverManager().install())
dr=webdriver.Chrome(service=ser_obj, options=options)
dr.get("https://parivahan.gov.in/parivahan/")
dr.maximize_window()

links=dr.find_elements(By.TAG_NAME,'a')
#links1=dr.find_elements(By.XPATH,'//a')
print(len(links))
for i in links:
    print(i.text)

ele_online=dr.find_element(By.XPATH, "//a[normalize-space()='Online Services']")
ele_online.click()
#drp = select(ele_online)


#time.sleep(3)
#ele_online.click()
time.sleep(3)
dr.quit()