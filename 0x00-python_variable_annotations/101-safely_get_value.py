#!/usr/bin/env python3
"""A type annotated function"""

from typing import Union, Mapping, Any, TypeVar


def safely_get_value(dict: Mapping, key: Any, default: Union[TypeVar, None]
                     = None) -> Union[Any, TypeVar]:
    """Type annotation"""
    if key in dct:
        return dct[key]
    else:
        return default
