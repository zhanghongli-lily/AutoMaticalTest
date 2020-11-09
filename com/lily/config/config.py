import os
url="https://www.baidu.com";

BasePath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
DriverPath = os.path.join(BasePath, 'driverpath')
ReportPath = os.path.join(BasePath, "reports")
CasePath = os.path.join(BasePath, "testcases/cases")
logPath = os.path.join(BasePath, "logs")
ConfigPath = os.path.join(BasePath, "config")





# print(DriverPath)