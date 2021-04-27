import unittest
from Labs.module_1 import lab_1


class TestModule1(unittest.TestCase):
    """
    Test return of a particular value
    """
    def test_lab1(self):
        result = lab_1.main()
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()