#!/usr/bin/env python3

from typing import List, Tuple, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Returns a list where each item in the tuple lst is repeated factor times.

    Parameters:
    lst (Tuple[int, ...]): A tuple of integers.
    factor (int): The number of times to repeat each item.

    Returns:
    List[int]: A list with each item repeated factor times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
