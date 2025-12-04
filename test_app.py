import unittest
from app import app
import json

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], "Üdvözletem, ez a beadando alkalmazasom!")

if __name__ == "__main__":
    unittest.main()
