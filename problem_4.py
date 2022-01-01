def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    left_index = 0
    right_index = len(input_list)-1
    index = 0 
    while index <= right_index:
        if input_list[index] == 0:
            input_list[index] = input_list[left_index]
            input_list[left_index] = 0
            index += 1
            left_index += 1
        elif input_list[index] == 2:
            input_list[index] = input_list[right_index]
            input_list[right_index] = 2
            right_index -= 1
        else:
            index += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
#[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
#[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

print(sort_012([])) #Edge case
#[]

print(sort_012([0])) #Edge case
#[0]