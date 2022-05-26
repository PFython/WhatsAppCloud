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
            numeric phone number starting with country code; no "+" or leading 0
        body (str):
            body of text message, or media id/link if audio/video/image/document
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
            self.data[content_type] = kwargs
        if autosend:
            self.send()

    def send(self):
        self.response = requests.post(ENDPOINT, headers=HEADERS, json=self.data)

    @staticmethod
    def text(body="", contact="", preview_url=True, **kwargs):
        data = {"body": body, "preview_url": preview_url}
        # NB content_type must be "" for __init__ to populate "body" correctly
        return Whatsapp(contact, "text", **(dict(data, **kwargs)))

    @staticmethod
    def template(template_name="", contact="", language_code="", **kwargs):
        data = {
            "name": template_name or "hello_world",
            "language": {"code": language_code or "en_US"},
        }
        return Whatsapp(contact, "template", **dict(data, **kwargs))

    @staticmethod
    def location(contact="", lat="", long="", name="", address="", **kwargs):
        data = {
            "latitude": lat or "50.900089",
            "longitude": long or "-3.490490",
            "name": name or "Tiverton",
            "address": address or "Devon, UK",
        }
        return Whatsapp(contact, "location", **(dict(data, **kwargs)))

    @staticmethod
    def image(link="", contact="", caption="", **kwargs):
        data = {"link": link, "caption": caption}
        return Whatsapp(contact, "image", **(dict(data, **kwargs)))

    @staticmethod
    def image_id(contact="", **kwargs):
        data = {"id": image, "caption": caption}
        return Whatsapp(contact, "image_id", **(dict(data, **kwargs)))


    @staticmethod
    def video(contact="", **kwargs):
        data = {"link": video, "caption": caption}
        return Whatsapp(contact, "video", **(dict(data, **kwargs)))

    @staticmethod
    def video_id(contact="", **kwargs):
        data = {"id": video, "caption": caption}
        return Whatsapp(contact, "video_id", **(dict(data, **kwargs)))

    @staticmethod
    def document(contact="", **kwargs):
        data = {"link": document, "caption": caption}
        return Whatsapp(contact, "document", **(dict(data, **kwargs)))

    @staticmethod
    def document_id(contact="", **kwargs):
        data = {"id": document, "caption": caption}
        return Whatsapp(contact, "document_id", **(dict(data, **kwargs)))
