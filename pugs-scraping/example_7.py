
import os
import tempfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

firefoxOptions = Options()
firefoxOptions.add_argument('-headless')

driver = webdriver.Firefox(options=firefoxOptions)

url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'
driver.get(url)

dateField = driver.find_element_by_id('UpdatedTextCDR')
print(dateField.text)
