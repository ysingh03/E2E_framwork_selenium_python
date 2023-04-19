import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Base import locatorsReader

class Alerts:
    def __init__(self, focusdriver, section):
        global driver
        driver = focusdriver
        self.section = section

    def click_button(self, locator):
        element = driver.find_element(By.XPATH, locatorsReader.readLocator(self.section, locator))
        element.click()

    def click_simple_alert_box(self):
        alert = driver.switch_to.alert
        alert.accept()
        driver.switch_to.default_content()

    def click_input_alert_box(self):
        alert = driver.switch_to.alert
        alert.send_keys("Yogesh")
        alert.accept()
        driver.switch_to.default_content()

    def dismiss_alert_box(self):
        alert = driver.switch_to.alert
        alert.send_keys("Yogesh")
        alert.dismiss()
        driver.switch_to.default_content()

