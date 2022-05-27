import requests
from cleverdict import CleverDict

from config import CONTACTS, ENDPOINT, HEADERS, TEST_MESSAGE, TEST_URL


class Whatsapp:
    def __init__(self, contact="", content_type="", autosend=True, **kwargs):
        """
        Prepare and optionally execute a request to the Whatsapp Cloud API for sending a message to a pre-approved or opted-in) Whatsapp contact.

        Default: immediately send a text message with url preview enabled.

        Arguments
        ---------
        contact (str):
            recipient phone number starting with country code; no + or leading 0
        content_type (str):
            text[default]|audio|contacts|document|image
            template|video|sticker|location|interactive
        autosend (bool):
            True: Send message immediately.
            False: Create but do not send (for testing or scheduled sending etc)
        """
        self.data = CleverDict(
            {
                "messaging_product": "whatsapp",
                "to": contact or CONTACTS[0],
                "type": content_type or "text",
            }
        )
        if not content_type or content_type == "text":
            # Create default test message
            self.data.text = CleverDict(
                {
                    "preview_url": kwargs.get("preview_url")
                    if "preview_url" in kwargs
                    else True,
                    "body": kwargs.get("body") or TEST_MESSAGE + TEST_URL,
                }
            )
        else:
            self.data[content_type] = CleverDict(kwargs)
        if autosend:
            self.send()

    def send(self):
        self.response = requests.post(ENDPOINT, headers=HEADERS, json=self.data)

    @staticmethod
    def text(body="", contact="", preview_url=True, autosend=True):
        """
        Arguments
        ---------
        body (str):
            body of text message, or media id/link if audio/video/image/document
        preview_url (bool):
            True: Show page preview for any urls included in body.
        """
        return Whatsapp(
            contact, "text", body=body, preview_url=preview_url, autosend=autosend
        )

    @staticmethod
    def template(name="", contact="", language_code="", autosend=True):
        name = name or "hello_world"
        language = {"code": language_code or "en_US"}
        return Whatsapp(
            contact, "template", name=name, language=language, autosend=autosend
        )
