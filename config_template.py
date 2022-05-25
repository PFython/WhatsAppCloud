"""
Rename this file to config.py once complete.
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
                 # Check expiry!
URL = f"https://graph.facebook.com/v13.0/{PHONE_ID}/messages"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}
TEST_MESSAGE = "*TEST* _*TEST*_ TEST _TEST_\n"
TEST_URL = "https://twitter.com/AWSOM_solutions"
