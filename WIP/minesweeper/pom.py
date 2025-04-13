from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from general_page_model import GeneralPageModel


class MinesweeperPage(GeneralPageModel):
    def __init__(self, driver):
        super().__init__(driver, 'https://high-flyer.hu/selenium/minesweeper-game.html')
        self.wait = WebDriverWait(self.driver, 5)

    def get_menu(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'menu-link')))

    def get_menu_new(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'menu-new')))

    def get_menu_beginner(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'menu-beginner')))

    def get_menu_intermediate(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'menu-intermediate')))

    def get_menu_expert(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'menu-expert')))

    def get_menu_custom(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, 'menu-custom')))

    