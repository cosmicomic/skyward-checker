from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import codecs

def get_user_data():
	# should get data from GUI
	user_data = {"username" : "LIANGCRY000", "password" : "badwolfbay42*"}
	return user_data

def log_in(driver): # where user_data is a dictionary; initialize driver in main.py
	driver.get("https://www01.nwrdc.wa-k12.net/scripts/cgiip.exe/WService=wissaqus71/mobilelogin.w")

	user_data = get_user_data()

	WebDriverWait(driver, timeout=10).until(lambda x: x.find_element_by_id('login'))
	driver.find_element_by_id("login").send_keys(user_data["username"])
	driver.find_element_by_id("password").send_keys(user_data["password"])
	driver.find_element_by_id("bLogin").click()