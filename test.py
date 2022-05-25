import pytest
from whatsapp import *

class Test_core_functionality():
    def test_send(self):
        wa = Whatsapp()
        assert wa.response.status_code == 200

    def test_cleverdict_aliases(self):
        wa = Whatsapp(autosend=False)
        assert wa.data.messaging_product == 'whatsapp'
        assert wa.data.to == CONTACTS[0]
        assert wa.data.type == 'text'
        assert not hasattr(wa.data, "response")
        assert wa.data.text == {'preview_url': True, 'body': TEST_MESSAGE + TEST_URL}

    def test_content(self):
        wa = Whatsapp("Another test message", autosend=False)
        assert wa.data == {'messaging_product': 'whatsapp', 'to': CONTACTS[0], 'type': 'text', 'text': {'preview_url': True, 'body': 'Another test message'}}

    def test_contact(self):
        wa = Whatsapp("", CONTACTS[1], autosend=False)
        assert wa.data.to == CONTACTS[1]
        assert wa.data.text['body'] == TEST_MESSAGE + TEST_URL

    def test_no_preview(self):
        data = {"text": {"preview_url": False}}
        wa = Whatsapp(autosend=False, **data)
        assert not wa.data.text['preview_url']
