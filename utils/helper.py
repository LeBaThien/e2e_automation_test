import os
import json
from selenium import webdriver

CONFIG = None

def get_driver():
    browser = os.getenv('browser', 'chrome').lower()
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def load_config():
    global CONFIG
    if CONFIG is None:
        config_path = os.path.join(os.path.dirname(__file__), '../config/config.json')
        with open(config_path) as config_file:
            CONFIG = json.load(config_file)
    return CONFIG
