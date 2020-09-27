def middle_of_three(a, b, c):
    """
    Returns the middle one of three numbers a,b,c
    Examples:
    >>> middle_of_three(5, 3, 4)
    4
    >>> middle_of_three(1, 1, 2)
    1
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    list_abc = [a,b,c]
    max_one = max(list_abc)
    min_one = min(list_abc)
    list_abc.remove(max_one)
    list_abc.remove(min_one)
    return list_abc[0]


def sum_up_to(n):
    """
    Returns the sum of integers from 1 to n
    
    Examples:
    >>> sum_up_to(1)
    1
    >>> sum_up_to(5)
    15
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    sum_number = 0
    for i in range(1,n+1):
        sum_number = sum_number+i

    return sum_number


def square_root_heron(x, epsilon=0.01):
    """
    Find square root using Heron's algorithm

    Parameters:
    x: integer or float
    epsilon: desired precision,
        default value epsilon = 0.01 if not specified

    Returns:
    the square root value, rounded to two decimals
    the number of iterations of the algorithm run

    Example use:
    >>> y, c = square_root_heron(20)
    >>> print(y, c)
    4.47 4
    """
    # DON'T CHANGE ANYTHING ABOVE
    # UPDATE CODE BELOW
    
    guess = x/2 # Make initial guess
    iteration = 0
    # Loop until squared value of guess is close to x
    while abs(guess*guess - x) >= epsilon:
        guess = (guess + x/guess)/2 # Update guess using Heron's formula
        iteration = iteration + 1
    return round(guess, 2), iteration # replace the dots with the final number of iterations


def square_root_bisection(x, epsilon=0.01):
    """
    Find square root using bisection search

    Parameters:
    x: integer or float
    epsilon: desired precision,
        default value epsilon = 0.01 if not specified

    Returns:
    the square root value, rounded to two decimals
    the number of iterations of the algorithm run

    Example use:
    >>> y, c = square_root_bisection(20)
    >>> print(y, c)
    4.47 9
    """
    # DON'T CHANGE ANYTHING ABOVE
    # UPDATE CODE BELOW
    iteration = 0
    low = 0.0
    high = max(1.0, x) # Why are we doing this? What would happen for x=0.5?
    guess = (low + high)/2 # First guess at midpoint of low and high
    while abs(guess*guess - x) >= epsilon:
        if guess*guess < x:
            low = guess # update low
        else:
            high = guess # update high
        guess = (low + high)/2 # new guess at midpoint of low and high
        iteration = iteration+1
    return round(guess,2),iteration


