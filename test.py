from tools.numbers.comp import is_palindrome, sum_of_digits
from tools.numbers.col import my_zip
from tools.numbers.simp import adding_numbers, subtracting_numbers

simp_module_called = False

def test_adding(num1, num2):
    global simp_module_called
    simp_module_called = True
    print(adding_numbers(num1, num2))


def test_subtracting(num1, num2):
    global simp_module_called
    simp_module_called = True
    print(subtracting_numbers(num1, num2))


def test_col_module(list1, list2):
    print(my_zip(list1, list2))


def test_palindrom(num):
    if not simp_module_called:
        raise Exception("Cannot call comp_function before calling any function in simp module")
    print(is_palindrome(num))

def test_sum_of_digits(num):
    if not simp_module_called:
        raise Exception("Cannot call comp_function before calling any function in simp module")
    print(sum_of_digits(num))