from pageObjectModel.AccountInformation import AccountInformation
from pageObjectModel.HomePage import HomePage
from pageObjectModel.Login import Login
from pageObjectModel.ContactUs import ContactUs
from pageObjectModel.TestCasesPage import TestCasesPage
from pageObjectModel.Products import Products
from utilities.BaseClass import BaseClass
import pytest


class TestCases(BaseClass):
    home_text = "FEATURES ITEMS"
    singUp_text = "New User Signup!"
    account_text = "ENTER ACCOUNT INFORMATION"
    account_created = "ACCOUNT CREATED!"
    logged_text = "Logged in as Mathew Perry"
    account_deleted_text = "Account Deleted!"
    login_text = "Login to your account"
    incorrect_text = "Your email or password is incorrect!"
    login_sinUp_incorrect_text = "Email Address already exist!"
    title_ContactUs_text = "Get In Touch"
    contactUs_succes_txt = "Success! Your details have been submitted successfully."
    test_cases_text = "Test Cases"
    all_products_text = "All Products"



    def test_cases_1_Register_User(self):
        homePage = HomePage(self.driver)
        loginPage = Login(self.driver)
        accountInformation = AccountInformation(self.driver)


        txtHome = homePage.textHomeMethod().text
        assert TestCases.home_text == txtHome
        homePage.btnSingUpLoginMethod().click()
        txtSingUp = loginPage.txtSingUpMethod().text
        assert TestCases.singUp_text == txtSingUp
        loginPage.inputNameMethod().send_keys("Mathew Perry")
        loginPage.inputEmailMethod().send_keys("netdisonn+star7@gmail.com")
        loginPage.btnSingUpMethod().click()
        txtAccount = accountInformation.txtAccountInformationMethod().text
        assert TestCases.account_text == txtAccount
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
        assert TestCases.account_created == txtAccountCreated
        accountInformation.btnContinueMethod().click()
        txtLogged = homePage.txtLoggedMethod().text
        assert TestCases.logged_text == txtLogged
        homePage.btnDeleteAccountMethod().click()
        txt_account_deleted = homePage.txtAccountDeletedMethod().text
        assert TestCases.account_deleted_text == txt_account_deleted.title()
        homePage.btnDeleteAccountContinueMethod().click()

    def test_cases_2_LoginUserWithCorrectEmailAndPassword(self):


        homePage = HomePage(self.driver)
        loginPage = Login(self.driver)

        txtHome = homePage.textHomeMethod().text
        assert TestCases.home_text == txtHome
        homePage.btnSingUpLoginMethod().click()
        txtLogin = loginPage.txtLoginMethod().text
        assert TestCases.login_text == txtLogin
        loginPage.inputEmailLogginMethod().send_keys("netdisonn+star10@gmail.com")
        loginPage.inputPasswordLogginMethod().send_keys("123456")
        loginPage.btnLoginMethod().click()
        txtLogged = homePage.txtLoggedMethod().text
        assert TestCases.logged_text == txtLogged

    def test_cases_3_LoginUserWithIncorrectEmailAndPassword(self):



        homePage = HomePage(self.driver)
        loginPage = Login(self.driver)

        txtHome = homePage.textHomeMethod().text
        assert TestCases.home_text == txtHome
        homePage.btnSingUpLoginMethod().click()
        txtLogin = loginPage.txtLoginMethod().text
        assert TestCases.login_text == txtLogin
        loginPage.inputEmailLogginMethod().send_keys("netdisonnstar10@gmail.com")
        loginPage.inputPasswordLogginMethod().send_keys("12345")
        loginPage.btnLoginMethod().click()
        textIncorrect = loginPage.txtIncorrectMethod().text
        assert TestCases.incorrect_text == textIncorrect

    def test_cases_4_Logout_User(self):


        homePage = HomePage(self.driver)
        loginPage = Login(self.driver)

        txtHome = homePage.textHomeMethod().text
        assert TestCases.home_text == txtHome
        homePage.btnSingUpLoginMethod().click()
        txtLogin = loginPage.txtLoginMethod().text
        assert TestCases.login_text == txtLogin
        loginPage.inputEmailLogginMethod().send_keys("netdisonn+star10@gmail.com")
        loginPage.inputPasswordLogginMethod().send_keys("123456")
        loginPage.btnLoginMethod().click()
        txtLogged = homePage.txtLoggedMethod().text
        assert TestCases.logged_text == txtLogged
        homePage.btnLogoutMethod().click()
        txtLogin = loginPage.txtLoginMethod().text
        assert TestCases.login_text == txtLogin

    def test_cases_5_Register_User_with_existing_email(self):
        homePage = HomePage(self.driver)
        loginPage = Login(self.driver)

        txtHome = homePage.textHomeMethod().text
        assert TestCases.home_text == txtHome
        homePage.btnSingUpLoginMethod().click()
        txtSingUp = loginPage.txtSingUpMethod().text
        assert TestCases.singUp_text == txtSingUp
        loginPage.inputNameMethod().send_keys("Don Selenium Python")
        loginPage.inputEmailMethod().send_keys("seleniump@gmail.com")
        loginPage.btnSingUpMethod().click()
        txtSingUpIncorrect = loginPage.txtSingUpIncorrectMethod().text
        assert TestCases.login_sinUp_incorrect_text == txtSingUpIncorrect

    def test_cases_6_Contact_Us_Form(self):
        homePage = HomePage(self.driver)
        contactUs = ContactUs(self.driver)

        txtHome = homePage.textHomeMethod().text
        assert TestCases.home_text == txtHome
        homePage.btnContactUsMethod().click()
        txtTitleContactUs = contactUs.txtTitleContactUsMethod().text
        assert TestCases.title_ContactUs_text.upper() == txtTitleContactUs
        contactUs.inputNameMethod().send_keys("Mathew")
        contactUs.inputEmailMethod().send_keys("netdisonn+star10@gmail.com")
        contactUs.inputSubjectMethod().send_keys("Send me a message")
        contactUs.textAreaMethod().send_keys("YAML es un acrónimo recursivo que significa YAML Ain't Markup Language (en castellano, ‘YAML no es un lenguaje de marcado’).1​ A comienzos de su desarrollo, YAML significaba Yet Another Markup Language (otro lenguaje de marcado más) para distinguir su propósito centrado en los datos en lugar del marcado de documentos. Sin embargo, dado que se usa frecuentemente XML para serializar datos y XML es un auténtico lenguaje de marcado de documentos, es razonable considerar YAML como un lenguaje de marcado ligero.")
        contactUs.btnUploadMethod().send_keys("C:\\Users\\USER\\Pictures\\Screenshots\\testing.JPG")
        contactUs.btnSubmitMethod().click()
        self.acceptAlert()
        textSucces = contactUs.txtSuccesMethod().text
        assert TestCases.contactUs_succes_txt == textSucces
        contactUs.btnHomeMethod().click()
        txtHome = homePage.textHomeMethod().text
        assert TestCases.home_text == txtHome

    def test_cases_7_Verify_Test_Cases_Page(self):
        homePage = HomePage(self.driver)
        testCasesPage = TestCasesPage(self.driver)

        txtHome = homePage.textHomeMethod().text
        assert TestCases.home_text == txtHome
        homePage.btnTestCasesMethod().click()
        txtTestcases = testCasesPage.txtTestCasesMethod().text
        assert self.test_cases_text == txtTestcases.title()

    def test_Cases_8_Verify_All_Products_and_product_detail_page(self):
        homePage = HomePage(self.driver)
        products = Products(self.driver)

        txtHome = homePage.textHomeMethod().text
        assert TestCases.home_text == txtHome
        homePage.btnProductsMethod().click()
        txtAll_products = products.txtAllProductsMethod().text
        assert self.all_products_text.upper() == txtAll_products
        stock = products.productsMethod()

        for product in stock:
            if product == stock[0]:
                self.scroll()
                products.btnViewProductMethod().click()

        products.nameProductMethod().is_displayed()
        products.categoryProductMethod().is_displayed()
        products.priceProductMethod().is_displayed()
        products.availabilityProductMethod().is_displayed()
        products.conditionProductMethod().is_displayed()
        products.brandProductMethod().is_displayed()

        name = products.nameProductMethod().text
        print(f"Product: {name}")
        category = products.categoryProductMethod().text
        print(category)
        price = products.priceProductMethod().text
        print(f"Price: {price}")
        availability = products.availabilityProductMethod().text
        print(availability)
        condition = products.conditionProductMethod().text
        print(condition)
        brand = products.brandProductMethod().text
        print(brand)

