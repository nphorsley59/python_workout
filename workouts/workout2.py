from typing import Sequence

def mysum(iterable: Sequence[int], start: int = 0) -> int:
    """Adds initial value, start, and items in an iterable.
    
    Args:
        iterable (Sequence[int]): Iterable of ints that will be summed left
            to right.
        start (int, optional): Value that items in iterable will be added to.
    
    Returns:
        sum (int): Sum of start and items in iterable.
    
    """
    
    sum = start
    
    for y in iterable:
        sum += y
    
    return sum;


mysum([1, 2, 3], 4)