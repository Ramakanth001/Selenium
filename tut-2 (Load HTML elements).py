# DONE TILL 5:49

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() #Load the chrome webdriver

driver.get("https://google.com") #open the URL
# time.sleep(5) 
search = driver.find_element("id","APjFqb") #points to for search bar
search.send_keys('Seshabhattar Ramakanth') #search text to be entered in search bar
search.send_keys(Keys.RETURN) #Hit enter button

time.sleep(5) 

driver.quit()  #closes the browser

