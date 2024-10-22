#!/usr/bin/env python3
"""A Type annotated function"""

from typing import Tuple, Iterable, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """A function that returns a List with a tuple"""
    return [(i, len(i)) for i in lst]
