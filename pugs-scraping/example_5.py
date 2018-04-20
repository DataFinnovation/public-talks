from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

# start up a chrome
driver = webdriver.Chrome()

# laod our target page
url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'
driver.get(url)

# set the type in a form
productForm = driver.find_element_by_xpath("//select[contains(@name,'ctl00$MainContentHolder$ListBox1')]")
formSelect = Select(productForm)
formSelect.select_by_visible_text('Call Reports -- Single Period')

# now click a button
radioButton = driver.find_element_by_id('XBRLRadiobutton')
radioButton.click()

# find the download button and click that too
button = driver.find_element_by_name('ctl00$MainContentHolder$TabStrip1$Download_0')
button.click()

# sleep for demo purposes
sleep(15)
driver.quit()
