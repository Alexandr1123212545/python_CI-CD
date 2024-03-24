import unittest
from unittest.mock import patch
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_all_products(self):
        response = self.app.get('/api/products')
        self.assertEqual(response.status_code, 200)

    def test_get_product_by_id(self):
        response = self.app.get('/api/products/1')
        self.assertEqual(response.status_code, 404)  # Assuming no product with ID 1 initially

    def test_add_product(self):
        data = {'name': 'Test Product', 'price': 10.99}
        response = self.app.post('/api/products', json=data)
        self.assertEqual(response.status_code, 201)

    def test_update_product(self):
        data = {'name': 'Updated Product'}
        response = self.app.patch('/api/products/1', json=data)
        self.assertEqual(response.status_code, 404)  # Assuming no product with ID 1 initially

    def test_delete_product(self):
        response = self.app.delete('/api/products/1')
        self.assertEqual(response.status_code, 202)  # Assuming no product with ID 1 initially


if __name__ == '__main__':
    unittest.main()
