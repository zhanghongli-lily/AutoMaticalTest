from  ..common.BasePage import BasePage


class BaiduPage(BasePage):
    def __init__(self, type= "chrome"):
       super(BaiduPage, self).__init__(type = "chrome")
    def index(self, input, button):

        self.find_element_by_id(input)
        self.clear()
        self
        self.find_element_by_id(button)