# DONE TILL 12:49

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome() #Load the chrome webdriver

# driver.get("https://google.com") #open the URL
# # time.sleep(5) 
# search = driver.find_element("id","APjFqb") #points to for search bar
# search.send_keys('Seshabhattar Ramakanth') #search text to be entered in search bar
# search.send_keys(Keys.RETURN) #Hit enter button


driver.get("https://www.cm-alliance.com/cybersecurity-blog")
# driver.get("https://cybersecurity.att.com/blogs")

try:
    # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.class,"blogv2-postbox")))
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"blogv2-postbox"))
        )
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.class,"blogv2-postbox"))
    #     )
    # element = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR,"blog-card-text")))
    print(element.text)
    # wrap-resource-blocks
    # blog-card-text
except:
    driver.quit()



time.sleep(5) 

driver.quit()  #closes the browser

