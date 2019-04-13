"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the original
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output
would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def solution002(numbers_list):
    """
    No division solution. We need to create two dicts to store product to
    the left and to the right of the index. The new list is created by 
    multiplying results from 'left dict and 'right dict' for given index i.
    
    Args:
        numbers_list (list): list of numbers
        
    Returns:
        new_list (list): new list
    """
    left_mult_dict = {}
    right_mult_dict = {}
    
    new_list = [None] * len(numbers_list)
    
    left_mult_dict[-1] = 1
    for i in range(len(numbers_list) - 1):
        left_mult_dict[i] = numbers_list[i] * left_mult_dict[i - 1]
    
    right_mult_dict[len(numbers_list)] = 1
    for j in reversed(range(len(numbers_list))[1: ]):
        right_mult_dict[j] = numbers_list[j] * right_mult_dict[j + 1]
        
    for i in range(len(numbers_list)):
        new_list[i] = left_mult_dict[i - 1] * right_mult_dict[i + 1]
    
    return new_list
    
    
def main():
    numbers_list = [1, 2, 3, 4, 5]
#    numbers_list = [3, 2, 1, 5, 7, 8]
#    numbers_list = [-1, -4, 9, 8, 6]
#    numbers_list = []
    print(solution002(numbers_list))
    
    
if __name__ == '__main__':
    main()    
