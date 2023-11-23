import unittest
from server import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/index')
        self.assertEqual(response.status_code, 200)

    def test_nosotros(self):
        response = self.app.get('/nosotros')
        self.assertEqual(response.status_code, 200)

    def test_romper(self):
        response = self.app.get('/entrada')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()