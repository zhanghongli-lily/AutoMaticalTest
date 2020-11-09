from com.lily.testcases.common.Browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from com.lily.config.config import url


class BasePage(Browser):
    def __init__(self, type="chrome"):
        super(Browser, self).__init__(type=type)

    def get(self):

        self.driver.get(url)

    def find_element_by_id(self, id):
        try:
            WebDriverWait(self.driver.find_element_by_id(By.ID, id), 5)
        except Exception as e:
            print("定位失败：%s", e)

    def find_element_by_name(self, name):
        try:
            self.driver.find_element_by_name(By.NAME, name)
        except Exception as e:
            print("定位失败：%s", e)

    def find_element_by_class_name(self, class_name):
        try:
            self.driver.find_element_by_class_name(By.CLASS_NAME, class_name)
        except Exception as e:
            print("定位失败：%s", e)

    def find_element_by_tag_name(self, tag_name):
        try:
            self.driver.find_element_by_tag_name(By.TAG_NAME, tag_name)
        except Exception as e:
            print("定位失败：%s", e);

    def find_element_by_link_text(self, link_text):
        try:
            self.driver.find_element_by_link_text(By.LINK_TEXT, link_text);
        except Exception as e:
            print("定位失败：%s", e)

    def find_element_by_link_partial_text(self, link_partial_text):
        try:
            self.driver.find_element_by_link_text(By.PARTIAL_LINK_TEXT, link_partial_text)
        except Exception as e:
            print("定位失败：%s", e)

    def find_elements_by_css_selector(self, css_selector):
        try:
            self.driver.find_element_by_class_name(By.CSS_SELECTOR, css_selector)

        except Exception as e:
            print("定位失败：%s", e)

    def find_elements_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(By.XPATH, xpath)

        except Exception as e:
            print("定位失败：%s", e)

    def clear(self):

        self.driver.clear()

    def send_Keys(self, element, text):
        # element=(By.ID,"#kw")
        try:

            ele = self.driver.find_element(element)
            ele.send_keys(text)

        except Exception as e:

            print("发送失败：%s", e)
