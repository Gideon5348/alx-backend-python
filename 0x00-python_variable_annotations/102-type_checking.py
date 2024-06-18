#!/usr/bin/env python3

"""
102-type_checking.py

This module provides a function to zoom into array by repeating its elements.
"""

from typing import List


def zoom_array(lst: List, factor: int = 2) -> List:
    """
    Returns a list where each item in the list lst is repeated factor times.

    Parameters:
    lst (List): A list of elements.
    factor (int): The number of times to repeat each item.

    Returns:
    List: A list with each item repeated factor times.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
