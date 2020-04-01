from selenium import webdriver
from time import sleep

from secrets import username, password

class facebookAutomate():
    def _init_(self):
        self.driver = webdriver.Chrome()

   