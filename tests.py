import pytest
from whatsapp import Whatsapp, CleverDict, CONTACTS, TEST_MESSAGE, TEST_URL


class Test_core_functionality:
    def test_default_send(self):
        wa = Whatsapp()
        assert wa.response.status_code == 200

    def test_cleverdict_aliases(self):
        autosend = True
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

    def test_default_content(self):
        autosend = True
        wa = Whatsapp(body="Another test message", autosend=autosend)
        assert wa.data == {
            "messaging_product": "whatsapp",
            "to": CONTACTS[0],
            "type": "text",
            "text": {"preview_url": True, "body": "Another test message"},
        }

    def test_contact(self):
        autosend = False
        wa = Whatsapp(CONTACTS[1], autosend=autosend)
        assert wa.data.to == CONTACTS[1]
        assert wa.data.text.body == TEST_MESSAGE + TEST_URL
        wa = Whatsapp(contact=CONTACTS[1], autosend=autosend)
        assert wa.data.to == CONTACTS[1]
        assert wa.data.text.body == TEST_MESSAGE + TEST_URL

    def test_no_preview(self):
        # Using defaults
        autosend = True
        wa = Whatsapp(preview_url=False, autosend=autosend)
        assert not wa.data.text.preview_url
        # Using the .text() method
        wa = Whatsapp.text(preview_url=False, autosend=autosend)
        assert not wa.data.text.preview_url


class Test_other_message_types:
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
        wa = Whatsapp.template(contact=CONTACTS[1], autosend=autosend)
        wa = Whatsapp.template(
            contact=CONTACTS[1],
            template_name="urgent_new_item",
            language_code="en_UK",
            autosend=autosend,
        )
        assert wa.data.template == {
            "name": "urgent_new_item",
            "language": {"code": "en_UK"},
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
            contact=CONTACTS[1], name="Bag End", address="The Shire", autosend=autosend
        )
        assert wa.data.location == {
            "latitude": "50.900089",
            "longitude": "-3.490490",
            "name": "Bag End",
            "address": "The Shire",
        }
        assert wa.data.to == CONTACTS[1]

    def test_image(self):
        link = "https://raw.githubusercontent.com/PFython/cleverdict/master/resources/cleverdict.png"
        wa = Whatsapp.image(link, caption="CleverDict logo", autosend=True)
        assert wa.data.image == {'link': 'https://raw.githubusercontent.com/PFython/cleverdict/master/resources/cleverdict.png', 'caption': ''}
        wa = Whatsapp.image(link, CONTACTS[1], "CleverDict logo", autosend=False)
        assert wa.data.to == CONTACTS[1]
