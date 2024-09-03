from guardian_pom import PageModel
from create_driver import create_driver

page = PageModel(create_driver(), 11111)
page.open()

iframe_cookie = page.iframe_cookie()

page.driver.switch_to.frame(iframe_cookie)

page.button_cookie_accept().click()

page.driver.switch_to.parent_frame()

print(len(page.svg_grid_elements()))

page.svg_grid_elements()[0].click()
page.input_hidden().send_keys('asdsd')

# page.close()