def check_sorted(L):
    """
    Uses looping to check whether a list is sorted or not (could be increasing or decreasing).
    Examples:
    >>> check_sorted([3, 6, 48, 24, 51, 262, 119])
    False
    >>> check_sorted([748, 623, 424, 414, 74, 2])
    True
    >>> check_sorted([1, 2, 3])
    True
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    for i in range(len(L)-2):
        if (L[i] > L[i+1]) != (L[i+1] > L[i+2]):
            return False
    return True


def longest_sorted(L):
    """
    Uses looping to return the longest sorted sequence in a list (ascending).
    Examples:
    >>> longest_sorted([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 13, 15, 3, 11, 7, 5])
    [1, 9, 13, 15]
    >>> longest_sorted([25, 72, 31, 32, 8, 20, 38, 43, 85, 39, 33, 40, 98, 37, 14])
    [8, 20, 38, 43, 85]
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW THIS
    all_sequence = []

    for i in range(len(L)):
        tem_seq = []
        for j in range(i,len(L)):
            if len(tem_seq) == 0:
                tem_seq.append(L[j])
            else:
                if L[j] > tem_seq[-1]:
                    tem_seq.append(L[j])
                else:
                    break
        all_sequence.append(tem_seq)
        
    return sorted(all_sequence,key=len)[-1]