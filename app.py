"""
The main of the project to test and run
"""

from test import test_adding, test_col_module, test_palindrom, test_subtracting, test_sum_of_digits


def main():
    #test the sum of two numbers
    test_adding(10, 20)

    #test the subtracting of two numbers
    test_subtracting(20, 10)
    #test for a palindrom number
    test_palindrom(12321)

    #test for not a palindrom number
    test_palindrom(123241)

    #test the sum of digits
    test_sum_of_digits(1123)

    #test the zip method
    list1 = ("Sunday", "Monday", "Friday")
    list2 = (1, 2, 6)
    test_col_module(list1, list2)


if __name__ == "__main__":
    main()