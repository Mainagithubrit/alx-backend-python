#!/usr/bin/env python3
"""A type annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function to multiply multiplier with"""
    return lambda x: x * multiplier
