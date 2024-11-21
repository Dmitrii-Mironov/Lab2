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

class TestBinaryMultiple3(unittest.TestCase):

    def test_binary_multiple_3(self):
        # Тест двоичные числа, которые кратны 3
        self.assertTrue(is_binary_multiple_3('0')) # 0
        self.assertTrue(is_binary_multiple_3('11')) # 3
        self.assertTrue(is_binary_multiple_3('110')) # 6
        self.assertTrue(is_binary_multiple_3('111')) # 7(проверка теста)
        self.assertTrue(is_binary_multiple_3('1100')) # 12

    def test_binary_not_multiple_3(self):
        # Тест двоичные числа, которые не кратны 3
        self.assertFalse(is_binary_multiple_3('1')) # 1
        self.assertFalse(is_binary_multiple_3('10')) # 2
        self.assertFalse(is_binary_multiple_3('100')) # 4
        self.assertFalse(is_binary_multiple_3('101')) # 5
        self.assertFalse(is_binary_multiple_3('1111')) # 15(проверка теста)

    def test_invalid_binary_strings(self):
        # Тест некорректные двоичные строки
        self.assertFalse(is_binary_multiple_3(''))  # пустая строка
        self.assertFalse(is_binary_multiple_3('abc'))
        self.assertFalse(is_binary_multiple_3('2')) # не двоичная запись
        self.assertFalse(is_binary_multiple_3('a'))
        self.assertFalse(is_binary_multiple_3('12'))

    def test_mixed_valid_and_invalid_binaries(self):
        binaries = ['110', '101', '2', '011', 'abc', '1111', '000', '111111']
        results = [is_binary_multiple_3(b) for b in binaries]
        expected_results = [True, False, False, True, False, False, True, True]
        self.assertEqual(results, expected_results)