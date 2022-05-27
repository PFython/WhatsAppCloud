PHONE_ID = "111363561583451"
CONTACTS = ["447919882422", "447940225066"]

TOKEN = "EAAFYodZAyoM8BAHZCHfQNhugcUlt0GsxrnRi3p2rMMfmepr2morHdzOPu8injFEb2jpJPp7wki3ZBJ4XZBhK4BJ8VYHmwj7yz6eGhwNJ9wFgap53JsWWrCOO5cT7DWsHzP7jsvVqm0tw9JGgPXMLAVBObdF6cH5BpLcLmRTegDPmt78njgPcQBpJ7I4SOaF11wPW1vdhywZDZD"

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
