#!/usr/bin/env python3
"""A module"""

import time
import asyncio
import tracemalloc

tracemalloc.start()

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """A module that measures the total execution time,
    for wait_n(n, max_delay)"""

    start_time = time.time()
    await wait_n(n, max_delay)
    return (time.time() - start_time) / n

async def main():
    avg_time = await measure_time(5, 10)
    print(avg_time)  # Print just the average time

asyncio.run(main())
