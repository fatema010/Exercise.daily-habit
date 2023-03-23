from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


path = "C:\selenium\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.techwithtim.net/")
link = driver.find_element(By.XPATH,'//*[@id="menu-item-402"]/a')
link.click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="menu-item-511"]/a'))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="sow-button-19310003"]'))
    )
    element.click()
    driver.back()
    driver.back()
    driver.back()



except :
    
    driver.quit()
    