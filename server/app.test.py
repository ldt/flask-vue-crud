import unittest
import json

from app import app


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/ping', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        assert b'pong pong' in response.data


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a blank temp database before each test."""
        self.app = app.test_client()

    def tearDown(self):
        """Destroy blank temp database after each test."""
        pass

    def test_books(self):
        """check that /books return a list of books. """
        rv = self.app.get('/books')
        data = json.loads((rv.data).decode('utf-8'))
        self.assertEqual(type(data['books']), list)


if __name__ == '__main__':
    unittest.main()
