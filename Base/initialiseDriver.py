from selenium import webdriver

driver = webdriver.Chrome()


def startBrowser(url):
    """
    This is to start the chrome browser and open way2automation testing website.
    :return: driver
    """
    driver.get(url)
    driver.maximize_window()
    return driver


def stopBrowser():
    driver.quit()
