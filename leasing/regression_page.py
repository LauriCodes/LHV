from selenium import webdriver

from leasing_page import LeasingPage


# Test Setup
browser = webdriver.Chrome()


# LHV Lease Page
lease_page = LeasingPage(driver=browser)
lease_page.go()
lease_page.iframe.switch("iframe")
lease_page.vehicle_price_input.input_text("10000")
lease_page.downpayment_input.input_text("20")
lease_page.lease_period_dropdown.select(3)
lease_page.residual_value_input.input_text("15")
lease_page.next_button.click()
lease_page.quit()
print("Regression Test Passed")
