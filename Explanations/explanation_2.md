### Description:
The goal is to search in a Rotated Sorted Array

### Data structure:
Searching is done by Binary Search. We can search an element in one pass of Binary Search.

### Implementation process:
1.  Find middle point mid = (l + h)/2
2.  If target number is present at middle point, return mid.
3. Else If input_list[l..mid] is sorted
    a) If key to be searched lies in range from input_list[l]
       to input_list[mid], recur for input_list[l..mid].
    b) Else recur for input_list[mid+1..h]
4.  Else (input_list[mid+1..h] must be sorted)
    * If target number to be searched lies in range from input_list[mid+1]
       to input_list[h], recur for input_list[mid+1..h].
    * Else recur for input_list[l..mid]

### Time Complexity:
Time complexity of the searching is O(logn).
We can easily know which half is sorted by comparing start and end element of each half.

Once we find which half is sorted we can see if the key is present in that half - simple comparison with the extremes.

If the key is present in that half we recursively call the function on that half
else we recursively call our search on the other half.

We are discarding one half of the array in each call which makes this algorithm O(logN).

### Time Complexity:
Space complexity is O(1).
