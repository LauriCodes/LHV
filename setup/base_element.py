from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(
            self.driver, 10).until(
            EC.presence_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def input_text(self, txt):
        text = self.web_element.send_keys(txt)
        return text

    def click(self):
        element = WebDriverWait(
            self.driver, 30).until(
            EC.element_to_be_clickable(locator=self.locator))
        self.driver.execute_script("arguments[0].click();", element)
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    def switch(self, locator):
        self.driver.switch_to.frame(locator)
        return None

    def select(self, index):
        Select(self.web_element).select_by_index(index)
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

