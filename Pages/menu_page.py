import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Base import locatorsReader
from selenium import webdriver

driver = webdriver.Chrome()
class Menu:
    def __init__(self, focusdriver, section):
        global driver
        driver = focusdriver
        self.section = section

    def hover_on_menu_element(self, listofitems, texttoverified):
        for i in listofitems:
            element = driver.find_element(By.XPATH, f"//div[text()='{i}']")
            ac = ActionChains(driver)
            ac.move_to_element(element)
            ac.perform()
            time.sleep(2)

        element1 = driver.find_element(By.XPATH, f"//div[text()='{texttoverified}']")
        return element1.is_displayed()