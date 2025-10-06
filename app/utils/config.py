# app/utils/config.py
import os
from dotenv import load_dotenv

# Load environment variables from the .env file in the project root
# The path is constructed to go up one level from the utils directory to the app directory,
# and then one more level up to the project root where .env is located.
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Fetching credentials from environment variables
PNRR_EMAIL = os.getenv("PNRR_EMAIL")
PNRR_PASSWORD = os.getenv("PNRR_PASSWORD")

# Quick check to ensure variables are loaded. If not, the program will exit.
if not PNRR_EMAIL or not PNRR_PASSWORD:
    raise ValueError("PNRR_EMAIL and PNRR_PASSWORD must be set in the .env file.")