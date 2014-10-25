__author__ = 'nap'

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait

class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '#id_Login'
    PASSWORD = '#id_Password'
    DOMAIN = '#id_Domain'
    SUBMIT = '#gogogo>input'

    def set_login(self, login):
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(pwd)

    def set_domain(self, domain):
        select = self.driver.find_element_by_css_selector(self.DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()


class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class Slider(Component):
    SLIDER = '.price-slider__begunok'

    def move(self, offset):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SLIDER)
        )
        ac = ActionChains(self.driver)
        ac.click_and_hold(element).move_by_offset(offset, 0).perform()

class Edit(Component):
    EDIT = '.campaign-row .control__link_edit'
    DELETE = '.control__preset_delete'

    def click_edit(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EDIT)
        ).click()

    def click_delete(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.DELETE)
        ).click()

class Triangle(Component):
    INCOME = '[data-name="income_group"] > .campaign-setting__value.js-setting-value'
    INTERESTS = '[data-node-id="interests"]'

    def click_income(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INCOME)
        ).click()

    def click_interests(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INTERESTS)
        ).click()

class Checkbox(Component):
    AVTO = '#interests1 > input'
    INCOME_HIGH = '#income_group-9288'
    INCOME_MEDUIM = '#income_group-9287'
    INCOME_LOW = '#income_group-9286'

    def check_avto(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.AVTO)
        ).click()

    def check_income_high(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INCOME_HIGH)
        ).click()

    def check_income_medium(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INCOME_MEDUIM)
        ).click()

    def avto_is_selected(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.AVTO)
        ).is_selected()

    def income_high_is_selected(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INCOME_HIGH)
        ).is_selected()

    def income_medium_is_selected(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INCOME_MEDUIM)
        ).is_selected()

    def income_low_is_selected(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.INCOME_LOW)
        ).is_selected()

class Text(Component):
    HEAD = 'input[data-name="title"]'
    TEXT = 'textarea[data-name="text"]'
    LINK = 'li.banner-form__row:nth-child(4) > span:nth-child(2) > input:nth-child(1)'
    IMAGE = 'input[data-name="image"]'
    CREATE = '.banner-form__save-button'

    def set_head(self, head):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.HEAD)
        ).send_keys(head)

    def set_text(self, text):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TEXT)
        ).send_keys(text)

    def set_link(self, link):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.LINK)
        ).send_keys(link)

    def set_image(self, address):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.IMAGE)
        ).send_keys(address)

    def click_add_ads(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CREATE)
        ).click()

class Ad(Component):
    AD = '.main-button-new'

    def click_ads(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.AD)
        ).click()

class Place(Component):
    PLACE = '.base-setting__pads-item__label'

    def get_place(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PLACE).text
        )
