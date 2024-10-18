#!/usr/bin/env python3

"""A module"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """A function that creates an async funtion"""
    return asyncio.create_task(wait_random(max_delay))
