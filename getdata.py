from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium
import codecs
import datetime
import time

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
		
def element_present(driver, element):
	try:
		driver.find_element_by_id(element)
	except selenium.common.exceptions.NoSuchElementException:
		return False
		
	return True
		
def get_gradebook_data(driver, number_of_classes):
	gradebook_data = []
	
	WebDriverWait(driver, timeout=10).until(lambda x: element_present(x, "link2")) # Student Access
	driver.find_element_by_id("link2").click()
	print "\n" + "Student Access"

	WebDriverWait(driver, timeout=10).until(lambda x: element_present(x, "link1") and not element_present(x, "link2")) # Name
	driver.find_element_by_id("link1").click()

	WebDriverWait(driver, timeout=10).until(lambda x: element_present(x, "link4")) # Gradebook
	driver.find_element_by_id("link4").click()
	print "\n" + "Gradebook"
	
	for i in range(number_of_classes): # Get grades from individual classes
		WebDriverWait(driver, timeout=10).until(lambda x: "gradebook.w" in x.current_url and x.find_element_by_id("link" + (str)(i + 1)))
		driver.find_element_by_id("link" + (str)(i + 1)).click()
		print "\n" + "link" + (str)(i + 1)
		gradebook_data.append(fetch_gradebook_data(driver))
		return_to_all_gradebook(driver)
		
	return gradebook_data