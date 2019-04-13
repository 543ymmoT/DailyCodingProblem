"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from
the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def solution001(numbers_list, target):
    """
    We use hashset to keep numbers we have seen. Then we check if difference
    between target and number is in our hashset.
    
    Args:
        numbers_list (list): list of numbers
        target (int): a sum of numbers we look for
    
    Returns:
        bool: True if there is pair of numbers that add up to target
    """
    numbers_seen = set()
    for num in numbers_list:
        if target - num in numbers_seen:
            return True
        else:
            numbers_seen.add(num)
    return False
        

def main():
    a = [10, 15 ,3, 7]
    k = 17
    print(solution001(a, k))
    
    
if __name__ == '__main__':
    main()    
