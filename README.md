# Automation Test - UI Testing

This repository contains automation scripts and results for UI testing of a website across various browsers and screen resolutions. 

## Objective

The goal is to test and verify that a website is rendering correctly on different screen resolutions and browsers. This includes capturing full-page screenshots and creating a video of the test in running mode.

## Setup

### Prerequisites

- Python 3.x
- Selenium WebDriver
- ChromeDriver
- GeckoDriver for Firefox
- A video recording tool (optional for recording the test)

### Resolutions & Devices

The following devices and resolutions are to be tested:

**Desktop -** 

- 1920×1080
- 1366×768
- 1536×864

**Mobile -** 

- 360×640
- 414×896
- 375×667

## Browsers to be Tested

- **Chrome** (Windows OS)
- **Firefox** (Windows OS)
- **Safari** (MAC OS only)

## Instructions

### 1. Cloning the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/hemanth1223/automation_of_resolution_testing-UI_testing.git

### 2. Setting Up the Environment
Navigate to the project directory and install the required Python packages:
```bash
cd automation_of_resolution_testing-UI_testing
pip install -r requirements.txt

### 3. Running the Tests
1. For Chrome and Firefox on Windows OS:
Ensure you have the appropriate WebDrivers (ChromeDriver and GeckoDriver) installed.
Update the paths to the WebDrivers in the script if necessary.
Run the test script to capture screenshots and validate the pages:
```bash
python test_script.py

2. For Safari on MAC OS:
Follow similar steps using a MAC OS environment.

4. Validation
1. Screenshots
The screenshots are saved in a folder structure as follows:

screenshots/
  └── Chrome/
      └── 1920x1080/
          └── screenshot-date-time.png
      └── 1366x768/
          └── screenshot-date-time.png
      └── 1536x864/
          └── screenshot-date-time.png
  └── Firefox/
      └── 1920x1080/
          └── screenshot-date-time.png
      └── 1366x768/
          └── screenshot-date-time.png
      └── 1536x864/
          └── screenshot-date-time.png

2. Video
A video of the test in running mode should be recorded (optional).

3. Script Validation
Use the provided validation script to check if all required screenshots are captured.

Notes
- Chrome does not have built-in or additional features to capture full-page screenshots. It can only capture the visible screen area.
- Firefox has built-in functionality to capture full-page screenshots.
- For Safari testing, please use a MAC OS environment and follow similar steps to those used for Chrome and Firefox.

Troubleshooting
- Ensure that all WebDriver executables are in your system's PATH or provide absolute paths in the script.
- For any issues, check the documentation or raise an issue in the repository.
