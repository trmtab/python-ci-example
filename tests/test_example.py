import unittest

class ExampleTestCase(unittest.TestCase):
    """
    Test the example module as part of demonstrated CI workflow
    """
    def test_example(self):
        self.assertTrue(1 == 1)

