from selenium.webdriver.common.by import By


class TestCasesPage:
    def __init__(self, driver):
        self.driver = driver

    txtTestCases = (By.XPATH, "//div[@class='col-sm-9 col-sm-offset-1']/h2")

    def txtTestCasesMethod(self):
        return self.driver.find_element(*TestCasesPage.txtTestCases)