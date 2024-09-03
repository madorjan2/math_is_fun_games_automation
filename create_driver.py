from selenium import webdriver
from selenium.webdriver import ChromeOptions

def create_driver():
	options = ChromeOptions()
	options.add_experimental_option('detach', True)
	options.add_argument('disable-search-engine-choice-screen')
	driver = webdriver.Chrome(options)
	driver.maximize_window()
	return driver