import requests
from cleverdict import CleverDict
from config import CONTACTS, URL, HEADERS, TEST_MESSAGE, TEST_URL


class Whatsapp:

    def __init__(self, content="", contact="", content_type="", autosend=True, **kwargs):
        """
        Prepare and optionally execute a request to the Whatsapp Cloud API for sending a message to a pre-approved or opted-in) Whatsapp contact.

        Default: immediately send a text message with url preview enabled.

        Arguments
        ---------
        content (str):
            body of text message, or media id/link if audio/video/image/document
        contact (str):
            numeric phone number starting with country code; no "+" or leading 0
        content_type (str):
            text|video|audio|image|template|location|list|document
        autosend (bool):
            True: Send message immediately.
            False: Create but do not send (for testing or scheduled sending etc)
        """
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

    def template(self, template_name="", language=""):
        kwargs = {"type": "template",
                  "template": {"name": template_name or "hello_world",
                     "language": {"code": language or "un_US"}},}

"""
                       "location": {
                "latitude": lat,
                "longitude": long,
                "name": name,
                "address": address,
            },
                      "image": {"id": image, "caption": caption},
                      "image": {"link": image, "caption": caption},
                   "video": {"link": video, "caption": caption},
                 "video": {"id": video, "caption": caption},
                 "document": {"link": document, "caption": caption},
                 "document": {"id": document, "caption": caption},
"""
