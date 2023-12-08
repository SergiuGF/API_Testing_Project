import unittest
from Simple_Books_Request import SimpleBooksRequest


class TestGetBooks(unittest.TestCase):
    def setUp(self) -> None:
        self.books_api = SimpleBooksRequest()

    def test_get_books(self):
        response = self.books_api.get_books()
        expected_number_books = 6
        actual_number_of_books = len(response.json())
        self.assertEqual(expected_number_books, actual_number_of_books)

        # print(len(response.json()[0]))
        for i in range(actual_number_of_books):
            # print(len(response.json()[i]))
            self.assertEqual(4, len(response.json()[i]))

    def test_get_books_fiction(self):
        response = self.books_api.get_books('fiction')
        cnt = 0
        actual_number_of_books = len(response.json())
        for i in range(actual_number_of_books):
            if response.json()[i]['type'] == 'fiction':
                cnt += 1

        print(cnt)

    def test_get_books_limit(self):
        response = self.books_api.get_books(limit=3)

        actual_number_of_books = len(response.json())
        self.assertEqual(3, actual_number_of_books)

    def test_get_books_non_fiction(self):
        response = self.books_api.get_books('non-fiction')
        cnt = 0
        actual_number_of_books = len(response.json())
        for i in range(actual_number_of_books):
            if response.json()[i]['type'] == 'non-fiction':
                cnt += 1

        print(cnt)

    def test_get_books_fiction_with_limit(self):
        response = self.books_api.get_books('fiction', 2)
        cnt = 0
        actual_number_of_books = len(response.json())
        for i in range(actual_number_of_books):
            if response.json()[i]['type'] == "fiction":
                cnt += 1

        self.assertEqual(2, cnt)

    def test_get_books_non_fiction_with_limit(self):
        response = self.books_api.get_books('non-fiction', 1)
        cnt = 0
        actual_number_of_books = len(response.json())
        for i in range(actual_number_of_books):
            if response.json()[i]['type'] == 'non-fiction':
                cnt += 1

        self.assertEqual(1, cnt)

    def test_get_books_negative_limit(self):
        response = self.books_api.get_books(limit=-5)

        self.assertEqual("Invalid value for query parameter 'limit'. Must be greater than 0.",
                         response.json()['error'])

    def test_with_greater_limit(self):
        response = self.books_api.get_books(limit=21)

        self.assertEqual("Invalid value for query parameter 'limit'. Cannot be greater than 20.",
                         response.json()['error'])

    def test_with_greater_than_0(self):


        # self.assertEqual("Invalid value for query parameter 'limit'. Must be greater than 0.",
        # response.json()['error'])
        # range(start, stop, step)
        for i in range(-10, 0, 1):
            response = self.books_api.get_books(limit=i)
            self.assertEqual("Invalid value for query parameter 'limit'. Must be greater than 0.",
                             response.json()['error'])

            print(i)

        for i in range(21, 30, 1):
            response = self.books_api.get_books(limit=i)
            self.assertEqual("Invalid value for query parameter 'limit'. Cannot be greater than 20.",
                             response.json()['error'])

            print(i)
