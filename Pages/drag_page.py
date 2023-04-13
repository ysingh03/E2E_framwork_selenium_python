from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Base import locatorsReader


class Drag:
    def __init__(self, focusdriver, section):
        global driver
        driver = focusdriver
        self.section = section

    def click_Cursor_style_page(self):
        driver.find_element(By.XPATH, locatorsReader.readLocator('Drag', 'click_cursor_style')).click()


    def current_position_of_element(self, locator):
        element = driver.find_element(By.ID, locatorsReader.readLocator(self.section, locator))
        location = element.location
        x = location.get('x')
        y = location.get('y')
        return x, y

    def drag_and_drop(self, locator):
        oc = ActionChains(driver)
        oc.drag_and_drop_by_offset(driver.find_element(By.ID, locatorsReader.readLocator(self.section, locator)), 700, 200)
        oc.perform()

    def drag_and_drop_to_destination(self, source, destination):
        ac = ActionChains(driver)
        source = driver.find_element(By.ID, locatorsReader.readLocator(self.section, source))
        destination = driver.find_element(By.ID, locatorsReader.readLocator(self.section, destination))
        ac.drag_and_drop(source, destination)
        ac.perform()



