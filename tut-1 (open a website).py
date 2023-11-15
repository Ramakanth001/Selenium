from selenium import webdriver
import time

driver = webdriver.Chrome() #Load the chrome webdriver

driver.get("https://google.com") #open the URL
print(driver.title)
time.sleep(5) 

driver.quit()  #closes the browser



