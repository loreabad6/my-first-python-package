import lorepy
import unittest

class TestHello(unittest.TestCase):

  def test_hello(self):
    self.assertIsNone(lorepy.hello())