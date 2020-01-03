# https://www.seleniumeasy.com
# Working with forms, putting values into From, clicking to button etc.
# Usefull sites:
# https://selenium.dev, https://www.crummy.com/software/BeautifulSoup/bs4/doc/, https://automatetheboringstuff.com
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys('Hello World!')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

messageFieldA = driver.find_element_by_xpath('//*[@id="sum1"]')
messageFieldA.send_keys('5')
messageFieldB = driver.find_element_by_xpath('//*[@id="sum2"]')
messageFieldB.send_keys('10')
sumButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
sumButton.click()

