from selenium import webdriver
import getdata
import login
import parse

driver = webdriver.Firefox()
url = "https://www01.nwrdc.wa-k12.net/scripts/cgiip.exe/WService=wissaqus71/mobilelogin.w"

def update():
	login.log_in(driver, url)
	newAssignments = parse.make_assignments(getdata.get_gradebook_data())
	parse.compare_assignments(newAssignments)

def create():
	login.log_into_skyward()
	newAssignments = parse.make_assignments(getdata.get_gradebook_data())
	parse.writeAssignments(newAssignments)