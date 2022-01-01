def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) < 1:
        return -1
    else:
        return rotated_array_search_recursive(input_list, 0, len(input_list)-1, number)
        
def rotated_array_search_recursive(input_list, start, end, number):
    if start == end:
        if input_list[start] == number:
            return start
        else:
            return -1
    mid = (start + end)//2
    if input_list[mid] == number:
        return mid
    elif input_list[mid] < number:
        if input_list[end] < number:
            return rotated_array_search_recursive(input_list, start, mid - 1, number)
        elif input_list[end] > number:
            return binary_search_recursive(input_list, mid+1, end, number)
        else:
            return end
    else:
        if input_list[start] < number:
            return binary_search_recursive(input_list, start, mid-1, number)
        elif input_list[start] > number: 
            return rotated_array_search_recursive(input_list, mid+1, end, number)
        else:
            return start
    
def binary_search_recursive(input_list, start, end, number):
    if start == end:
        if input_list[start] == number:
            return start
        else:
            return -1
    mid = (start+end) //2
    if input_list[mid] == number:
        return mid
    elif input_list[mid] < number:
        return binary_search_recursive(input_list, mid + 1, end, number)
    else:
        return binary_search_recursive(input_list, start, mid -1, number)  

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
#0 

print(rotated_array_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))
#5 

print(rotated_array_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)) 
#-1

print(rotated_array_search([], 0)) #edge case
#-1

print(rotated_array_search([0], 0)) #edge case
#0