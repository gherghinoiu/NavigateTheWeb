# app/main.py
from app.scraper.navigator import WebsiteNavigator
from app.utils.config import PNRR_EMAIL, PNRR_PASSWORD

def run_extraction():
    """
    The main function to orchestrate the web scraping and data processing workflow.
    """
    print("Starting the extraction process...")

    # Initialize the navigator with credentials from our config
    navigator = WebsiteNavigator(email=PNRR_EMAIL, password=PNRR_PASSWORD)

    try:
        # Attempt to log in
        login_successful = navigator.login()

        if login_successful:
            print("Login was successful. Proceeding to next steps (to be implemented)...")
            # Here is where we will later add the logic to:
            # 1. Navigate to the documents section.
            # 2. Extract document links and information.
            # 3. Download files.
            # 4. Pass them to the processing module.
        else:
            print("Login failed. Please check your credentials or the website structure.")

    finally:
        # It's crucial to always close the browser to free up resources.
        navigator.close()

if __name__ == "__main__":
    run_extraction()