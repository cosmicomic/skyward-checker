from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import codecs
import datetime

def get_semester():
	if date.today() <= datetime.date(2013, 1, 25):
		return 1
	else:
		return 2
		
def fetch_gradebook_data(driver):
	if get_semester() == 1:
		WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('link3'))
		driver.find_element_by_id("link3").click()
	else:
		WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('link6'))
		driver.find_element_by_id("link6").click()	
	WebDriverWait(driver, timeout=3).until(lambda x: x.find_element_by_id('bViewGradeMarks'))
	return driver.page_source
	
def return_to_all_gradebook():
	driver.find_element_by_id("bCancel").click() 
	driver.find_element_by_id("bCancel").click() 
		
def get_gradebook_data(driver, number_of_classes):
	gradebook_data = []
	
	WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('link2')) # Student Access
	driver.find_element_by_id("link2").click()

	WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('link1')) # Name
	driver.find_element_by_id("link1").click()

	WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('link4')) # Gradebook
	driver.find_element_by_id("link4").click()
	
	for i in range(number_of_classes):
		WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id("link" + (str)(i))) # Get grades from individual classes
		driver.find_element_by_id("link" + (str)(i)).click()
		gradebook_data += fetch_gradebook_data()
		return_to_all_gradebook()
		
	return gradebook_data