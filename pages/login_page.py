from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Page Object Model (POM) implementation for maintaining test locators
    and eliminating flaky DOM interactions with explicit waits.
    """
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Locators (Prefer data-testid or ID over volatile XPaths)
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "flash.success")

    def enter_username(self, username):
        element = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        element = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        element.clear()
        element.send_keys(password)

    def click_submit(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        element.click()

    def get_success_message(self):
        element = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        return element.text
