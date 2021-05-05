import unittest
from Labs import lab_0


class TestModule0(unittest.TestCase):

    def test_problem_1(self):
        # Test to ensure answer to Problem 1 is an integer
        result = lab_0.main()
        self.assertEqual(type(result['prob1']), int)

    def test_problem_2(self):
        # Test to ensure answer to Problem 2 is a string
        result = lab_0.main()
        self.assertEqual(type(result['prob2']), str)

    def test_problem_3a(self):
        # Test to ensure answer to Problem 3 is an integer
        result = lab_0.main()
        self.assertEqual(type(result['prob3']), int)

    def test_problem_3b(self):
        # Test to ensure answer to Problem 3 is not the same as the answer to Problem 1
        result = lab_0.main()
        self.assertFalse(result['prob1'] == result['prob3'])
