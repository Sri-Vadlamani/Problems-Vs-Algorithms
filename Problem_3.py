def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1
    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]
    # return the ordered, merged list
    return merged

def sorted(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items
    # Otherwise, find the midpoint and split the list
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    # Call mergesort recursively with the left and right half
    left = sorted(left)
    right = sorted(right)
    # Merge our two halves and return
    return merge(left, right)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # sorted the elements
    input_list = sorted(input_list)
    num1, num2 = 0, 0
    for i in range(len(input_list)):
        if i % 2 == 0:
            num1 = num1 * 10 + input_list[i]
        else:
            num2 = num2 * 10 + input_list[i]
    return [num2, num1]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])  #pass
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)                     #pass [edge case]
test_function([[1,1,1,1,1], [111, 11]])      #pass
test_function([[0], [-1, -1]])               #fail
test_function([[0, 0], [0, 0]])             #pass  [edge case]
test_function([[0, 0, 1, 1, 5, 5], [510, 510]])   #pass
