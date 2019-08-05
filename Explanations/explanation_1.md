### Description:
The square root of the integer without using any Python library. Implemented the code to print floor value of the square root.

### Algorithm:
Naive solution is to consider all positive numbers starting from 1, and find the first number i for which i*i is greater than the given number x. the i-1 would be the floor of square root of X. Then the time complexity is O(vx).

However, the algorithm implemented for this problem is Binary search algorithm which would improve the above time complexity.

### Implementation process:
Algorithm:
1. Start with ‘start’ = 0, end = ‘x’,
2. Do following while ‘start’ is smaller than or equal to ‘end’.
      * Compute ‘mid’ as (start + end)/2
      * compare mid*mid with x.
      * If x is equal to mid*mid, return mid.
      * If x is greater, do binary search between mid+1 and end. In this case, ans is also updated.
      * If x is smaller, do binary search between start and mid

### Time Complexity:
The time required to compute the integral part is O(log(number)) and constant i.e, = precision for computing the fractional part. Therefore, overall time complexity is O(log(number) + precision) which is approximately equal to O(log(number)).

### Space Complexity:
The space complexity is O(1)
