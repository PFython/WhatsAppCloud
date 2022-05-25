# Send Whatsapp messages from Python - absolutely free!

It's true - you really can send free messages to five (verified) phone numbers for free using Meta's [WhatsApp Business Platform](https://developers.facebook.com/products/whatsapp/).  The only stipulation is that you observe their terms and conditions, especially regarding opting-in and acceptable use, and there are other restrictions

The even better news is that I've waded my way through the API docs and created a minimalist wrapper in about 20 lines which you can copy into your own scripts and enjoy Whatsapp automation with importing a single extra dependency.


## TLDR:
![](Screenshot%201.png)
```
import requests
from cleverdict import CleverDict
from config import PHONE_ID, CONTACTS, TOKEN, URL, HEADERS, TEST_MESSAGE, TEST_URL

class Whatsapp:

    def __init__(self, content="", contact="", autosend=True, **kwargs):
        content_type = kwargs.get("type")
        self.data = CleverDict({
            "messaging_product": "whatsapp",
            "to": contact or CONTACTS[0],
            "type": content_type  or "text",
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
```
WhatsApp Business Account
reply to first message!
