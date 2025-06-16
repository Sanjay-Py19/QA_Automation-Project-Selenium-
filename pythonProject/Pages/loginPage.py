from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    user_name = "username"
    pass_word = "password"
    login_button = "//*[@class='button' and @value='Log In']"

    def userName(self, username_text):
        self.driver.find_element(By.NAME, self.user_name).send_keys(username_text)

    def passWord(self, password_text):
        self.driver.find_element(By.NAME, self.pass_word).send_keys(password_text)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button).click()
