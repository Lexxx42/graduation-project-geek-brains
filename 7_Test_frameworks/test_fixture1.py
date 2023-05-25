from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://demoqa.com/'


class TestMainPage1:

    @classmethod
    def setup_class(cls):
        print('\nstart browser for test suite..')
        cls.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        print('quit browser for test suite..')
        cls.browser.quit()

    def test_guest_should_see_banner_image(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, '.banner-image')

    def test_guest_should_see_elements_card_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][.//h5[text()="Elements"]]')


class TestMainPage2:

    def setup_method(self):
        print('start browser for test..')
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print('quit browser for test..')
        self.browser.quit()

    def test_guest_should_see_banner_image(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, '.banner-image')

    def test_guest_should_see_elements_card_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.XPATH, '//*[@class="card mt-4 top-card"][.//h5[text()="Elements"]]')
