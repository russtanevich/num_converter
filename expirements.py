# -*- coding: utf-8 -*-
"""Module for experiments"""
from __future__ import division
from data import NUMBERS


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
                print(1, curr_val)
                str_value = "{} {}".format(str_value, str_val)
                print(str_val)
                break

            str_val = NUMBERS.get(curr_val // ten_pow * ten_pow)
            if str_val and curr_val < 100:
                print(2, curr_val)
                str_value = "{} {}".format(str_value, str_val)
                curr_val -= curr_val // ten_pow * ten_pow
                print(str_val)
                continue

            val = curr_val // ten_pow
            str_val = NUMBERS[val]

            str_value = "{} {} {}".format(str_value, str_val, NUMBERS[ten_pow])
            curr_val -= val * ten_pow

        str_number = "{} {} {}".format(str_number, str_value, NUMBERS[thousand_pow])
        current_num -= value * thousand_pow

    return str_number


num = 120969601
t = context_translate(num)
print("{} ==> {}".format(num, t))
