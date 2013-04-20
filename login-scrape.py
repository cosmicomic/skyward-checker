from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import codecs

login = "login"
password = "password"

driver = webdriver.Firefox()
driver.get("https://www01.nwrdc.wa-k12.net/scripts/cgiip.exe/WService=wissaqus71/mobilelogin.w")

WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('login'))
driver.find_element_by_id("login").send_keys(login)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("bLogin").click()

WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('link2')) # Student Access
driver.find_element_by_id("link2").click()

WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('link1')) # Name
driver.find_element_by_id("link1").click()

WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('link4')) # Gradebook
driver.find_element_by_id("link4").click()

WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('link1')) # this later be a more complex thing that will loop through each class
driver.find_element_by_id("link1").click()

WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('link6')) # assume second semester; program will be able to detect the date and check with semester it is
driver.find_element_by_id("link6").click()

WebDriverWait(driver, timeout=3).until(lambda x: x.find_element_by_id('bViewGradeMarks'))

with codecs.open('file.html', 'w', 'utf-8') as f:
	f.write(driver.page_source)
	



