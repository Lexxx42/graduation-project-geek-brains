from selenium import webdriver
from selenium.webdriver.common.by import By

new_tab_button_locator = (By.CSS_SELECTOR, '#tabButton')
sample_text_locator = (By.CSS_SELECTOR, '#sampleHeading')

browser = webdriver.Chrome()
browser_windows_page_link = 'https://demoqa.com/browser-windows'
browser.get(browser_windows_page_link)

new_tab_button = browser.find_element(*new_tab_button_locator)
new_tab_button.click()

browser.switch_to.window(browser.window_handles[1])

sample_text_element = browser.find_element(*sample_text_locator)
actual_sample_text = sample_text_element.text
expected_sample_text = 'This is a sample page'

assert actual_sample_text == expected_sample_text, \
    f'Expected {expected_sample_text=} in new tab ' \
    f'to be equal to {actual_sample_text=}.'
