## Finding the Square Root of an Integer

For the finding the square root of an integer, I used binary search algorithm because the square of interger increases monotonically as increases. The square of the mid point is chosen to compare with the target integer, and search in a smaller range after determing whether this mid point needs to be smaller or larger.

Time Complexity: O(log(N)), where N is the integer  
Space complexity: O(1), only constant number of variables are required.
