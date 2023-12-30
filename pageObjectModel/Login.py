from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver

    txtSingUp = (By.XPATH, "//div[@class='signup-form']/h2")
    inputName = (By.CSS_SELECTOR, "input[name= 'name']")
    inputEmail = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    btnSingUp = (By.CSS_SELECTOR, "button[data-qa='signup-button']")
    txtLogin = (By.XPATH, "//div[@class='login-form']/h2")
    inputEmailLoggin = (By.CSS_SELECTOR,"input[data-qa='login-email']")
    inputPasswordLoggin = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    btnLogin = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    txtIncorrect = (By.XPATH, "//div[@class='login-form']/form/p")
    txtSingUpIncorrect = (By.XPATH, "//div[@class='signup-form']/form/p")


    def txtSingUpMethod(self):
        return self.driver.find_element(*Login.txtSingUp)

    def inputNameMethod(self):
        return self.driver.find_element(*Login.inputName)

    def inputEmailMethod(self):
        return self.driver.find_element(*Login.inputEmail)

    def btnSingUpMethod(self):
        return self.driver.find_element(*Login.btnSingUp)

    def txtLoginMethod(self):
        return self.driver.find_element(*Login.txtLogin)

    def inputEmailLogginMethod(self):
        return self.driver.find_element(*Login.inputEmailLoggin)

    def inputPasswordLogginMethod(self):
        return self.driver.find_element(*Login.inputPasswordLoggin)

    def btnLoginMethod(self):
        return self.driver.find_element(*Login.btnLogin)

    def txtIncorrectMethod(self):
        return self.driver.find_element(*Login.txtIncorrect)

    def txtSingUpIncorrectMethod(self):
        return self.driver.find_element(*Login.txtSingUpIncorrect)