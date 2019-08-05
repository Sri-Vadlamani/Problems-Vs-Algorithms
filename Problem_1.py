# Returns floor of square root of x
def sqrt(x) :

    # Base cases
    if (x == 0 or x == 1) :
        return x

    # Do Binary Search for floor(sqrt(x))
    start = 1
    end = x
    while (start <= end) :
        mid = (start + end) // 2

        # If x is a perfect square
        if (mid*mid == x) :
            return mid

        # Since we need floor, we update
        # answer when mid*mid is smaller
        # than x, and move closer to sqrt(x)
        if (mid * mid < x) :
            start = mid + 1
            ans = mid

        else :

            # If mid*mid is greater than x
            end = mid-1

    return ans

print ("Pass" if  (3 == sqrt(9)) else "Fail")  #pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")  #pass  (edge case)
print ("Pass" if  (4 == sqrt(16)) else "Fail") #pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")  #pass
print ("Pass" if  (5.196 == sqrt(27)) else "Fail") #fail (edge case)
print ("Pass" if  (5 == sqrt(27)) else "Fail")  #pass
