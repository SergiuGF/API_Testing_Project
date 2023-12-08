import unittest
from Simple_Books_Request import SimpleBooksRequest


class TestSubmitOrder(unittest.TestCase):
    # declaram access_token la nivel de clasa ca sa folosim acelasi token la toate testele
    # initial va fi = ""
    access_token = ""

    def setUp(self):
        self.books_api = SimpleBooksRequest()
        if self.access_token == "":
            self.access_token = self.books_api.generate_token()

    def test_submit_order_status_code(self):
        response = self.books_api.submit_order(self.access_token, bookId=1, customerName='John')

        expected_response_code = 201
        actual_response_code = response.status_code
        self.assertEqual(expected_response_code, actual_response_code)


