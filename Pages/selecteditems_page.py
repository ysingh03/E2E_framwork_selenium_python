from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from Base import locatorsReader


class Selected_Item:
    def __init__(self, focusdriver, section):
        global driver
        driver = focusdriver
        self.section = section

    def click_item(self, locator):
        item = driver.find_element(By.XPATH, locatorsReader.readLocator(self.section, locator))
        item.click()

    def press_ctrl_and_click(self, locator):
        ac = ActionChains(driver)
        item = driver.find_element(By.XPATH, locatorsReader.readLocator(self.section, locator))
        ac.key_down(Keys.CONTROL)
        ac.click(item)
        ac.key_up(Keys.CONTROL)
        ac.perform()

    def selected_items(self, locator):
        items = driver.find_elements(By.XPATH, locatorsReader.readLocator(self.section, locator))
        itemcount = len(items)
        return itemcount

    def selected_items_by_loops(self, locator, items):
        allitems = driver.find_elements(By.XPATH, locatorsReader.readLocator(self.section, locator))
        to_select_item = ['Item 1', 'Item 3', 'Item 4', 'Item 7']
        for allitem in allitems:
            if allitem == to_select_item:
                pass

    def Add_New_Contract(self, locator):
        # Menu_Transaction= "//li[@class='nav-item menu-is-opening menu-open']//ul[@class='nav nav-treeview']"
        AllmenuCSS = "li[class='nav-item'] a"
        Allitems = driver.find_elements(By.XPATH, locatorsReader.readLocator(self.section, locator))
        for menu_name in Allitems:
            if menu_name.text in "BOQ":
                menu_name.click()
                break


