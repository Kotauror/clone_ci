# from django.test import TestCase
# from journal_app.models import Posts
import unittest

class SimpleTestCase(unittest.TestCase):
    def test_that_number_is_returned(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()