#!/usr/bin/env pyrhon3

"""A module"""
from typing import List

async_generator =__import__ ('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """A coroutine that collects 10 random numbers,
    using an async comprehension"""

    return [n async for n in async_generator()]
