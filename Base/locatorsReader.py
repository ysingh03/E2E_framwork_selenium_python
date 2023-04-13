import configparser


def readLocator(section, key):
    reader = configparser.ConfigParser()
    path = 'ConfigData/locators.cfg'
    reader.read(path)
    return reader.get(section, key)
