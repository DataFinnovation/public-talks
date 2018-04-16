from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

chromeOptions = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chromeOptions)

url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'
driver.get(url)

productForm = driver.find_element_by_xpath("//select[contains(@name,'ctl00$MainContentHolder$ListBox1')]")
formSelect = Select(productForm)
formSelect.select_by_visible_text('Call Reports -- Single Period')

radioButton = driver.find_element_by_id('XBRLRadiobutton')
radioButton.click()

button = driver.find_element_by_name('ctl00$MainContentHolder$TabStrip1$Download_0')
button.click()

sleep(15)
driver.quit()
