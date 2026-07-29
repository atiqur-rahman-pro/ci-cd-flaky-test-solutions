# 🛠️ CI/CD Flaky Selenium Test Mitigation Guide & Reference Implementation

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.18+-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

A practical reference implementation demonstrating how to eliminate **flaky Selenium test failures in CI/CD pipelines** (Jenkins, GitHub Actions, GitLab CI) using **Explicit Waits**, **Page Object Model (POM)**, **Docker containerization**, and **Pytest retry mechanisms**.

---

## 🎯 4 Proven Strategies Implemented in this Repo

| # | Flakiness Root Cause | Anti-Pattern (Flaky) | Best Practice (Robust Solution) |
| :--- | :--- | :--- | :--- |
| 1 | **Timing & Synchronisation** | `time.sleep(5)` | `WebDriverWait(driver, 10).until(EC.element_to_be_clickable(...))` |
| 2 | **Environment Mismatches** | Local machine vs CI OS differences | **Docker Containerization** (Headless Chrome in Linux container) |
| 3 | **Unstable Network / APIs** | Single failure marks build RED | `@pytest.mark.flaky(reruns=2, reruns_delay=1)` |
| 4 | **Brittle Locators** | Long XPaths `/html/body/div[3]/form/button` | Page Object Model with `data-testid` attributes |

---

## 🧪 Code Comparison

### ❌ Anti-Pattern: Flaky Test (`tests/test_flaky_vs_fixed.py`)
```python
def test_flaky_approach(driver):
    driver.get("https://example.com/login")
    time.sleep(2)  # ❌ Fails if CI server CPU is under heavy load
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(1)  # ❌ Brittle delay
    assert "Success" in driver.page_source
```

### ✅ Best Practice: Robust Test (`pages/login_page.py`)
```python
@pytest.mark.flaky(reruns=2, reruns_delay=1)  # ✅ Retries unstable network calls
def test_robust_approach(driver):
    driver.get("https://example.com/login")
    login_page = LoginPage(driver)  # ✅ Page Object Model
    login_page.enter_username("tomsmith")  # ✅ Explicit Wait
    login_page.click_submit()
    assert "Success" in login_page.get_success_message()
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/atiqur-rahman-pro/ci-cd-flaky-test-solutions.git
cd ci-cd-flaky-test-solutions

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Pytest suite with automatic retries
pytest tests/ --reruns 2
```

---

## 🐳 Running with Docker

```bash
# Build & run tests inside container
docker build -t flaky-test-solutions .
docker run --rm flaky-test-solutions
```

---

## 👤 Author Identity & Connect

<div align="center">

### **Designed & Developed by Atiqur Rahman**
*Senior Software QA & Test Automation Specialist*

[![Microsoft Playwright](https://img.shields.io/badge/MICROSOFT_PLAYWRIGHT-OPEN_SOURCE_CONTRIBUTOR-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)](https://github.com/microsoft/playwright-python/pull/3157)
[![YouTube](https://img.shields.io/badge/YOUTUBE-SUBSCRIBE_NOW-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@Digital_Digest_Live)  
[![GitHub](https://img.shields.io/badge/GITHUB-ATIQUR--RAHMAN--PRO-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/atiqur-rahman-pro)
[![LinkedIn](https://img.shields.io/badge/LINKEDIN-CONNECT_ME-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/atiqur-rahman-pro)

</div>
