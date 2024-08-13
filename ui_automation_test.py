from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time
import os

firefox_options = FirefoxOptions()
firefox_options.binary_location = r"C:\\Program Files\\Mozilla Firefox\\firefox.exe"

resolutions = {
    "Desktop": [(1920, 1080), (1366, 768), (1536, 864)],
    "Mobile": [(360, 640), (414, 896), (375, 667)]
}

browsers = {
    "Chrome": webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
    "Firefox": webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options),
}

# Manually specified pages
pages = [
    "https://www.getcalley.com/",
    "https://www.getcalley.com/calley-lifetime-offer/",
    "https://www.getcalley.com/see-a-demo/",
    "https://www.getcalley.com/calley-teams-features/",
    "https://www.getcalley.com/calley-pro-features/"
]

def capture_screenshots(driver, url, browser_name, resolution):
    print(f"Capturing screenshot for {url} on {browser_name} at {resolution}")
    width, height = resolution
    driver.set_window_size(width, height)
    driver.get(url)
    print(f"Accessing URL: {url}")
    time.sleep(2)  

    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(width, total_height) 
    
    folder_path = f"./screenshots/{browser_name}/{width}x{height}/"
    print(f"Saving screenshots to: {folder_path}")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")
    
    screenshot_path = f"{folder_path}screenshot-{time.strftime('%Y%m%d-%H%M%S')}.png"
    try:
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
    except Exception as e:
        print(f"Failed to save screenshot: {e}")

print("Starting UI Automation Test")

# No need to fetch sitemap since URLs are manually specified
print(f"Pages to capture: {pages}")

for browser_name, driver in browsers.items():
    try:
        print(f"Launching {browser_name} browser")
        for page in pages:
            print(f"Accessing page: {page}")
            for device, resolution_list in resolutions.items():
                for resolution in resolution_list:
                    print(f"Capturing {device} screenshot at resolution {resolution} on {browser_name}")
                    capture_screenshots(driver, page, browser_name, resolution)
    finally:
        print(f"Quitting {browser_name} browser")
        driver.quit()

print("UI Automation Test Completed")

def validate_screenshots(browser_name, resolutions):
    base_dir = f"./screenshots/{browser_name}/"
    missing_screenshots = []

    for resolution in resolutions:
        resolution_dir = os.path.join(base_dir, f"{resolution[0]}x{resolution[1]}/")
        if not os.path.exists(resolution_dir):
            missing_screenshots.append(f"Missing directory: {resolution_dir}")
            continue
        
        screenshots = [f for f in os.listdir(resolution_dir) if f.endswith('.png')]
        if len(screenshots) == 0:
            missing_screenshots.append(f"No screenshots found in: {resolution_dir}")

    if missing_screenshots:
        print("Validation failed with the following issues:")
        for issue in missing_screenshots:
            print(issue)
    else:
        print(f"All screenshots are present for {browser_name}.")

resolutions_list = [(1920, 1080), (1366, 768), (1536, 864), (360, 640), (414, 896), (375, 667)]  
validate_screenshots("Chrome", resolutions_list)
validate_screenshots("Firefox", resolutions_list)