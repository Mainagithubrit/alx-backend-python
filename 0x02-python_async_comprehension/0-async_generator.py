#!/usr/bin/env python3
""" A coroutine"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A coroutine that loops 10 times,
    and waits for 1 second before printing each value"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.random() * 10
