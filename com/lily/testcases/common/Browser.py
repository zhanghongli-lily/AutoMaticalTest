from selenium import webdriver;

from com.lily.config.config import DriverPath

ChromeDriver_Path=DriverPath + "\chromedriver.exe"
IeDriver_Path = DriverPath + "\IEDriverServer.exe"


drivers_type = {
    "chrome": webdriver.Chrome(),
    "firefox": webdriver.Firefox(),
    "ie": webdriver.Ie()
}

drivers_exetuble = {
    "chrome": ChromeDriver_Path,
    "firefox": "wires",
    "ie": IeDriver_Path
}


class UnsupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, type="chrome"):
        self._type = type.lower();
        if type in drivers_type:
             self.browser = drivers_type[self._type]
        else:
             raise  UnsupportBrowserTypeError("仅支持%s" % ",".join(drivers_type.keys()));
        self.driver = self.browser(executable_path = drivers_exetuble[self._type])