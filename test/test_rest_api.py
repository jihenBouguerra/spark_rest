import unittest


class TestRestAPI(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_upper_(self):
        self.assertEqual('fo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
