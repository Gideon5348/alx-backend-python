#!/usr/bin/env python3
"""
This module provides a coroutine that collects random numbers using
an asynchronous comprehension.
"""

from typing import List
from importlib import import_module

# Import the async_generator function from the previous task
async_generator = import_module('async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator
    using an async comprehension and returns the list of numbers.
    """
    return [number async for number in async_generator()]
