def get_min_max(ints):

  """Return a tuple(min, max) out of list of unsorted integers.
  Args:
     ints(list): list of integers containing one or more integers
  """
  if not ints:
      return
  max = ints[0]
  min = ints[0]


  for i in ints:
      if i > max:
          max = i
      if i < min:
          min = i
  return (min, max)



## Example Test Case of Ten Integers
import random

l = [int(i) for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")  #pass
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")   #pass
print ("Pass" if (None == get_min_max([])) else "Fail")  #pass
