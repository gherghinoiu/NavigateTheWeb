# app/scraper/navigator.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# A class to encapsulate all browser navigation actions
class WebsiteNavigator:
    """
    Manages the Selenium WebDriver and browser interactions.
    """
    def __init__(self, email, password):
        """
        Initializes the navigator with user credentials and sets up the WebDriver.
        """
        self.email = email
        self.password = password
        # Set up Chrome options for running in a headless environment like Codespaces
        options = webdriver.ChromeOptions()
        options.add_argument("--headless") # Run in headless mode (no UI)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080") # Set a window size

        # Use webdriver_manager to automatically install and manage the Chrome driver
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        print("WebDriver initialized.")

    def login(self):
        """
        Navigates to the login page and performs the login action.
        """
        login_url = "https://coordonare.pnrr.gov.ro/auth/login"
        print(f"Navigating to {login_url}...")
        self.driver.get(login_url)

        try:
            # We use WebDriverWait to ensure the page elements are loaded before we try to interact with them.
            # This makes our script more robust against slow page loads.
            wait = WebDriverWait(self.driver, 10) # Wait for a maximum of 10 seconds

            print("Locating username and password fields...")
            # Find the username field by its ID and enter the email
            username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_field.send_keys(self.email)

            # Find the password field by its ID and enter the password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(self.password)

            print("Locating login button...")
            # The button doesn't have a unique ID, so we use a more complex CSS selector.
            # This selector looks for a button that contains the text 'Autentificare'.
            login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

            print("Clicking login button...")
            login_button.click()

            # A simple way to check for successful login is to wait for the URL to change
            # or for an element on the dashboard page to appear.
            # Let's wait for the URL to change from '/auth/login'.
            wait.until(EC.not_(EC.url_contains('/auth/login')))

            print("Login successful! Current URL:", self.driver.current_url)
            # You can add a screenshot to verify it works, especially in headless mode
            self.driver.save_screenshot("successful_login.png")
            print("Screenshot 'successful_login.png' saved.")

        except Exception as e:
            print(f"An error occurred during login: {e}")
            self.driver.save_screenshot("login_error.png")
            print("Screenshot 'login_error.png' saved for debugging.")
            return False

        return True

    def close(self):
        """
        Closes the browser and quits the driver.
        """
        if self.driver:
            print("Closing the browser.")
            self.driver.quit()