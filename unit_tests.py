import unittest
from shortcuts import issue_HTTP_request, make_dictionary_from_JSON


class TestShortcuts(self, unittest.TestCase):
    def test_issue_HTTP_request(self):
        self.assertEqual(type(issue_HTTP_request()), dict)
        # self.assertEqual

    def test_make_dictionary_from_JSON(self):
        self.assertEqual(type(make_dictionary_from_JSON({}, "Albums")), dict)
        # self.assertEqual(function2(2.1, 1.2), 3.3)

if __name__ == '__main__':
    unittest.main()
