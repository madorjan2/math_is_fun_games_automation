import time

from create_driver import create_driver
from pom import PageModel
from utils import Board, Tile, remove_ads
from selenium.common.exceptions import TimeoutException

page = PageModel(create_driver())
page.open()
page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
page.driver.switch_to.frame(page.get_iframe())
remove_ads(page)

next_level = True

while next_level:
	board = Board((-1, 0), (4, 5))
	grid = page.get_grid()

	board.setup(len(grid[0]), len(grid))
	for column_index in range(len(grid)):
		for row_index in range(len(grid[0])):
			board.add_tile(Tile(page.get_tile_span(row_index, column_index).get_attribute('class')), row_index, column_index)

	solution = board.solve()

	while page.get_message_box().is_displayed():
		time.sleep(0.1)

	for column_index in range(len(solution[0])):
		for row_index in range(len(solution)):
			span = page.get_tile_span(row_index, column_index)
			while span.get_attribute('class') != solution[row_index][column_index]:
				span.click()

	page.button_speedup().click()
	try:
		page.button_next_level().click()
	except TimeoutException:
		next_level = False