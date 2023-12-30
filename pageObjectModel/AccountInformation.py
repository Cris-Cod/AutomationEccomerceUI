from selenium.webdriver.common.by import By


class AccountInformation:

    def __init__(self, driver):
        self.driver = driver

    txtAccountInformation = (By.XPATH, "//b[contains(text(),'Enter Account Information')]")
    gender = (By.CSS_SELECTOR, "#id_gender1")
    password = (By.ID, "password")
    selectDays = (By.ID, "days")
    selectMonth = (By.ID, "months")
    selectYears = (By.ID, "years")
    radioNewsletter = (By.ID, "newsletter")
    firstName = (By.ID, "first_name")
    lastName = (By.ID, "last_name")
    company = (By.ID, "company")
    address1 = (By.ID, "address1")
    selectCountry = (By.ID, "country")
    state = (By.ID, "state")
    city = (By.ID, "city")
    zipCode = (By.ID, "zipcode")
    mobileNumber = (By.ID, "mobile_number")
    btnCreateAccount = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    txtAccountCreated = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    btnContinue = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def txtAccountInformationMethod(self):
        return self.driver.find_element(*AccountInformation.txtAccountInformation)

    def genderMethod(self):
        return self.driver.find_element(*AccountInformation.gender)

    def passwordMethod(self):
        return self.driver.find_element(*AccountInformation.password)

    def selectDaysMethod(self):
        return self.driver.find_element(*AccountInformation.selectDays)

    def selectMonthMethod(self):
        return self.driver.find_element(*AccountInformation.selectMonth)

    def selectYearsMethod(self):
        return self.driver.find_element(*AccountInformation.selectYears)

    def radioNewsletterMethod(self):
        return self.driver.find_element(*AccountInformation.radioNewsletter)

    def firstNameMethod(self):
        return self.driver.find_element(*AccountInformation.firstName)

    def lastNameMethod(self):
        return self.driver.find_element(*AccountInformation.lastName)

    def companyMethod(self):
        return self.driver.find_element(*AccountInformation.company)

    def address1Method(self):
        return self.driver.find_element(*AccountInformation.address1)

    def selectCountryMethod(self):
        return self.driver.find_element(*AccountInformation.selectCountry)

    def stateMethod(self):
        return self.driver.find_element(*AccountInformation.state)

    def cityMethod(self):
        return self.driver.find_element(*AccountInformation.city)

    def zipCodeMethod(self):
        return self.driver.find_element(*AccountInformation.zipCode)

    def mobileNumberMethod(self):
        return self.driver.find_element(*AccountInformation.mobileNumber)

    def btnCreateAccountMethod(self):
        return self.driver.find_element(*AccountInformation.btnCreateAccount)

    def txtAccountCreatedMethod(self):
        return self.driver.find_element(*AccountInformation.txtAccountCreated)

    def btnContinueMethod(self):
        return self.driver.find_element(*AccountInformation.btnContinue)