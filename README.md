# Android Appium Network Toggle Tests

A Python-based mobile automation testing framework built with Pytest and Appium to validate Android device behavior during WiFi and Mobile Data state transitions.

---

## Overview

This project provides an automated testing setup to simulate network interruptions and restorations on Android devices. It uses Appium with the UiAutomator2 driver and integrates ADB commands within test execution to control system-level network states.

The framework is structured using Pytest fixtures for driver management and supports HTML test reporting.

---

## Key Features

- Appium-based Android automation
- Pytest testing framework
- UiAutomator2 driver integration
- ADB command execution within tests
- Network toggle simulation (WiFi and Mobile Data)
- HTML report generation
- Structured and reusable driver setup

---

## Technology Stack

- Python 3.x
- Pytest
- Appium Python Client
- Android SDK
- ADB (Android Debug Bridge)
- UiAutomator2
- Android Emulator or Physical Device

---

## Project Structure

AppiumTest/
│
├── conftest.py
├── test_data_load.py
├── report.html
├── assets/
│   └── style.css
└── .pytest_cache/

### File Descriptions

conftest.py  
Contains the Pytest fixture responsible for initializing and quitting the Appium driver.

test_data_load.py  
Contains the test case that toggles network states and validates application behavior.

report.html  
Generated HTML test execution report.

assets/style.css  
Styling file for HTML report formatting.

---

## Prerequisites

Ensure the following are installed:

- Python
- Node.js
- Appium Server
- Android SDK
- ADB configured in system PATH
- Android Emulator running or physical device connected

Verify installations:

python --version
adb devices
appium --version

---

## Installation

1. Clone the repository:

git clone <repository-url>
cd android-appium-network-toggle-tests

2. Install required Python packages:

pip install pytest
pip install Appium-Python-Client
pip install pytest-html

3. Start the Appium server:

appium

---

## Configuration

The automation framework uses the following default configuration:

- Platform Name: Android
- Automation Name: UiAutomator2
- App Package: com.android.settings
- App Activity: com.android.settings.Settings
- Appium Server URL: http://127.0.0.1:4723

Ensure the emulator or device is active before running tests.

---

## Running Tests

Run all tests:

pytest

Run tests with HTML report generation:

pytest --html=report.html

---

## Test Scenario

Network Toggle Validation

The test performs the following steps:

1. Launch the Android Settings application.
2. Disable WiFi using ADB.
3. Disable Mobile Data using ADB.
4. Re-enable WiFi.
5. Re-enable Mobile Data.
6. Validate that the Settings app remains active.

The test ensures that the application remains stable during network transitions.

---

## How It Works

- The Pytest fixture in conftest.py initializes the Appium driver.
- The test case in test_data_load.py executes ADB shell commands via Python’s subprocess module.
- After toggling network states, the current package is validated to confirm application stability.
- The driver session is properly terminated after test execution.

---

## Use Cases

- Network resilience validation
- Android system automation testing
- Infrastructure behavior testing
- Appium framework reference implementation
- Device-level automation validation

---

## Future Improvements

- Multi-device configuration support
- Parameterized environment handling
- Logging framework integration
- Screenshot capture on failure
- CI/CD pipeline integration
- Enhanced reporting and analytics

---

## License

This project is intended for automation learning and internal testing purposes.
