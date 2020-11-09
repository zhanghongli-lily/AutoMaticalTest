import  unittest
from ..config.config import CasePath,ReportPath
import os
from HtmlTestRunner import  HTMLTestRunner
def loadTestCases():

        testSuit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(CasePath, pattern="test*.py", top_level_dir=None)
        for test_suit in discover:
            for testcase in test_suit:
                testSuit.addTests(testcase)
        return testSuit

def RunTestCases():
         report_title = "测试报告测试"
         result_path = os.path.join(ReportPath, report_title)
         with open(result_path,"wb") as file:
            runner= HTMLTestRunner(stream=file,title="report_title",descriptions=r"自动化测试报告",Author="Lily")
            runner.run(loadTestCases())

if __name__ == '__main__':
         RunTestCases()

