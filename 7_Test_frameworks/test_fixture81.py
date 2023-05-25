import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://demoqa.com/'


@pytest.fixture(scope='function')
def browser():
    print('\nstart browser')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser')
    browser.quit()


class TestMainPage1:
    @pytest.mark.smoke
    def test_guest_should_see_banner_image(self, browser):
        print('smoke test 1')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '.banner-image')

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_elements_card_on_the_main_page(self, browser):
        print('smoke test 2')
        browser.get(link)
        browser.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][.//h5[text()="Elements"]]')
