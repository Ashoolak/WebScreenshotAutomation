import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# List of websites to visit
websites = [
    # List of websites
]

# Set up headless Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1280x1024')
chrome_driver_path = '/Users/user_name/Desktop/chromedriver'  # Replace with the path to your downloaded ChromeDriver

# Create output directory for screenshots
output_dir = 'screenshots'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Visit each website and take a screenshot of their cookies
for index, url in enumerate(websites):
    try:
        driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
        driver.get(url)

        # Give time for the cookies notification to appear
        time.sleep(5)

        # Take a screenshot and save it
        screenshot_path = os.path.join(output_dir, f'screenshot_{index}.png')
        driver.save_screenshot(screenshot_path)
        print(f'Screenshot saved for {url} at {screenshot_path}')
    except Exception as e:
        print(f'Error capturing screenshot for {url}: {str(e)}')
    finally:
        driver.quit()

print('Process completed.')
