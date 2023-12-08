import unittest
from Simple_Books_Request import SimpleBooksRequest


class TestApiStatus(unittest.TestCase):
    def setUp(self):
        self.books_api = SimpleBooksRequest()

    def test_api_status(self):
        response = self.books_api.get_api_status()

        expected_response_code = 200
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code)

        expected_response_message = 'OK'
        actual_response_message = response.json()['status']
        self.assertEqual(expected_response_message, actual_response_message)