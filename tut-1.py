from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://google.com")
print(driver.title)
time.sleep(5)

driver.quit() 
# --closes the entire browser

# driver.close()  
# --closes only the tab


# while(True):
#   pass
# --This will always keep the browser open