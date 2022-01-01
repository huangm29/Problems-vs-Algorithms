##Max and Min in a Unsorted Array

In this problem, I used divide and conquer strategy for finding max and min in a single traverse. The array is separted into two halves, then the max and min of each half is calculated, and the max and min of entire array is determined by comparing max and min from two halves. This should be faster by the algorithm of doing single traverse of the array and comparing each element with the saved max and min,  beacuse we can eliminate some duplicate comparisons. 

Time complexity:O(N), where N is the length of araray

Space complexity: O(1), no need to save extra elements from the array.