#!/usr/bin/env python3

from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list where each item in the tuple lst is repeated factor times.

    Parameters:
    lst (Tuple): A tuple of elements.
    factor (int): The number of times to repeat each item.

    Returns:
    List: A list with each item repeated factor times.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
