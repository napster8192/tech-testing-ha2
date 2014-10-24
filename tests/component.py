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
    EDIT = '/html/body/div[1]/div[5]/div[1]/div[2]/div/ul/li[1]/div[2]/div[1]/div[3]/div/ul/li[3]/a'
    DELETE = '/html/body/div[1]/div[5]/div[1]/div[2]/div/ul/li[1]/div[2]/div[1]/div[3]/div/ul/li[4]/span'

    def click_edit(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDIT)
        ).click()

    def click_delete(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE)
        ).click()

class Triangle(Component):
    INCOME = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[7]/div/div[2]/ul/li[29]/div/div[2]/span'
    INTERESTS = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[7]/div/div[2]/ul/li[21]/div/div[2]/span'

    def click_income(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INCOME)
        ).click()

    def click_interests(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INTERESTS)
        ).click()

class Checkbox(Component):
    AVTO = '//*[@id="interests1"]/label'
    INCOME_HIGH = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[7]/div/div[2]/ul/li[29]/div/div[2]/div/div/ul/li[1]/label'
    INCOME_MEDUIM = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[7]/div/div[2]/ul/li[29]/div/div[2]/div/div/ul/li[2]/label'

    def check_avto(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.AVTO)
        ).click()

    def check_income_high(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INCOME_HIGH)
        ).click()

    def check_income_medium(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INCOME_MEDUIM)
        ).click()

    def avto_is_selected(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.AVTO)
        ).is_selected()

    def income_high_is_selected(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INCOME_HIGH)
        ).is_selected()

    def income_medium_is_selected(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INCOME_MEDUIM)
        ).is_selected()

class Text(Component):
    HEAD = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[2]/input'
    TEXT = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[3]/textarea'
    LINK = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[4]/span[2]/input'
    IMAGE = 'input[data-name="image"]'
    CREATE = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[3]/input'

    def set_head(self, head):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.HEAD)
        ).send_keys(head)

    def set_text(self, text):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT)
        ).send_keys(text)

    def set_link(self, link):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LINK)
        ).send_keys(link)

    def set_image(self, address):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.IMAGE)
        ).send_keys(address)

    def click_add_ads(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CREATE)
        ).click()

class Ad(Component):
    AD = '/html/body/div[1]/div[5]/div/div[2]/div/div[2]/div[2]/span'

    def click_ads(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.AD)
        ).click()
