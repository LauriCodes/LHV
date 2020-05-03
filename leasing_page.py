from selenium.webdriver.common.by import By

from setup.base_element import BaseElement
from setup.base_page import BasePage
from setup.locator import Locator


class LeasingPage(BasePage):
    url = "https://www.lhv.ee/et/liising/taotlus"

    @property
    def iframe(self):
        locator = Locator(By.CSS_SELECTOR, "iframe")
        return BaseElement(self.driver, locator=locator)

    @property
    def vehicle_price_input(self):
        locator = Locator(By.CSS_SELECTOR, "input#origin-price")
        return BaseElement(self.driver, locator=locator)

    @property
    def downpayment_input(self):
        locator = Locator(By.CSS_SELECTOR, "input#initial_percentage")
        return BaseElement(self.driver, locator=locator)

    @property
    def lease_period_dropdown(self):
        locator = Locator(By.CSS_SELECTOR, "select#duration_years")
        return BaseElement(self.driver, locator=locator)

    @property
    def residual_value_input(self):
        locator = Locator(By.CSS_SELECTOR, "input#reminder_percentage")
        return BaseElement(self.driver, locator=locator)

    @property
    def next_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button[value="Edasi"]')
        return BaseElement(self.driver, locator=locator)
