from unittest import TestCase
from api.core import BaseProvider


class UnknownDevice(Exception):
    """UnknownDevice exception."""

    pass


class MockProvider(BaseProvider):
    """MockProvider."""

    def __init__(self):
        self._devs = {
            1: {
                'GET_STATE': 'online'
            }
        }

    def send_request(self, address, action, payload=None):
        try:
            ret = self._devs[address][action]
            return ret
        except LookupError:
            raise UnknownDevice


class Walljack():
    """Walljack."""

    def __init__(self, address, provider):
        self._dev_addr = address
        self._dev_prov = provider

    def get_state(self):
        return self._dev_prov.send_request(self._dev_addr, 'GET_STATE')


class WalljackTestCase(TestCase):
    def setUp(self):
        self._mock_prov = MockProvider()

    def test_walljack_state_request(self):
        wj = Walljack(1, self._mock_prov)
        state = wj.get_state()
        self.assertEqual(state, 'online')
