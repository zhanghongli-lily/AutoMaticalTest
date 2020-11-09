from  ..common.BasePage import BasePage


class BaiduPage(BasePage):
    def __init__(self, type= "chrome"):
       super(BaiduPage, self).__init__(type = "chrome")
    def index(self, input, button):

        ele = self.find_element_by_id(input)
        ele.clear()
        self.send_Keys(self, ele, input)
        self.find_element_by_id(button)