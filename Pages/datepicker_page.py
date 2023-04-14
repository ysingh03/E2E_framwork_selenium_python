import datetime

from selenium.webdriver.common.by import By
from Base import locatorsReader


class Date_picker:
    def __init__(self, focusdriver, section):
        global driver
        driver = focusdriver
        self.section = section

    def click_date_button(self, locator):
        date_btn = driver.find_element(By.ID, locatorsReader.readLocator(self.section, locator))
        date_btn.click()

    def click_current_date(self, locator):
        current_date = driver.find_element(By.XPATH, locatorsReader.readLocator(self.section, locator))
        current_date.click()

    def text_from_textbox(self, locator):
        element = driver.find_element(By.ID, locatorsReader.readLocator(self.section, locator))
        return element.text

    def click_on_specific_date(self, specific_day, selected_month, month, selected_year, year, direction):
        while True:
            current_month = driver.find_element(By.XPATH, locatorsReader.readLocator(self.section, month)).text
            current_year = driver.find_element(By.XPATH, locatorsReader.readLocator(self.section, year)).text
            if current_year == selected_year and current_month == selected_month:
                selectdate = f"//a[text()={specific_day}]"
                driver.find_element(By.XPATH, selectdate).click()
                break
            else:
                driver.find_element(By.XPATH, locatorsReader.readLocator(self.section, direction)).click()
