#!/usr/bin/env python3
"""Module for async comprehension task."""

from typing import List
from importlib import import_module

# Import the async_generator function from the previous task
async_generator = import_module('async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using an async comprehension over async_generator."""
    return [number async for number in async_generator()]
