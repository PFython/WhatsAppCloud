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
        return Whatsapp(contact, "text", body=body, preview_url=preview_url, autosend=autosend)

    @staticmethod
    def template(name="", contact="", language_code="", autosend=True):
        name = name or "hello_world"
        language = {"code": language_code or "en_US"}
        return Whatsapp(contact, "template", name=name, language=language, autosend=autosend)

    @staticmethod
    def location(lat="", long="", name="", address="", contact="", autosend=True):
        kwargs = {
            "latitude": lat or "50.900089",
            "longitude": long or "-3.490490",
            "name": name or "Tiverton",
            "address": address or "Devon, UK",
        }
        return Whatsapp(contact, "location", autosend=autosend, **kwargs)

    @staticmethod
    def document(link="", contact="", autosend=True):
        link = link or "https://binaries.templates.cdn.office.net/support/templates/en-gb/tf00112764_win32.dotx"
        return Whatsapp(contact, "document", link=link, autosend=autosend)

    @staticmethod
    def image(link="", contact="", caption="", autosend=True):
        link = link or "https://imgs.xkcd.com/comics/python.png"
        return Whatsapp(contact, "image", link=link, caption=caption, autosend=autosend)

    @staticmethod
    def image_id(id, contact="", caption="", autosend=True):
        # TODO: Work in progress
        return Whatsapp(contact, "image", id=id, caption=caption, autosend=autosend)

    @staticmethod
    def audio(link="", contact="", caption="", autosend=True):
        link = link or "https://www2.cs.uic.edu/~i101/SoundFiles/ImperialMarch60.wav"
        # TODO: Work in progress
        return Whatsapp(contact, "audio", link=link, caption=caption, autosend=autosend)

    @staticmethod
    def audio_id(id, contact="", caption="", autosend=True):
        # TODO: Work in progress
        return Whatsapp(contact, "audio", autosend=autosend)

    @staticmethod
    def video(link="", contact="", caption="", autosend=True):
        # TODO: Work in progress
        link = link or "https://www.youtube.com/watch?v=qetW6R9Jxs4"
        return Whatsapp(contact, "video", link=link, caption=caption, autosend=autosend)

    @staticmethod
    def video_id(id, contact="", caption=""):
        # TODO: Work in progress
        return Whatsapp(contact, "video", id=id, caption=caption, autosend=autosend)


    @staticmethod
    def document_id(id, contact="", autosend=True):
        # TODO: Work in progress
        return Whatsapp(contact, "document", id=id, autosend=autosend)

    @staticmethod
    def sticker(link, contact="", caption="", autosend=True):
        # TODO: Work in progress
        return Whatsapp(contact, "sticker", link=link, caption=caption, autosend=autosend)

    @staticmethod
    def sticker_id(id, contact="", caption="", autosend=True):
        # TODO: Work in progress
        return Whatsapp(contact, "image", id=id, caption=caption, autosend=autosend)

    @staticmethod
    def upload_media(media):
        # TODO: Work in progress
        return

    @staticmethod
    def download_media(media):
        # TODO: Work in progress
        return

    @staticmethod
    def contact(contact_json="", contact="", autosend=True):
        """
        contact_json: list of dicts containing actual contact data
        contact (str): Phone number of the contact you're sending a message to
        """
        # TODO: Work in progress
        contact_json = contact_json or [{
            "addresses": [{
                "street": "STREET",
                "city": "CITY",
                "state": "STATE",
                "zip": "ZIP",
                "country": "COUNTRY",
                "country_code": "COUNTRY_CODE",
                "type": "HOME"
                },
                {
                "street": "STREET",
                "city": "CITY",
                "state": "STATE",
                "zip": "ZIP",
                "country": "COUNTRY",
                "country_code": "COUNTRY_CODE",
                "type": "WORK"
                }],
            "birthday": "YEAR_MONTH_DAY",
            "emails": [{
                "email": "EMAIL",
                "type": "WORK"
                },
                {
                "email": "EMAIL",
                "type": "HOME"
                }],
            "name": {
                "formatted_name": "NAME",
                "first_name": "FIRST_NAME",
                "last_name": "LAST_NAME",
                "middle_name": "MIDDLE_NAME",
                "suffix": "SUFFIX",
                "prefix": "PREFIX"
            },
            "org": {
                "company": "COMPANY",
                "department": "DEPARTMENT",
                "title": "TITLE"
            },
            "phones": [{
                "phone": "PHONE_NUMBER",
                "type": "HOME"
                },
                {
                "phone": "PHONE_NUMBER",
                "type": "WORK",
                "wa_id": "PHONE_OR_WA_ID"
                }],
            "urls": [{
                "url": "URL",
                "type": "WORK"
                },
                {
                "url": "URL",
                "type": "HOME"
                }]
            }]
        return Whatsapp(contact, "contacts", contacts=contact_json, autosend=autosend)

    @staticmethod
    def button(button,contact):
        kwargs = {
            "type": "list",
            "header": {"type": "text", "text": button.get("header")},
            "body": {"text": button.get("body")},
            "footer": {"text": button.get("footer")},
            "action": button.get("action"),
        }
        return Whatsapp(contact, "interactive", create_button(button),autosend=autosend, **kwargs)

