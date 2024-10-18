#!/usr/bin/env python3
"""An Asynchronous Coroutine function"""

import asyncio
import random


async def wait_random(max_delay=10) -> float:
    """waits for a random number of seconds"""
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time
