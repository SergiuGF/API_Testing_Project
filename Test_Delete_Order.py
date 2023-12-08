import unittest
from Simple_Books_Request import SimpleBooksRequest


class TestDeleteOrder(unittest.TestCase):
    access_token = ""

    def setUp(self):
        self.books_api = SimpleBooksRequest()
        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_delete_an_order(self):
        response = self.books_api.delete_an_order(self.access_token, orderId="OAeAUneKzwxgXNtXAQYqb")
        expected_response_code = 404
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code)
