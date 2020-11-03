def recursive_fibonacci(n):
    """
    Assumes that n is an int >= 0
        returns Fibonacci of n
    
    Example use:
    >>> recursive_fibonacci(2)
    1
    >>> recursive_fibonacci(5)
    5
    >>> recursive_fibonacci(8)
    21
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)
    


def merge_sort(L):
    """
    Sort the input list using the merge sort algorithm.
    
    Parameters:
        L is an unsorted list
        
    Returns:
        L sorted in increasing order
    
    Examples:
    >>> merge_sort([3, 6, 8, 2, 78, 1, 23, 45, 9])
    [1, 2, 3, 6, 8, 9, 23, 45, 78]
    >>> merge_sort([1, 13, -23, 2.7, -3, 5, 7.5])
    [-23, -3, 1, 2.7, 5, 7.5, 13]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    if len(L) < 2: # Base case - list is max one item, so sorted
        return L[:] # Return (copy of) the entire list
    else: # General case: split and sort each half, then merge
        return merge(merge_sort(L[:len(L)//2]),merge_sort(L[len(L)//2:]))

def merge(left, right):
    """
    Merge two sorted lists into one
    
    Parameters: 
        left and right are sorted lists
       
    Returns a single sorted list.
    
    Example use:
    >>> left = [1, 5, 6]
    >>> right = [2, 3, 4]
    >>> merge(left, right)
    [1, 2, 3, 4, 5, 6]
    """
    # YOUR CODE BELOW
    # DON'T CHANGE ANYTHING ABOVE
    # This is one possible approach:
    result = [] # the result of merging
    while left != [] and right != []:
        result = result + [left.pop(0)] if left[0] < right[0] else result + [right.pop(0)]
    result = result + right if left == [] else result + left
    return result