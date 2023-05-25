import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://demoqa.com/'


@pytest.fixture
def browser():
    print('\nstart browser')
    browser = webdriver.Chrome()
    return browser
    print('\nquit browser')
    browser.quit()


class TestMainPage1:
    def test_guest_should_see_banner_image(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.banner-image')

    def test_guest_should_see_elements_card_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][.//h5[text()="Elements"]]')
