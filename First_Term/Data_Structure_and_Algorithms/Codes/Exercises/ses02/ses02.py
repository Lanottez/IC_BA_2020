def sum_of_squares(x, y):
    """
    Returns the sum of squares of x and y

    Examples:
    >>> sum_of_squares(1, 2)
    5
    >>> sum_of_squares(100, 3)
    10009
    >>> sum_of_squares(-1, 0)
    1
    >>> x = sum_of_squares(2, 3)
    >>> x + 1
    14
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    return x^2+y^2 # REPLACE THIS LINE WITH YOUR CODE


def print_grade(mark, grade_high, grade_low):
    """
    Prints out 'distinction', 'pass', or 'fail' depending on mark

    If mark is at least grade_high, prints 'distinction'
    Else if mark is at least grade_low, prints 'pass'
    Else prints 'fail'
    
    Examples:
    >>> grade_high = 70 
    >>> grade_low = 50
    >>> print_grade(20, grade_high, grade_low)
    fail
    >>> print_grade(61, 70, 50)
    pass
    >>> print_grade(90, 80, 60)
    distinction
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    if mark >= grade_high:
        print("distinction")
    elif mark >= grade_low:
        print("pass")
    else: 
        print("fail")
