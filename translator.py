# -*- coding: utf-8 -*-
"""Translator module"""
from __future__ import division
from data import NUMBERS


class Translator(object):
    """Translator class"""

    @classmethod
    def translate(cls, data):
        """The method for converting a input data to number instance """
        if isinstance(data, str):
            str_result = "".join(char for char in data if char.isdigit())
            value = int(str_result) if str_result else 0
        elif isinstance(data, (int, float, long)):
            value = data
        else:
            raise TypeError("Expected {} or {} / {}. But taken {}".format(str, int, float, data))
        return value

    def __enter__(self):
        self.translate = self.context_translate
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

    @classmethod
    def context_translate(cls, data):
        """TRANSLATE methodf"""
        value = cls.translate(data)
        sign = "" if value >= 0 else NUMBERS["minus"]
        abs_value = abs(value)
        if value in NUMBERS and value < 100:
            str_value = NUMBERS[abs_value]
        else:
            str_value = " ".join(cls._get_power_thousand(abs_value))
        return " ".join((sign, str_value))

    @classmethod
    def _get_power_thousand(cls, value):
        """Sort out with thousand to the power"""
        while value >= 1:
            len_value = len(str(value))
            power_thousand = 10 ** ((len_value - 1) // 3 * 3)
            value_under_thousand = value // power_thousand

            str_value_under_thousand = " ".join(cls._get_under_thousand(value_under_thousand))

            str_power_thousand = NUMBERS[power_thousand] if power_thousand > 1 else ""
            str_value = " ".join((str_value_under_thousand, str_power_thousand))
            value -= value_under_thousand * power_thousand
            yield str_value

    @classmethod
    def _get_under_thousand(cls, value):
        """Sort out with values under thousand"""
        while value >= 1:
            if value >= 100:
                quantity_hundreds = value // 100
                value -= quantity_hundreds * 100
                str_and = NUMBERS["and"] if value > 0 else ""
                str_value = " ".join((NUMBERS[quantity_hundreds], NUMBERS[100], str_and))
            elif value in NUMBERS:
                str_value = NUMBERS[value]
                value = 0
            else:
                value_tens = value // 10 * 10
                str_value = NUMBERS[value_tens]
                value = value - value_tens
            yield str_value



