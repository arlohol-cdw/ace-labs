import unittest
from Labs import lab_1


class TestModule1(unittest.TestCase):
    """
    Series of tests to validate Lab 1 on basic operators for strings and integers
    """

    def test_problem_1(self):
        result = lab_1.main()
        self.assertEqual(result['int1'], 1458)

    def test_problem_2(self):
        result = lab_1.main()
        self.assertEqual(result['int2'], 81)

    def test_problem_3(self):
        result = lab_1.main()
        self.assertEqual(result['int3'], 2)

    def test_problem_4(self):
        result = lab_1.main()
        self.assertEqual(result['int4'], 2.0)

    def test_problem_5(self):
        result = lab_1.main()
        self.assertEqual(result['int5'], 0)

    def test_problem_6(self):
        result = lab_1.main()
        self.assertEqual(result['str1'], 'test string 1TeSt sTrInG 2')

    def test_problem_7(self):
        result = lab_1.main()
        self.assertEqual(result['str2'], 'test string 1 TeSt sTrInG 2')

    def test_problem_8(self):
        result = lab_1.main()
        self.assertEqual(result['str3'], 'test string 2')

    def test_problem_9(self):
        result = lab_1.main()
        self.assertEqual(result['str4'], 'TEST STRING 1')

    def test_problem_10(self):
        result = lab_1.main()
        self.assertEqual(result['str5'], ['test', 'string', '1'])


if __name__ == '__main__':
    unittest.main()
