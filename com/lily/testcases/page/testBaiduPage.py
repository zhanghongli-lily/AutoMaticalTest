from ..common.BasePage import BasePage
import time
class TestBaiduPage(BasePage):
   def __init__(self,type="chrome"):
      super(BasePage,type)
   def  testBaidu(self):
      sousuo= self.find_element_by_id("kw");
      time.sleep(3);
      sousuo.sendKeys("python");
      time.sleep(3);
      aniu=self.find_element_by_id("su");
      time.sleep(3);
      aniu.click();
      print("hahah")

