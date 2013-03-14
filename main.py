from selenium import webdriver
import getdata
import login
import parse

driver = webdriver.Firefox()
url = "https://www01.nwrdc.wa-k12.net/scripts/cgiip.exe/WService=wissaqus71/mobilelogin.w"
number_of_classes = 6

def update(driver, url):
	login.log_in(driver, url)
	newAssignments = parse.makeAssignments(getdata.get_gradebook_data(driver, number_of_classes))
	parse.compare_assignments(newAssignments)

def create(driver, url):
	login.log_in(driver, url)
	gradebook_data = getdata.get_gradebook_data(driver, number_of_classes)
	newAssignments = parse.makeAssignments(gradebook_data)
	parse.writeAssignments(newAssignments)
	
def testPrint(driver, url):
	login.log_in(driver, url)
	gradebook_data = getdata.get_gradebook_data(driver, number_of_classes)
	
	for gradebook in gradebook_data:
		print "\n" + "---------------------------------------" + "\n" + gradebook
		
def testSave(driver, url):
	login.log_in(driver, url)
	gradebook_data = getdata.get_gradebook_data(driver, number_of_classes)
	parse.save_assignments(gradebook_data)
		
create(driver, url)