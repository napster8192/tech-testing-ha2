import os

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from page import *

class Test(unittest.TestCase):

    USERNAME = 'tech-testing-ha2-19@bk.ru'
    PASSWORD = os.environ['TTHA2PASSWORD']
    DOMAIN = '@bk.ru'
    IMAGE = os.path.abspath('img.jpg')

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_domain(self.DOMAIN)
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

    def tearDown(self):
        self.driver.quit()

    # def test_email(self):
    #     create_page = CreatePage(self.driver)
    #     create_page.open()
    #     email = create_page.top_menu.get_email()
    #
    #     self.assertEqual(self.USERNAME, email)

    def test_create_ad(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.text.set_head('a new big ad')
        create_page.text.set_text('there is a big text')
        create_page.text.set_link('www.target.mail.ru')
        create_page.text.set_image(self.IMAGE)

        create_page.triangle.click_interests()
        create_page.checkbox.check_avto()
        create_page.triangle.click_income()
        create_page.checkbox.check_income_high()
        create_page.checkbox.check_income_medium()

        create_page.ads.click_ads()
        create_page.edit.click_edit()

        self.assertEquals(True, create_page.checkbox.avto_is_selected())
        self.assertEquals(True, create_page.checkbox.income_high_is_selected())
        self.assertEquals(True, create_page.checkbox.income_medium_is_selected())

        create_page = EditPage(self.driver)
        create_page.open()
        create_page.edit.click_delete()

        # ## And some examples
        # create_page.slider.move(100)
        # FILE_PATH = '/Users/bayandin/repos/tech-testing-selenium-demo/img.jpg'
        # element = WebDriverWait(self.driver, 30, 0.1).until(
        #     lambda d: d.find_element_by_css_selector('.banner-form__img-file')
        # )
        #
        # element.send_keys(FILE_PATH)
