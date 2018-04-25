
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# we want headless
firefoxOptions = Options()
firefoxOptions.add_argument('-headless')

# kick off a firefox
driver = webdriver.Firefox(options=firefoxOptions)

# now as before
url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'
driver.get(url)
dateField = driver.find_element_by_id('UpdatedTextCDR')
print(dateField.text)

# or, cause it's python....
dt = datetime.datetime.strptime("-".join( [[str(i) for i in driver.find_element_by_id('UpdatedTextCDR').text.split(' ')[2].split('/')][j] for j in [2,0,1]] ),"%Y-%m-%d")

driver.quit()