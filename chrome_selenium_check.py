import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import mysql.connector

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')



if os.name == 'nt':
    chromedriver_path = 'C:/Inst/chromedriver.exe'
else:
    chromedriver_path = '/usr/local/bin/chromedriver'

driver = webdriver.Chrome(
    executable_path=chromedriver_path,
    options=chrome_options)

driver.quit()

print("ChromeDriver check - PASSED!")

def take_pass():
    if os.name == 'nt':
        filename = 'c:/inst/info.txt'
    else:
        filename = '/opt/dbrealtor/Backups/info.txt'
    text = open(filename, mode="r", encoding="utf-8")
    line = text.readline()
    return line

connection_config_dict = {
    'user': 'vova',
    'password': take_pass(),
    'host': 'localhost',
    #'host': '3.123.24.56',
    'database': 'dbrealtor',
    'raise_on_warnings': True,
    #'use_pure': True,
    'autocommit': True,
    'pool_size': 5
}

# Open Connection
connection = mysql.connector.connect(**connection_config_dict)
try:
    connection = mysql.connector.connect(**connection_config_dict)
    query = 'SELECT COUNT(*) FROM dataloadlog'
    cursor = connection.cursor()
    cursor.execute(query)
    #print('MySQL check - PASSED! Count of DataLoadLog rows = ' + str(cursor.rowcount))
    print(f"{bcolors.OKGREEN}OK: MySQL check - PASSED! Count of DataLoadLog rows = {bcolors.ENDC}")
except:
    print(f"{bcolors.FAIL}ERROR: MySQL check DOESN'T PASSED{bcolors.ENDC}")
finally:
    connection.close

