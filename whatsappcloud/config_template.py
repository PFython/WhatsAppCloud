"""
Rename this file to config.py once completed.
Add config.py to .gitignore etc before including in Github or other repository.
"""

PHONE_ID = "111111111111111"  # 15 digit numerical string
CONTACTS = [
    "447919xxxxxx",  # Up to five contact numbers
    "447940xxxxxx",  # Numerical strings starting with country code
    "44208xxxxxxx",  # No leading 0 between country code and area code
    "xxxxxxxxxxxx",
    "xxxxxxxxxxxx",
]
TOKEN = "x...x"  # 200+ alphanumeric character string

# TOKEN expires every 24 hours with Test Business Account.
# You can update config.py manually or automate/scrape using:

"""
import webbrowser

APP_ID = "111111111111111"  # 15 digit numerical string from Meta App Dashboard
APP_URL = f"https://developers.facebook.com/apps/{APP_ID}/dashboard/"
webbrowser.open(APP_URL)
"""

ENDPOINT = f"https://graph.facebook.com/v13.0/{PHONE_ID}/messages"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}
TEST_MESSAGE = "*TEST* _*TEST*_ TEST _TEST_\n"
TEST_URL = "https://twitter.com/AWSOM_solutions"
