from selenium.webdriver.common.by import By

link = 'https://demoqa.com/'


def test_guest_should_see_banner_image(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.banner-image')
