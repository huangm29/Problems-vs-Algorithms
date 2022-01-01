##Search in a Rotated Sorted Array

For this search problem, I used divide and conquer here where the list is divided into two halfs. Half of it will still be a rotated array and the other half is a monotonic one. Separtate search can be performed then after determing whether the target element is in either half. Doing this recursively would allow me to do the search in the entire rotated sort array. 

Time Complexity: O(log(N)), where N is the length of arrray. Typical binary O(log n). 

Space complexity: O(1), only the indexes are used. 
