from selenium.webdriver.common.by import By


class ContactUs:

    def __init__(self, driver):
        self.driver = driver

    txtTitleContactUs = (By.XPATH,"//div[@class='contact-form']/h2")
    inputName = (By.CSS_SELECTOR, "input[data-qa='name']")
    inputEmail = (By.CSS_SELECTOR, "input[data-qa='email']")
    inputSubject = (By.CSS_SELECTOR, "input[data-qa='subject']")
    textArea = (By.ID, "message")
    btnUpload = (By.CSS_SELECTOR,"input[name='upload_file']")
    btnSubmit = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    txtSucces = (By.XPATH, "//div[@class='status alert alert-success']")
    btnHome = (By.XPATH, "//a[@class='btn btn-success']")

    def txtTitleContactUsMethod(self):
        return self.driver.find_element(*ContactUs.txtTitleContactUs)

    def inputNameMethod(self):
        return self.driver.find_element(*ContactUs.inputName)

    def inputEmailMethod(self):
        return self.driver.find_element(*ContactUs.inputEmail)

    def inputSubjectMethod(self):
        return self.driver.find_element(*ContactUs.inputSubject)

    def textAreaMethod(self):
        return self.driver.find_element(*ContactUs.textArea)

    def btnUploadMethod(self):
        return self.driver.find_element(*ContactUs.btnUpload)

    def btnSubmitMethod(self):
        return self.driver.find_element(*ContactUs.btnSubmit)

    def txtSuccesMethod(self):
        return self.driver.find_element(*ContactUs.txtSucces)

    def btnHomeMethod(self):
        return self.driver.find_element(*ContactUs.btnHome)