import requests
import random


class SimpleBooksRequest:
    _BASE_URL = "https://simple-books-api.glitch.me"
    _API_STATUS_ENDPOINT = "/status"
    _GET_BOOKS_ENDPOINT = "/books"
    _API_AUTH_ENDPOINT = "/api-clients"
    _ORDERS_ENDPOINT = "/orders"

    def get_api_status(self):
        api_status_url = self._BASE_URL + self._API_STATUS_ENDPOINT
        response = requests.get(api_status_url)
        return response

    def get_books(self, book_type='', limit=''):
        get_books_url = self._BASE_URL + self._GET_BOOKS_ENDPOINT

        if book_type != '' and limit == '':
            get_books_url += f'?type={book_type}'

        if book_type == '' and limit != '':
            get_books_url += f'?limit={limit}'

        if book_type != '' and limit != '':
            get_books_url += f'?type={book_type}&limit={limit}'

        response = requests.get(get_books_url)
        return response

    def generate_token(self):
        generate_token_url = self._BASE_URL + self._API_AUTH_ENDPOINT
        random_nr = random.randint(5, 9999999999999999999999)
        request_body = {
            "clientName": "Ana",
            "clientEmail": f"ana0{random_nr}@example.com"
        }
        response = requests.post(generate_token_url, json=request_body)
        return response.json()['accessToken']

    def submit_order(self, access_token, bookId, customerName):
        submit_order_url = self._BASE_URL + self._ORDERS_ENDPOINT
        header_body = {
            'Authorization': access_token
        }
        request_body = {
            'bookId': bookId,
            'customerName': customerName
        }

        response = requests.post(submit_order_url, json=request_body, headers=header_body)
        return response

    def delete_an_order(self, access_token, orderId):
        delete_order_url = self._BASE_URL + self._ORDERS_ENDPOINT + f'/{orderId}'
        header_body = {
            'Authorization': access_token
        }
        response = requests.delete(delete_order_url, headers=header_body)
        return response
