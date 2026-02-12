from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Android Emulator"
options.automation_name = "UiAutomator2"
options.browser_name = "Chrome"
options.chromedriver_executable = "C:/Android/chromedriver/chromedriver.exe"
options.set_capability(
    "goog:chromeOptions",
    {
        "args": [
            "--no-first-run",
            "--no-default-browser-check",
            "--disable-fre",
            "--disable-notifications",
            "--disable-infobars"
        ]
    }
)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

driver.get("https://example.com")

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

driver.quit()