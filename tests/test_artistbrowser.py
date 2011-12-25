import unittest
from spotify._mockspotify import mock_artistbrowse, mock_artist
from tests import SkipTest

callback_called = False
callback_userdata = None

class TestArtistbrowser(unittest.TestCase):

    artist = mock_artist("foo0", 1)

    def callback(self, browser, userdata):
        global callback_called
        global callback_userdata
        callback_called = True
        callback_userdata = userdata

    def test_is_loaded(self):
        browser = mock_artistbrowse(self.artist, 1)
        assert browser.is_loaded()

    def test_is_not_loaded(self):
        browser = mock_artistbrowse(self.artist, 0)
        assert not browser.is_loaded()

    def test_sequence(self):
        browser = mock_artistbrowse(self.artist, 1)
        assert len(browser) == 3
        assert browser[0].name() == 'foo'
        assert browser[1].name() == 'bar'
        assert browser[2].name() == 'baz'

    def test_callback(self):
        global callback_called
        global callback_userdata
        callback_called = False
        browser = mock_artistbrowse(self.artist, 0, self.callback, self)
        self.assertTrue(callback_called)
        self.assertEqual(callback_userdata, self)
