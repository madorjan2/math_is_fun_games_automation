from general_page_model import GeneralPageModel
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

class PageModel(GeneralPageModel):

	def __init__(self, driver, puzzleno):
		super().__init__(driver, f'https://www.theguardian.com/crosswords/quick/{puzzleno}')

	def iframe_cookie(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '//iframe[@title]')))

	def svg_grid_elements(self):
		return self.driver.find_elements(By.XPATH, '//*[name()="rect" and @class="crossword__cell"]')

	def input_hidden(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, '//input[@class="crossword__hidden-input"]')))

	def button_cookie_accept(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Yes, I’m happy"]')))