#!/usr/bin/env python3
"""A type annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A function that returns the sum of integers and floats,
    in a list"""
    return float(sum(mxd_lst))
