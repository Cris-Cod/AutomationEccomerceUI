from selenium.webdriver.common.by import By


class Products:
    def __init__(self, driver):
        self.driver = driver

    txtAllProducts = (By.XPATH, "//div[@class='features_items']/h2")
    products = (By.XPATH, "//div[@class='product-image-wrapper']")
    btnViewProduct = (By.XPATH, "//div[@class='product-image-wrapper']/div[2]/ul/li/a")
    nameProduct = (By.XPATH, "//div[@class='product-information']/h2")
    categoryProduct = (By.XPATH, "//div[@class='product-information']/p[1]")
    priceProduct = (By.XPATH, "//div[@class='product-information']/span/span[1]")
    availabilityProduct = (By.XPATH, "//div[@class='product-information']/p[2]")
    conditionProduct = (By.XPATH, "//div[@class='product-information']/p[3]")
    brandProduct = (By.XPATH, "//div[@class='product-information']/p[4]")
    inputSearch = (By.ID, "search_product")
    btnSearch = (By.ID, "submit_search")
    txtSearchedP = (By.XPATH, "//div[@class='features_items']/h2")
    txtMainProduct = (By.XPATH, "//div[@class='product-image-wrapper']/div/div/p")

    def txtAllProductsMethod(self):
        return self.driver.find_element(*Products.txtAllProducts)

    def productsMethod(self):
        return self.driver.find_elements(*Products.products)

    def btnViewProductMethod(self):
        return self.driver.find_element(*Products.btnViewProduct)

    def nameProductMethod(self):
        return self.driver.find_element(*Products.nameProduct)

    def categoryProductMethod(self):
        return self.driver.find_element(*Products.categoryProduct)

    def priceProductMethod(self):
        return self.driver.find_element(*Products.priceProduct)

    def availabilityProductMethod(self):
        return self.driver.find_element(*Products.availabilityProduct)

    def conditionProductMethod(self):
        return self.driver.find_element(*Products.conditionProduct)

    def brandProductMethod(self):
        return self.driver.find_element(*Products.brandProduct)

    def inputSearchMethod(self):
        return self.driver.find_element(*Products.inputSearch)

    def btnSearchMethod(self):
        return self.driver.find_element(*Products.btnSearch)

    def txtSearchedPMethod(self):
        return self.driver.find_element(*Products.txtSearchedP)

    def txtMainProductMethod(self):
        return self.driver.find_element(*Products.txtMainProduct)