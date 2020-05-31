def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    length = len(ints)
    min_value = None
    max_value = None
    index = 0
    
    while index < length:
        if min_value is None or ints[index] < min_value:
            min_value = ints[index]
            
        if max_value is None or ints[index] > max_value:
            max_value = ints[index]
        index += 1
    return (min_value, max_value)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("``````````````````````random test cases````````````````````````````````")
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((0, 999) != get_min_max(l)) else "Fail")
print ("Pass" if ((-9, 0) != get_min_max(l)) else "Fail")

print("``````````````````````manual test cases````````````````````````````````")
print(get_min_max([1, 1, 1, 1, 1])) #(1,1)
print(get_min_max([1, 1, 100, 1, -1])) #(-1,100)
print(get_min_max([1, 2, 4, 5, 100, 2, -1, 5, 20]))  #(-1,100) 
print(get_min_max([10, 5, 6, 0, 12, 8]))  # (0, 12)
print(get_min_max([5, 6, 12, 80, 8]))  # (5, 80)
print(get_min_max([1, 22, 5, 6, 0, 12, 8, 9, 4, 4, 2, 20]))  # (0, 22)
