import time
import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

# -------------------------------------------------------------------
# ❌ FLAKY APPROACH (Sleeps + Hardcoded Delays = High Failure Rate in CI)
# -------------------------------------------------------------------
def test_flaky_login_approach(driver):
    """
    Demonstrates why hard sleeps cause flaky test failures in CI pipelines.
    """
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)  # ❌ Anti-pattern: Hard sleep fails if CI server is under load

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(1)  # ❌ Brittle sleep
    assert "You logged into a secure area!" in driver.page_source


# -------------------------------------------------------------------
# ✅ FIXED APPROACH (Explicit Waits + POM + Dynamic Retries)
# -------------------------------------------------------------------
@pytest.mark.flaky(reruns=2, reruns_delay=1)  # ✅ Automatic retries for network-dependent runs
def test_robust_login_approach(driver):
    """
    Demonstrates 100% reliable test execution using Explicit Waits & POM.
    """
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)

    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_submit()

    # Dynamic verification with Explicit Wait
    success_msg = login_page.get_success_message()
    assert "You logged into a secure area!" in success_msg
