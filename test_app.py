import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Products', response.data)  # Update this line

    def test_orders(self):
        response = self.app.get('/orders')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Orders', response.data)

if __name__ == '__main__':
    unittest.main()