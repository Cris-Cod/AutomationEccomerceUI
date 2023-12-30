from pageObjectModel.AccountInformation import AccountInformation
from pageObjectModel.HomePage import HomePage
from pageObjectModel.Login import Login
from utilities.BaseClass import BaseClass
import pytest


class TestCases(BaseClass):

    def test_cases_1_Register_User(self):

        home_text = "FEATURES ITEMS"
        singUp_text = "New User Signup!"
        account_text = "ENTER ACCOUNT INFORMATION"
        account_created = "ACCOUNT CREATED!"
        logged_text = "Logged in as Mathew Perry"
        account_deleted_text = "Account Deleted!"

        homePage = HomePage(self.driver)
        loginPage = Login(self.driver)
        accountInformation = AccountInformation(self.driver)

        txtHome = homePage.textHomeMethod().text
        assert home_text == txtHome
        homePage.btnSingUpLoginMethod().click()
        txtSingUp = loginPage.txtSingUpMethod().text
        assert singUp_text == txtSingUp
        loginPage.inputNameMethod().send_keys("Mathew Perry")
        loginPage.inputEmailMethod().send_keys("netdisonn+star7@gmail.com")
        loginPage.btnSingUpMethod().click()
        txtAccount = accountInformation.txtAccountInformationMethod().text
        assert account_text == txtAccount
        accountInformation.genderMethod().click()
        accountInformation.passwordMethod().send_keys("123456")
        self.selectByText(accountInformation.selectDaysMethod(),"8")
        self.selectByText(accountInformation.selectMonthMethod(),"June")
        self.selectByText(accountInformation.selectYearsMethod(), "2016")
        accountInformation.radioNewsletterMethod().click()
        accountInformation.firstNameMethod().send_keys("Mathew")
        accountInformation.lastNameMethod().send_keys("Perry")
        accountInformation.companyMethod().send_keys("UNO")
        accountInformation.address1Method().send_keys("Calle 21 # 30")
        self.scroll()
        self.selectByText(accountInformation.selectCountryMethod(),"Canada")
        accountInformation.stateMethod().send_keys("Ontario")
        accountInformation.cityMethod().send_keys("Thunder Bay")
        accountInformation.zipCodeMethod().send_keys("ab25256")
        accountInformation.mobileNumberMethod().send_keys("3152154569")
        self.scroll()
        accountInformation.btnCreateAccountMethod().click()
        txtAccountCreated = accountInformation.txtAccountCreatedMethod().text
        assert account_created == txtAccountCreated
        accountInformation.btnContinueMethod().click()
        txtLogged = homePage.txtLoggedMethod().text
        assert logged_text == txtLogged
        homePage.btnDeleteAccountMethod().click()
        txt_account_deleted = homePage.txtAccountDeletedMethod().text
        assert account_deleted_text == txt_account_deleted.title()
        homePage.btnDeleteAccountContinueMethod().click()

    def test_cases_2_LoginUserWithCorrectEmailAndPassword(self):
        name = "Mathew Perry"
        home_text = "FEATURES ITEMS"
        login_text = "Login to your account"
        logged_text = f"Logged in as {name}"

        homePage = HomePage(self.driver)
        loginPage = Login(self.driver)

        txtHome = homePage.textHomeMethod().text
        assert home_text == txtHome
        homePage.btnSingUpLoginMethod().click()
        txtLogin = loginPage.txtLoginMethod().text
        assert login_text == txtLogin
        loginPage.inputEmailLogginMethod().send_keys("netdisonn+star10@gmail.com")
        loginPage.inputPasswordLogginMethod().send_keys("123456")
        loginPage.btnLoginMethod().click()
        txtLogged = homePage.txtLoggedMethod().text
        assert logged_text == txtLogged

    def test_cases_3_LoginUserWithIncorrectEmailAndPassword(self):
        home_text = "FEATURES ITEMS"
        login_text = "Login to your account"
        incorrect_text = "Your email or password is incorrect!"

        homePage = HomePage(self.driver)
        loginPage = Login(self.driver)

        txtHome = homePage.textHomeMethod().text
        assert home_text == txtHome
        homePage.btnSingUpLoginMethod().click()
        txtLogin = loginPage.txtLoginMethod().text
        assert login_text == txtLogin
        loginPage.inputEmailLogginMethod().send_keys("netdisonnstar10@gmail.com")
        loginPage.inputPasswordLogginMethod().send_keys("12345")
        loginPage.btnLoginMethod().click()
        textIncorrect = loginPage.txtIncorrectMethod().text
        assert incorrect_text == textIncorrect

    def test_cases_4_Logout_User(self):
        name = "Mathew Perry"
        home_text = "FEATURES ITEMS"
        login_text = "Login to your account"
        logged_text = f"Logged in as {name}"

        homePage = HomePage(self.driver)
        loginPage = Login(self.driver)

        txtHome = homePage.textHomeMethod().text
        assert home_text == txtHome
        homePage.btnSingUpLoginMethod().click()
        txtLogin = loginPage.txtLoginMethod().text
        assert login_text == txtLogin
        loginPage.inputEmailLogginMethod().send_keys("netdisonn+star10@gmail.com")
        loginPage.inputPasswordLogginMethod().send_keys("123456")
        loginPage.btnLoginMethod().click()
        txtLogged = homePage.txtLoggedMethod().text
        assert logged_text == txtLogged
        homePage.btnLogoutMethod().click()
        txtLogin = loginPage.txtLoginMethod().text
        assert login_text == txtLogin

    def test_cases_5_Register_User_with_existing_email(self):
        pass





