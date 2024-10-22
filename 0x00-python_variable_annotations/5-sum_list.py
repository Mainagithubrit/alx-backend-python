#!/usr/bin/env python3
"""A type annotated function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """A function that takes a list of floats"""
    return float(sum(input_list))
