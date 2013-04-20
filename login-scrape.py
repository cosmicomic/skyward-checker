from selenium import webdriver
import selenium
from selenium.webdriver.support.ui import WebDriverWait
import codecs
import datetime
import time

login = "LIANGCRY000"
password = "badwolfbay42*"
number_of_classes = 6

driver = webdriver.Firefox()

def get_semester():
	if datetime.date.today() <= datetime.date(2013, 1, 25):
		return 1
	else:
		return 2
		
def fetch_gradebook_data(driver):
	if get_semester() == 1:
		WebDriverWait(driver, timeout=10).until(lambda x: x.current_url == "https://www01.nwrdc.wa-k12.net/scripts/cgiip.exe/WService=wissaqus71/gradebook002.w")
		driver.find_element_by_id("link3").click()
		print "\n" + "First Semester"
	else:
		WebDriverWait(driver, timeout=10).until(lambda x: x.current_url == "https://www01.nwrdc.wa-k12.net/scripts/cgiip.exe/WService=wissaqus71/gradebook002.w")
		driver.find_element_by_id("link6").click()	
		print "\n" + "Second Semester"
	WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('bViewGradeMarks'))
	return driver.page_source
	
def return_to_all_gradebook(driver):
	driver.find_element_by_id("bCancel").click()
	WebDriverWait(driver, timeout=10).until(lambda x: element_present(x, "link6"))
	driver.find_element_by_id("bCancel").click() 

def log_in(driver, login, password):
	driver.get("https://www01.nwrdc.wa-k12.net/scripts/cgiip.exe/WService=wissaqus71/mobilelogin.w")

	WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('login'))
	driver.find_element_by_id("login").send_keys(login)
	driver.find_element_by_id("password").send_keys(password)
	driver.find_element_by_id("bLogin").click()

def element_present(driver, element):
	try:
		driver.find_element_by_id(element)
	except selenium.common.exceptions.NoSuchElementException:
		return False
	return True
	
def navigate_to_gradebook(driver):
	WebDriverWait(driver, timeout=10).until(lambda x: element_present(x, "link2")) # Student Access
	driver.find_element_by_id("link2").click()
	print "\n" + "Student Access"

	WebDriverWait(driver, timeout=10).until(lambda x: element_present(x, "link1") and not element_present(x, "link2")) # Name
	driver.find_element_by_id("link1").click()

	WebDriverWait(driver, timeout=10).until(lambda x: element_present(x, "link4")) # Gradebook
	driver.find_element_by_id("link4").click()
	print "\n" + "Gradebook"
	
def get_gradebook_data(driver, number_of_classes):
	gradebook_data = []

	for i in range(number_of_classes): # Get grades from individual classes
		WebDriverWait(driver, timeout=10).until(lambda x: "gradebook.w" in x.current_url and x.find_element_by_id("link" + (str)(i + 1)))
		driver.find_element_by_id("link" + (str)(i + 1)).click()
		print "\n" + "link" + (str)(i + 1)
		gradebook_data.append(fetch_gradebook_data(driver))
		return_to_all_gradebook(driver)
		
	return gradebook_data
	
def test_get_gradebook_data(driver, login, password, number_of_classes):	
	log_in(driver, login, password)
	navigate_to_gradebook(driver)
			
	for gradebook in get_gradebook_data(driver, number_of_classes):
		print gradebook + "\n" + "\n"
		
def test_get_one_gradebook(driver, login, password):
	log_in(driver, login, password)
	navigate_to_gradebook(driver)
	
	WebDriverWait(driver, timeout=10).until(lambda x: "gradebook.w" in x.current_url and x.find_element_by_id('link1'))
	driver.find_element_by_id("link3").click()

	WebDriverWait(driver, timeout=10).until(lambda x: x.current_url == "https://www01.nwrdc.wa-k12.net/scripts/cgiip.exe/WService=wissaqus71/gradebook002.w" and x.find_element_by_id('link6'))
	driver.find_element_by_id("link6").click() 
	
	WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('bViewGradeMarks'))
	
	with codecs.open('file.html', 'w', 'utf-8') as f:
		f.write(driver.page_source) 
		
# test_get_gradebook_data(driver, login, password, number_of_classes)
test_get_one_gradebook(driver, login, password)