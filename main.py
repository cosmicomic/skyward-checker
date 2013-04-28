from selenium import webdriver
import getdata
import login
import parse

def get_changes():
	driver = webdriver.Firefox()
	number_of_classes = 6
	login.log_in(driver)
	getdata.navigate_to_gradebook(driver)
	gradebook_data = getdata.get_gradebook_data(driver, number_of_classes)
	for gradebook in gradebook_data:
		for assignment in parse.gradebook_changes(gradebook, gradebook_data.index(gradebook) + 1):
			assignment.print_assignment()
			print "\n"
		print "\n --------------- \n"

def update():
	driver = webdriver.Firefox()
	number_of_classes = 6
	login.log_in(driver)
	getdata.navigate_to_gradebook(driver)
	gradebook_data = getdata.get_gradebook_data(driver, number_of_classes)
	for gradebook in gradebook_data:
		assignments = parse.make_assignments(gradebook, gradebook_data.index(gradebook))
		parse.write_assignments(assignments)
	

def testPrint(driver, url):
	login.log_in(driver, url)
	gradebook_data = getdata.get_gradebook_data(driver, number_of_classes)

	for gradebook in gradebook_data:
		print "\n" + "---------------------------------------" + "\n" + gradebook

def testSave(driver, url):
	login.log_in(driver, url)
	gradebook_data = getdata.get_gradebook_data(driver, number_of_classes)
	parse.save_assignments(gradebook_data)

# create(driver, url)