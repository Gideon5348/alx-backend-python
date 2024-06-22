#!/usr/bin/env python3
"""
Module to measure the runtime of executing async_comprehension in parallel.
"""

import asyncio
import time
from importlib import import_module as using

# Import async_comprehension function from 1-async_comprehension module
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing
    async_comprehension four times in parallel.
    """
    start_time = time.perf_counter()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()
    return end_time - start_time
