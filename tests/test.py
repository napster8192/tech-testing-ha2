# -*- coding: utf-8 -*-

import os

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from page import *

class Test(unittest.TestCase):

    USERNAME = 'tech-testing-ha2-19@bk.ru'
    PASSWORD = os.environ['TTHA2PASSWORD']
    DOMAIN = '@bk.ru'
    IMAGE = os.path.abspath('img.jpg')

    HEAD = 'a new big ad'
    TEXT = 'there is a big text'
    LINK = 'www.target.mail.ru'

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

    def test_email(self):
        create_page = CreatePage(self.driver)
        create_page.open()
        email = create_page.top_menu.get_email()

        self.assertEqual(self.USERNAME, email)

    def test_case_1(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.text.set_head(self.HEAD)
        create_page.text.set_text(self.TEXT)
        create_page.text.set_link(self.LINK)
        create_page.text.set_image(self.IMAGE)

        create_page.triangle.click_interests()
        create_page.checkbox.check_avto_1()
        create_page.triangle.click_income()
        create_page.checkbox.check_income_high()
        create_page.checkbox.check_income_medium()

        create_page.ads.click_ads()
        create_page.edit.click_edit()

        self.assertEquals(u'Социальные сети и сервисы (Одноклассники.Ру, МойМир@Mail.Ru, Почта@Mail.ru и др.)', create_page.place.get_place())
        self.assertEquals(True, create_page.checkbox.avto_1_is_selected())
        self.assertEquals(True, create_page.checkbox.income_high_is_selected())
        self.assertEquals(True, create_page.checkbox.income_medium_is_selected())
        self.assertEquals(False, create_page.checkbox.income_low_is_selected())

    def test_case_2(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.text.set_head(self.HEAD)
        create_page.text.set_text(self.TEXT)
        create_page.text.set_link(self.LINK)
        create_page.text.set_image(self.IMAGE)

        create_page.triangle.click_interests()
        create_page.triangle.click_avto()
        create_page.checkbox.check_avto_5()
        create_page.checkbox.check_avto_6()
        create_page.triangle.click_income()
        create_page.checkbox.check_income_low()

        create_page.ads.click_ads()
        create_page.edit.click_edit()

        self.assertEquals(u'Социальные сети и сервисы (Одноклассники.Ру, МойМир@Mail.Ru, Почта@Mail.ru и др.)', create_page.place.get_place())
        self.assertEquals(False, create_page.checkbox.avto_1_is_selected())
        create_page.triangle.click_interests()
        create_page.triangle.click_avto()
        self.assertEquals(False, create_page.checkbox.avto_2_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_3_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_4_is_selected())
        self.assertEquals(True, create_page.checkbox.avto_5_is_selected())
        self.assertEquals(True, create_page.checkbox.avto_6_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_7_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_8_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_9_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_10_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_11_is_selected())
        self.assertEquals(False, create_page.checkbox.income_high_is_selected())
        self.assertEquals(False, create_page.checkbox.income_medium_is_selected())
        self.assertEquals(True, create_page.checkbox.income_low_is_selected())

    def test_case_3(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.text.set_head(self.HEAD)
        create_page.text.set_text(self.TEXT)
        create_page.text.set_link(self.LINK)
        create_page.text.set_image(self.IMAGE)

        create_page.triangle.click_interests()
        create_page.triangle.click_avto()
        create_page.checkbox.check_avto_3()
        create_page.checkbox.check_avto_10()
        create_page.triangle.click_income()
        create_page.checkbox.check_income_high()

        create_page.ads.click_ads()
        create_page.edit.click_edit()

        self.assertEquals(u'Социальные сети и сервисы (Одноклассники.Ру, МойМир@Mail.Ru, Почта@Mail.ru и др.)', create_page.place.get_place())
        self.assertEquals(False, create_page.checkbox.avto_1_is_selected())
        create_page.triangle.click_interests()
        create_page.triangle.click_avto()
        self.assertEquals(False, create_page.checkbox.avto_2_is_selected())
        self.assertEquals(True, create_page.checkbox.avto_3_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_4_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_5_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_6_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_7_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_8_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_9_is_selected())
        self.assertEquals(True, create_page.checkbox.avto_10_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_11_is_selected())
        self.assertEquals(True, create_page.checkbox.income_high_is_selected())
        self.assertEquals(False, create_page.checkbox.income_medium_is_selected())
        self.assertEquals(False, create_page.checkbox.income_low_is_selected())

    def test_case_4(self):
        create_page = CreatePage(self.driver)
        create_page.open()

        create_page.text.set_head(self.HEAD)
        create_page.text.set_text(self.TEXT)
        create_page.text.set_link(self.LINK)
        create_page.text.set_image(self.IMAGE)

        create_page.triangle.click_interests()
        create_page.triangle.click_avto()
        create_page.checkbox.check_avto_2()
        create_page.checkbox.check_avto_11()
        create_page.triangle.click_income()
        create_page.checkbox.check_income_medium()

        create_page.ads.click_ads()
        create_page.edit.click_edit()

        self.assertEquals(u'Социальные сети и сервисы (Одноклассники.Ру, МойМир@Mail.Ru, Почта@Mail.ru и др.)', create_page.place.get_place())
        self.assertEquals(False, create_page.checkbox.avto_1_is_selected())
        create_page.triangle.click_interests()
        create_page.triangle.click_avto()
        self.assertEquals(True, create_page.checkbox.avto_2_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_3_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_4_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_5_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_6_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_7_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_8_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_9_is_selected())
        self.assertEquals(False, create_page.checkbox.avto_10_is_selected())
        self.assertEquals(True, create_page.checkbox.avto_11_is_selected())
        self.assertEquals(False, create_page.checkbox.income_high_is_selected())
        self.assertEquals(True, create_page.checkbox.income_medium_is_selected())
        self.assertEquals(False, create_page.checkbox.income_low_is_selected())
