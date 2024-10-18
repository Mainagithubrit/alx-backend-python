#!/usr/bin/env python3
"""A module"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """A module that measures the total execution time,
    for wait_n(n, max_delay)"""

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
