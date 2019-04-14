"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.

-----------

Some other thoughts:
A naive method to solve this problem is to search all positive integers, starting
from 1 in the given array. We may have to search at most n+1 numbers in the given
array. So this solution takes O(n^2) in worst case.

We can use sorting to solve it in lesser time complexity. We can sort the array
in O(nLogn) time. Once the array is sorted, then all we need to do is a linear
scan of the array. So this approach takes O(nLogn + n) time which is O(nLogn).

We can also use hashing. We can build a hash table of all positive elements in
the given array. Once the hash table is built. We can look in the hash table for
all positive integers, starting from 1. As soon as we find a number which is not
there in hash table, we return it. This approach may take O(n) time on average,
but it requires O(n) extra space.
"""

def solution004(numbers_list):
    numbers_list = [x for x in numbers_list if x > 0]
    
    for num in numbers_list:
        current_num = abs(num)
        if (current_num - 1) < len(numbers_list):
            numbers_list[current_num-1] *= -1
#            print(f"Changed list: {numbers_list}")
    
#    print(f"Enter list: {numbers_list}")
    for idx, num in enumerate(numbers_list):
        if num > 0:
            return idx+1
        
    return len(numbers_list) + 1


assert solution004([3, 4, -1, 1]) == 2
assert solution004([1, 2, 0]) == 3
assert solution004([1]) == 2
assert solution004([-3, -5, -8, 7, 1, 2, 3, 5, 6, 9, 13, 4, 8, 19, 10]) == 11
assert solution004([]) == 1
assert solution004([-1, -2, -3, -5]) == 1

