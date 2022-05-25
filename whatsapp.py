import requests
from cleverdict import CleverDict
from config import CONTACTS, URL, HEADERS, TEST_MESSAGE, TEST_URL


class Whatsapp:

    def __init__(self, content="", contact="", autosend=True, **kwargs):
        content_type = kwargs.get("type")
        self.data = CleverDict({
            "messaging_product": "whatsapp",
            "to": contact or CONTACTS[0],
            "type": content_type or "text",
        })
        if not content_type:
            self.data.text = {
                "preview_url": True,
                "body": content or TEST_MESSAGE + TEST_URL,
            }
        self.data.update(kwargs)
        if autosend:
            self.send()

    def send(self):
        self.response = requests.post(URL, headers=HEADERS, json=self.data)
