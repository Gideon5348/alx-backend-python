#!/usr/bin/env python3
"""
0-basic_async_syntax.py

This module contains an asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds
    and return the delay.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
