from selenium import webdriver

class GeneralPageModel:

	def __init__(self, driver: webdriver.Chrome, url):
		self.driver = driver
		self.url = url

	def open(self):
		self.driver.get(self.url)

	def close(self):
		self.driver.quit()