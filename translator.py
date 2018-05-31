# -*- coding: utf-8 -*-
"""Translator module"""
from __future__ import division
from data import NUMBERS


class Translator(object):
    """Translator class"""

    @staticmethod
    def translate(data):
        """The method for converting a input data to number instance """
        if isinstance(data, str):
            str_result = "".join(chr for chr in data if chr.isdigit())
            result = int(str_result) if str_result else 0
        elif isinstance(data, (int, float)):
            result = data
        else:
            raise TypeError("Expected {} or {} / {}. But taken {}".format(str, int, float, data))
        return result

    def __enter__(self):
        self.translate = self.context_translate
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

    @staticmethod
    def context_translate(num):
        assert isinstance(num, (int, float, long))
        str_number = ""
        current_num = num

        while current_num >= 1:
            len_num = len(str(current_num))
            thousand_pow = 10 ** ((len_num - 1) // 3 * 3)
            value = current_num // thousand_pow
            str_value = ""
            curr_val = value
            while curr_val >= 1:
                len_num = len(str(curr_val))
                ten_pow = 10 ** (len_num - 1)

                str_val = NUMBERS.get(curr_val)
                if str_val and curr_val < 100:
                    str_value = "{} {}".format(str_value, str_val)
                    break

                str_val = NUMBERS.get(curr_val // ten_pow * ten_pow)
                if str_val and curr_val < 100:
                    str_value = "{} {}".format(str_value, str_val)
                    curr_val -= curr_val // ten_pow * ten_pow
                    continue

                val = curr_val // ten_pow
                str_val = NUMBERS[val]

                str_value = "{} {} {}".format(str_value, str_val, NUMBERS[ten_pow])
                curr_val -= val * ten_pow

            str_number = "{} {} {}".format(str_number, str_value, NUMBERS[thousand_pow])
            current_num -= value * thousand_pow

        return str_number
