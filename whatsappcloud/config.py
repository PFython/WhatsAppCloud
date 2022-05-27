PHONE_ID = "111363561583451"
CONTACTS = ["447919882422", "447940225066"]

TOKEN = "EAAFYodZAyoM8BAIAwolTe8VZCGwZC4nEZBxHMCE1CefLXo9qUnJHJZAKbdJ9xTNjbSlblRflQ1yH0adoy8UpowsZCaYJnN5I97ZCjtblLzvwLuOzWZBQf8pjZC5ZCJ1x7uQPrZAra0lP5z4UtZCZCn2W6CxhZBYyFmxTH2agu6Iax0BZCAObyaUYmgBZBjDTWMTHGWszm5OJOBKPkZB82DQZDZD"

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
