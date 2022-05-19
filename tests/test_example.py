import unittest

class ExampleTestCase(unittest.TestCase):
    """
    Test the example module as part of demonstrated CI workflow
    """
    def test_example(self):
        number_one = 1
        self.assertTrue(number_one == 1)
