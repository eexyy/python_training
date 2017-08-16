# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def returnToGroups(self, wd):
        wd.find_element_by_link_text("group page").click()

    def createNewGroup(self, wd):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("yar1")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("123")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("123")
        wd.find_element_by_name("submit").click()

    def openGroup(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd):
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def openHomePage(self, wd):
        wd.get("http://localhost/addressbook/")

    def test_test(self):
        success = True
        wd = self.wd
        self.openHomePage(wd)

        self.login(wd)
        self.openGroup(wd)
        self.createNewGroup(wd)
        self.returnToGroups(wd)
        self.Logout(wd)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
