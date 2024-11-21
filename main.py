import re
import requests
import unittest

def is_binary_multiple_3(binary_string):
    if re.fullmatch(r'[01]+', binary_string):
        decimal_value = int(binary_string, 2)
        return decimal_value % 3 == 0
    return False
