def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) <= 0:
        return (None, None)
    return get_min_max_recursive(ints, 0, len(ints)-1)

def get_min_max_recursive(ints, start, stop):
    if start == stop:
        return (ints[start], ints[start])
    if start + 1 == stop:
        return (min(ints[start], ints[stop]), max(ints[start], ints[stop]))
    else:
        mid = (start + stop)//2
        min_left, max_left = get_min_max_recursive(ints, start, mid)
        min_right, max_right = get_min_max_recursive(ints, mid+1, stop)
        return (min(min_left, min_right), max(max_left, max_right))

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print(get_min_max(l))
#(0, 9)

print(get_min_max([3,3,3,3]))
#(3,3)

print(get_min_max([0])) #Edge case
#(0, 0) 

print(get_min_max([]))  #Edge case
#(None, None)