import pdb

def find_min_index(A, k):
    """
    Finds the index of the smallest element in the list A from index k onwards
    
    Parameters:
        A (list)
        k: index from which start search
        
    Example use:
    >>> find_min_index([1, 2, 5, -1], 0)
    3
    >>> find_min_index([1, 1, 1, 5, 9], 2)
    2
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    mv = float('inf')
    for i in range(k,len(A)):
        if A[i] < mv:
            mv = A[i]
    return A.index(mv,k)
        
def selection_sort(M):
    """
    Sorts the list M using selection sort
    
    Parameters:
        M is a list containing numbers
    
    Returns sorted copy of M.
    
    Uses find_min_index to find index with lowest value
    
    Examples:
    >>> selection_sort([3, 6, 8, 2, 78, 1, 23, 45, 9])
    [1, 2, 3, 6, 8, 9, 23, 45, 78]
    >>> selection_sort([1, 13, -23, 2.7, -3, 5, 7.5])
    [-23, -3, 1, 2.7, 5, 7.5, 13]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    L = M[:] # create a copy of the list to also preserve original list
    n = len(L)
    for index in range(n):
        min_index = find_min_index(L, index)
        L[min_index],L[index] = L[index],L[min_index]
    return L    


def sort_by_key(country_list, key_function):
    """
    Sorts a list of tuples by specified key function, in descending order
    
    Parameters:
        list of tuples; for example: each tuple is (country_name, unemployment, GDP_growth_rate)
        key_function, to be used for sorting
    	
    Returns:
        sorted list of tuples
    Examples: # these are made-up numbers!
    >>> sort_by_key([\
    		('USA', 4.4, 2.3),\
    		('Japan', 3.2, 2),\
    		('Germany', 4.0, 1),\
    		('China', 4.1, 9),\
    		('Thailand', 2, 1.2),\
    		('Argentina', 9, 2.3),\
    		('Brazil', 10, 1.7)], get_unemployment)
    [('Brazil', 10, 1.7), ('Argentina', 9, 2.3), ('USA', 4.4, 2.3), ('China', 4.1, 9), ('Germany', 4.0, 1), ('Japan', 3.2, 2), ('Thailand', 2, 1.2)]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE

        
    def find_max_index_tuple(A, k):
        mv_unemployment = ('',float('-inf'),'')
        for tuple_single in A[k:]:
            if get_unemployment(tuple_single) > get_unemployment(mv_unemployment):
                mv_unemployment = tuple_single
        return A.index(mv_unemployment, k)

    L = country_list[:] # create a copy of the list to also preserve original list
    n = len(L)
    for index in range(n):
        min_index = find_max_index_tuple(L, index)
        L[min_index],L[index] = L[index],L[min_index]
    return L    

def get_unemployment(x):
    """
    Returns the level of unemployment from the parameter x (tuple)
    Parameter: x - tuple (country_name, unemployment, GDP_growth_rate)
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE HERE
    return x[1]




    
	