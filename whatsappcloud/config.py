PHONE_ID = "111363561583451"
CONTACTS = ["447919882422", "447940225066"]

TOKEN = "EAAFYodZAyoM8BANZBAgNRmvCJOUySvEZAUrhSyowZC20wmcfP2aW4CPhaUivN1H8DOw2AeZBaGZCUapURVslTGccUiX85VHJmvSPrTdCo91j1xnWMRMBjvP2gmP9IHcLYaqoyqyBlzDcZAWPVvUXBhE1qRKwxRPJ0A8DKhAkPPe0G7iZC2is6XjgOHrI0tXZCPMEihCZCrdY9uXAZDZD"

# TOKEN expires every 24 hours with Test Business Account.
# You can update config.py manually or automate scrape/using:

"""
import webbrowser

APP_ID = "378927087526095"  # 15 digit numerical string from Meta App Dashboard
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
