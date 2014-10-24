__author__ = 'nap'

from component import *
import urlparse

class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)


class CreatePage(Page):
    PATH = '/ads/create'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def slider(self):
        return Slider(self.driver)

    @property
    def triangle(self):
        return Triangle(self.driver)

    @property
    def checkbox(self):
        return Checkbox(self.driver)

    @property
    def text(self):
        return Text(self.driver)

    @property
    def ads(self):
        return Ad(self.driver)

    @property
    def edit(self):
        return Edit(self.driver)

    @property
    def place(self):
        return Place(self.driver)

class EditPage(Page):
    PATH = 'ads/campaigns'

    @property
    def edit(self):
        return Edit(self.driver)

