import unittest
from app import app
import json

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        # Küldünk egy GET kérést
        response = self.app.get('/')
        # Ellenőrizzük, hogy a státusz kód 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Ellenőrizzük a tartalmat
        data = json.loads(response.data)
        self.assertEqual(data['message'], "Szia, ez a beadando alkalmazasom!")

if __name__ == "__main__":
    unittest.main()
