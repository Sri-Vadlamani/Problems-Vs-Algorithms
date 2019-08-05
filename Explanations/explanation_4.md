### Description:
Dutch National Flag Problem: Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

### Data structure:
Linear-time partition routine is used to sort the array that separated the values into three groups.
* values less than the pivot
* values equal to the pivot
* values greater than pivot

Here we consider 1 as pivot.

### Implementation process
The proposed code does not performs unnecessary swaps for inputs like 0 0 0 0 1 1 1 2 2 2 2 2 :lo=4 and mid=7 and hi=11.
The code avoids first 7 exchanged with 11 and 'hi' become 10 and mid is still pointing to 7. again the same operation is done till mid <= hi, which is really not required. So the swap function is changed to do a check that the values being swapped are same or not, if not same, then only swap values.

### Time Complexity:
The code traverses through the length of the array and compare the numbers and does swapping when necessary.
Hence the time complexity O(length of the array):O(n)

### Space Complexity:
Space complexity is O(1).
