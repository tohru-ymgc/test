#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate_defference(num_control,num_actual):
    num_of_difference = abs(num_control - num_actual)
    return num_of_difference


def lastline_is_equal(lastline):
    if lastline == "===":
        return True

    else:
        return False


if __name__ == "__main__":
    pass