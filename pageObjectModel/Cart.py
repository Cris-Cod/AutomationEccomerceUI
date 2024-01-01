from selenium.webdriver.common.by import By


class Cart:
    def __init__(self, driver):
        self.driver = driver

    txtSubscription = (By.XPATH,"//div[@class='footer-widget']/div/div/div[2]/div/h2")
    inputSubscription = (By.ID, "susbscribe_email")
    btnSubscribe = (By.ID, "subscribe")
    txtSuccess = (By.XPATH, "//div[@class='alert-success alert']")

    def txtSubscriptionMethod(self):
        return self.driver.find_element(*Cart.txtSubscription)

    def inputSubscriptionMethod(self):
        return self.driver.find_element(*Cart.inputSubscription)

    def btnSubscribeMethod(self):
        return self.driver.find_element(*Cart.btnSubscribe)

    def txtSuccessMethod(self):
        return self.driver.find_element(*Cart.txtSuccess)