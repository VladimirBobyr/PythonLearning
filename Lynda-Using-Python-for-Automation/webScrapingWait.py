# Example of waiting with Selenium
# 2 types of wait: Explicit - wait until a condition is satisfied
# and Implicit - pull DOM for a certain amount of time, until element becomes available

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get('https://www.google.com/earth/')
wait = WebDriverWait(driver, 10)
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launchEarthButton.click()


