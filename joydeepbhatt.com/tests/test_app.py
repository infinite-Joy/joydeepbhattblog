from main import app

import os
import unittest
import tempfile


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        self.app = app.test_client()
        # flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'Kenneth' in rv.data


if __name__ == '__main__':
    unittest.main()
