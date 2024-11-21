import re
import requests
import unittest

def is_binary_multiple_3(binary_string):
    if re.fullmatch(r'[01]+', binary_string):
        decimal_value = int(binary_string, 2)
        return decimal_value % 3 == 0
    return False

def find_binaries_3(text):
    binary_pattern = r'\b[01]+\b'
    binaries = re.findall(binary_pattern, text)
    # Оставляем только кратные 3
    multiples_of_3 = [b for b in binaries if is_binary_multiple_3(b)]
    return multiples_of_3