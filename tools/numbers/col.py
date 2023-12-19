"""
This module is a wrraper for a zip method
"""

def my_zip(it1 , it2):
    # Ensure both collections are of the same length
    if len(it1) != len(it2):
        raise ValueError("Collections must have the same length")

    # Use zip function and list constructor to create a list of tuples
    result = list(zip(it1, it2))

    return result