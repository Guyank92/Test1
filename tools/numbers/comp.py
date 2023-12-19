"""
This module has 2 methods for calculate sum of digits
And checking a number if is palindrome
"""
def sum_of_digits(number):
    # checking case that num is 0
    if number == 0 : return 0
    # checking case that num is negative
    if number < 0 :
        number = number*(-1)
    # creating a sum var
    sum=0
    while number > 0:
        sum += number % 10
        number //= 10
    
    return sum

def is_palindrome(number):
    # Convert the number to a string for easy comparison
    str_number = str(number)
    
    # Compare the string with its reverse
    return str_number == str_number[::-1]