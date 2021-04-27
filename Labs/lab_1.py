"""
This is the first lab for python. There are 10 exercises. 5 for strings and 5 for integers.
To test this, ensure you're in your ACE Lab directory and enter:
    python -m unittest Tests/test_lab_1.py -vv

Once all tests pass, run the following:
    pylint Labs/lab_1.py

Remediate all warnings to complete the lab.
"""


def main():
    """
    This exercise tests some basic operator exercises.
    INSTRUCTIONS:
    Each set of exercises contains a set of pre-set variables and a set of output variables. The
    input variables are identified by letters, and the outputs by numbers. For example, the string
    inputs are: stra, strb, strc, etc. while the string outputs are str1, str2, str3, etc.

    All problems should be completed with a single operator.

    Each of the outputs should be set to an expression using the inputs that sets the output
    variable to the desired value. For example:
    # Parameters
    intx = 1
    inty = 1
    # Problem: str10 should evaluate to 2
    # Answer:
    str10 = strx + stry
    might be an exercise
    :return:
    """
    # Integers
    # Complete Problems 1-5 using only the following variables. The answers should be integers.
    # For example: int1 = inta + intb. Do not use hard-coded numbers in the solution.
    inta = 54
    intb = 27

    # Problem 1:
    # int1 should resolve to 1458
    int1 = None
    # Problem 2
    # int2 should resolve to 81
    int2 = None
    # Problem 3
    # int3 should resolve to 2
    int3 = None
    # Problem 4
    # int4 should resolve to 38
    int4 = None
    # Problem 5
    # int5 should resolve to 583
    int5 = None

    # Strings
    # Complete Problems 6-10 using only the following variables. The answers should be strings
    # unless otherwise specified.
    # For example: int1 = inta + intb. Do not use hard-coded strings in the solution.
    stra = "test string 1"
    strb = "TeSt sTrInG 2"

    # Problem 6
    # str1 should resolve to 'test string 1TeSt sTrIngG2'
    str1 = None
    # Problem 7
    # str2 should resolve to 'test string 1 TeSt sTrInG2'
    str2 = None
    # Problem 8
    # str3 should resolve to 'test string 2'
    str3 = None
    # Problem 9
    # str4 should resolve to 'TEST STRING 1'
    str4 = None
    # Problem 10
    # str5 should resolve to ['test', 'string', '1']
    # This should be a list
    str5 = None

    # This output tests your solution. Do not modify this dictionary
    output = {'int1': int1, 'int2': int2, 'int3': int3, 'int4': int4, 'int5': int5,
              'str1': str1, 'str2': str2, 'str3': str3, 'str4': str4, 'str5': str5}
    return output


if __name__ == '__main__':
    main()
