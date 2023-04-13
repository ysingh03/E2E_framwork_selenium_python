from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Base import locatorsReader


class Resize:
    def __init__(self, focusdriver, section):
        global driver
        driver = focusdriver
        self.section = section

    def resize_area(self, draggingpoint):
        ac = ActionChains(driver)
        element = driver.find_element(By.XPATH, locatorsReader.readLocator(self.section, draggingpoint))
        ac.click_and_hold(element)
        ac.drag_and_drop_by_offset(element, 600, 200)
        ac.perform()



