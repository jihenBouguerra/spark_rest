import unittest


# pytest -s --junitxml=out.xml
class TestRestAPI(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_upper(self):
    #     self.assertEqual('fo'.upper(), 'FOO')
