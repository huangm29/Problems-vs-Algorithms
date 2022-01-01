def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    #Edge case
    if len(input_list) < 2:
        return None
    # quick sort
    quicksort(input_list)
    first = 0
    second = 0
    first_order = 1
    second_order = 1
    for i in range(0,len(input_list),2):
        first += input_list[i] * first_order
        first_order *= 10
    for i in range(1,len(input_list),2):
        second += input_list[i] * second_order
        second_order *= 10
    return [first, second]


def sort_a_little_bit(items, begin_index, end_index):    
    left_index = begin_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1
    
    return pivot_index

def sort_all(items, begin_index, end_index):
    if end_index <= begin_index:
        return
    
    pivot_index = sort_a_little_bit(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)
    
def quicksort(items):
    sort_all(items, 0, len(items) - 1)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print(rearrange_digits([1, 2, 3, 4, 5]))
#[531, 42]

print(rearrange_digits([4, 6, 2, 9, 5, 8]))
#[852, 964]

print(rearrange_digits([])) #Edge case
#None

print(rearrange_digits([1])) #Edge Case
#None

print(rearrange_digits([1, 2]))
#[1, 2]