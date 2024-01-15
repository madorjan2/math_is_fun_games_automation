from general_page_model import GeneralPageModel
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10

class PageModel(GeneralPageModel):

	def __init__(self, driver):
		super().__init__(driver, 'https://www.puzzle-nonograms.com/')

	def button_cookie_agree(self):
		return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="AGREE"]/..')))

	def get_game(self):
		return self.driver.find_element(By.ID, 'game')

	def get_task_columns(self):
		return self.get_game().find_elements(By.XPATH, '//div[@id="taskTop"]/div')

	def get_task_rows(self):
		return self.get_game().find_elements(By.XPATH, '//div[@id="taskLeft"]/div')

	def get_grid(self):
		return self.get_game().find_element(By.CLASS_NAME, 'nonograms-cell-back')

	def get_row_by_index(self, index):
		return self.get_grid().find_elements(By.CLASS_NAME, 'row')[index]

	def get_tile_by_index(self, x, y):
		return self.get_row_by_index(x).find_elements(By.CSS_SELECTOR, '.cell')[y]

	def get_button_done(self):
		return self.driver.find_element(By.ID, 'btnReady')

	def get_link_n_sized_puzzle(self, size):
		if size not in [5, 10, 15, 20, 25]:
			raise ValueError
		return self.driver.find_element(By.XPATH, f'//a[text()="{size}x{size} Nonograms"]')