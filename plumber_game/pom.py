from general_page_model import GeneralPageModel
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

class PageModel(GeneralPageModel):

	def __init__(self, driver):
		super().__init__(driver, 'https://www.mathsisfun.com/games/plumber-game.html')

	def get_iframe(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.presence_of_element_located((By.ID, 'iframe1')))

	def get_game_div(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '//div[@class="plumbing"]')))

	def get_columns(self):
		return self.get_game_div().find_elements(By.TAG_NAME, 'ul')

	def get_grid(self):
		grid = []
		for column in self.get_columns():
			grid.append(column.find_elements(By.TAG_NAME, 'li'))
		return grid


	def get_message_box(self):
		return self.driver.find_element(By.CLASS_NAME, 'message-box')

	def get_tile_span(self, row_index, column_index):
		return self.get_grid()[column_index][row_index].find_element(By.TAG_NAME, 'span')

	def button_speedup(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.element_to_be_clickable((By.CLASS_NAME, 'speedUp')))

	def button_next_level(self):
		return WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Next Level")]')))

	def ads(self):
		return self.driver.find_elements(By.XPATH, '//div[@title="Advertisement"]')