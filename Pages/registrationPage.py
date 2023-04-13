from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Base import locatorsReader


class reg:

    def __init__(self, focusdriver, section):
        global driver
        driver = focusdriver
        self.section = section

    def enter_Data_Using_Xpath(self, locator, data):
        self.enterdata = driver.find_element(By.XPATH, locatorsReader.readLocator(self.section, locator))
        self.enterdata.clear()
        self.enterdata.send_keys(data)

    def enter_Data_Using_Name(self, locator, data):
        self.enterdata = driver.find_element(By.NAME, locatorsReader.readLocator(self.section, locator))
        self.enterdata.clear()
        self.enterdata.send_keys(data)

    def enter_Data_Using_Tagname(self, locator, data):
        self.enterdata = driver.find_element(By.TAG_NAME, locatorsReader.readLocator(self.section, locator))
        self.enterdata.clear
        self.enterdata.send_keys(data)

    def click_element(self, locator):
        driver.find_element(By.XPATH, locatorsReader.readLocator(self.section, locator)).click()

    def select_Item_In_Dropdown(self, locator, itemtoselect):
        dd = Select(driver.find_element(By.XPATH, locatorsReader.readLocator(self.section, locator)))
        dd.select_by_visible_text(itemtoselect)



