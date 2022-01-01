def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    #special case
    if (number < 0):
        print("Negative number!")
        return None

    if (number == 0 or number == 1) :
        return number

    start = 0
    stop = number
    mid = (start + stop) // 2

    while(start <= stop):
        if (mid * mid == number):
            return mid
        elif (mid * mid < number):
            start = mid + 1
        else:
            stop = mid - 1
        mid = (start + stop) // 2
    return mid

print(sqrt(9))
# 3

print(sqrt(3))
# 1
         
print(sqrt(0)) #Edge case
# 0

print(sqrt(-1)) #Edge case
# Negative number!
# None