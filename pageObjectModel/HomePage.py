from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    textHome = (By.XPATH, "//h2[contains(text(),'Features Items')]")
    btnSingUpLogin = (By.XPATH, "//ul[@class='nav navbar-nav']/li[4]")
    txtLogged = (By.XPATH, "//ul[@class='nav navbar-nav']/li[10]")
    btnDeleteAccount = (By.XPATH, "//a[contains(text(),'Delete Account')]")
    txtAccountDeleted = (By.CSS_SELECTOR, "h2[data-qa='account-deleted']")
    btnDeleteAccountContinue = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    btnLogout = (By.XPATH, "//ul[@class='nav navbar-nav']/li[4]")
    btnContactUs = (By.XPATH, "//ul[@class='nav navbar-nav']/li[8]")
    btnTestCases = (By.XPATH, "//ul[@class='nav navbar-nav']/li[5]")
    btnProducts = (By.XPATH, "//ul[@class='nav navbar-nav']/li[2]")


    def textHomeMethod(self):
        return self.driver.find_element(*HomePage.textHome)

    def btnSingUpLoginMethod(self):
        return self.driver.find_element(*HomePage.btnSingUpLogin)

    def txtLoggedMethod(self):
        return self.driver.find_element(*HomePage.txtLogged)

    def btnDeleteAccountMethod(self):
        return self.driver.find_element(*HomePage.btnDeleteAccount)

    def txtAccountDeletedMethod(self):
        return self.driver.find_element(*HomePage.txtAccountDeleted)

    def btnDeleteAccountContinueMethod(self):
        return self.driver.find_element(*HomePage.btnDeleteAccountContinue)

    def btnLogoutMethod(self):
        return self.driver.find_element(*HomePage.btnLogout)

    def btnContactUsMethod(self):
        return self.driver.find_element(*HomePage.btnContactUs)

    def btnTestCasesMethod(self):
        return self.driver.find_element(*HomePage.btnTestCases)

    def btnProductsMethod(self):
        return self.driver.find_element(*HomePage.btnProducts)

