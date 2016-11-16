from unittest import TestCase

import time

from serverquery import ServerQuerier


class TestServerQuerier(TestCase):
    def test__check_server(self):
        server = "Test"

        self.assertTrue(ServerQuerier._check_server(server))

        time.sleep(.5)
        self.assertFalse(ServerQuerier._check_server(server))

        time.sleep(1)
        self.assertTrue(ServerQuerier._check_server(server))
