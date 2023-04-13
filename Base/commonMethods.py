from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Base import locatorsReader


class commonMethods:

    def __init__(self, focusdriver):
        global driver
        driver = focusdriver

    def switch_to_iframe(self, locator, section):
        element = driver.find_element(By.XPATH, locatorsReader.readLocator(section, locator))
        driver.switch_to.frame(element)

    def verify_element_is_visible(self, locator, section):
        try:
            check_element = driver.find_element(By.XPATH, locatorsReader.readLocator(section, locator))
            return True
        except NoSuchElementException:
            return False

    def find_Position_on_axis_xpath(self, locator, section, typeofaxis):
        item = driver.find_element(By.XPATH, locatorsReader.readLocator(section, locator))
        axis = item.location.get(typeofaxis)
        return axis

    def find_Position_on_axis_id(self, locator, section, typeofaxis):
        item = driver.find_element(By.ID, locatorsReader.readLocator(section, locator))
        axis = item.location.get(typeofaxis)
        return axis

    def find_height_and_width_xpath(self, locator, section, typeattrubute):
        item = driver.find_element(By.XPATH, locatorsReader.readLocator(section, locator))
        area = item.size.get(typeattrubute)
        return area

    def find_height_and_width_id(self, locator, section, typeattrubute):
        item = driver.find_element(By.ID, locatorsReader.readLocator(section, locator))
        area = item.size.get(typeattrubute)
        return area

    def click_element(self, locator, section):
        if locator.lower().endswith("id"):
            driver.find_element(By.ID, locatorsReader.readLocator(section, locator)).click()
        else:
            driver.find_element(By.XPATH, locatorsReader.readLocator(section, locator)).click()
