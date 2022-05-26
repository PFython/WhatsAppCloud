import pytest
from whatsapp import Whatsapp, CleverDict, CONTACTS, TEST_MESSAGE, TEST_URL


class Test_core_functionality:
    def test_default_send(self):
        wa = Whatsapp()
        assert wa.response.status_code == 200

    def test_cleverdict_aliases(self):
        autosend = False
        wa = Whatsapp(autosend=autosend)
        assert wa.data.messaging_product == "whatsapp"
        assert wa.data.to == CONTACTS[0]
        assert wa.data.type == "text"
        assert wa.data.text.preview_url
        assert wa.data.text.body == TEST_MESSAGE + TEST_URL
        if autosend:
            assert wa.response
            assert wa.response.text
            assert wa.response.status_code
            assert wa.response.request.body

    def test_body_text(self):
        autosend = True
        wa = Whatsapp(body="Another test message", autosend=autosend)
        assert wa.data == {
            "messaging_product": "whatsapp",
            "to": CONTACTS[0],
            "type": "text",
            "text": {"preview_url": True, "body": "Another test message"},
        }

    def test_no_preview(self):
        autosend = True
        wa = Whatsapp(preview_url=False, autosend=autosend)
        assert not wa.data.text.preview_url

    def test_new_contact(self):
        autosend = False
        wa = Whatsapp(CONTACTS[1], autosend=autosend)
        assert wa.data.to == CONTACTS[1]
        assert wa.data.text.body == TEST_MESSAGE + TEST_URL
        wa = Whatsapp(contact=CONTACTS[1], autosend=autosend)
        assert wa.data.to == CONTACTS[1]
        assert wa.data.text.body == TEST_MESSAGE + TEST_URL


class Test_other_message_types:

    def test_text(self):
        autosend = True
        wa = Whatsapp.text(body="Call on me! https://www.youtube.com/watch?v=qetW6R9Jxs4", preview_url=False, autosend=autosend)
        assert not wa.data.text.preview_url

    def test_template(self):
        autosend = True
        wa = Whatsapp.template(autosend=autosend)
        assert wa.data == {
            "messaging_product": "whatsapp",
            "to": CONTACTS[0],
            "type": "template",
            "template": {"name": "hello_world", "language": {"code": "en_US"}},
        }

        autosend = False
        wa = Whatsapp.template(
            contact=CONTACTS[1],
            name="new_urgent_item",
            language_code="en",
            autosend=autosend,
        )
        assert wa.data.template == {
            "name": "new_urgent_item",
            "language": {"code": "en"},
        }
        assert wa.data.to == CONTACTS[1]

    def test_location(self):
        autosend = True
        wa = Whatsapp.location(autosend=autosend)
        assert wa.data == {
            "messaging_product": "whatsapp",
            "to": CONTACTS[0],
            "type": "location",
            "location": {
                "latitude": "50.900089",
                "longitude": "-3.490490",
                "name": "Tiverton",
                "address": "Devon, UK",
            },
        }

        autosend = False
        wa = Whatsapp.location(
            contact=CONTACTS[1],
            name="Bag End",
            address="The Shire",
            autosend=autosend
        )
        assert wa.data.to == CONTACTS[1]
        assert wa.data.location == {
            "latitude": "50.900089",
            "longitude": "-3.490490",
            "name": "Bag End",
            "address": "The Shire",
        }

    def test_image(self):
        wa = Whatsapp.image(caption="_*Antigravity*_")
        assert wa.data.image,link == 'https://imgs.xkcd.com/comics/python.png'

        link = "https://raw.githubusercontent.com/PFython/cleverdict/master/resources/cleverdict.png"

        wa = Whatsapp.image(link, caption="CleverDict logo", autosend=True)
        assert wa.data.image == {'link': 'https://raw.githubusercontent.com/PFython/cleverdict/master/resources/cleverdict.png', 'caption': 'CleverDict logo'}

        autosend = False
        wa = Whatsapp.image(link, CONTACTS[1], "CleverDict logo", autosend=autosend)
        assert wa.data.to == CONTACTS[1]
        assert wa.data.image.link == 'https://raw.githubusercontent.com/PFython/cleverdict/master/resources/cleverdict.png'
        wa.data.image.caption == 'CleverDict logo'

    def test_document(self):
        wa = Whatsapp.document()
        assert wa.data.document.link == 'https://binaries.templates.cdn.office.net/support/templates/en-gb/tf00112764_win32.dotx'

        # TODO: Filename

        autosend=False
        wa = Whatsapp.document("", CONTACTS[1], autosend=autosend)


    def test_video(self):
        wa = Whatsapp.video(autosend=True)

    def test_audio(self):
        wa = Whatsapp.audio(autosend=True)

