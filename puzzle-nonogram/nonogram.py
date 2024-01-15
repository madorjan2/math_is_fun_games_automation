from create_driver import create_driver
from pom import PageModel
from utils import task_to_list

from selenium.common.exceptions import TimeoutException

SIZE = 15

page = PageModel(create_driver())
page.open()

try:
	page.button_cookie_agree().click()
except TimeoutException:
	pass

page.get_link_n_sized_puzzle(SIZE).click()

print(task_to_list(page.get_task_rows()))
print(task_to_list(page.get_task_columns()))


for x in range(SIZE):
	for y in range(SIZE):
		page.get_tile_by_index(x, y).click()