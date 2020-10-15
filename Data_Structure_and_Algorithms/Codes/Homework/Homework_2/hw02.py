"""

Homework 2

"""
import pdb
def moving_average(prices, n):
    """
    Calculates n-period moving average of a list of floats/integers.

    Parameters:
        prices: list of values (ordered in time),
        n: integer moving-average parameter

    Returns:
        list with None for the first n-1 values in prices and the appropriate moving average for the rest

    Example use:
    >>> ma = moving_average([2,3,4,5,8,5,4,3,2,1], 3)
    >>> [round(m, 2) if m is not None else None for m in ma]
    [None, None, 3.0, 4.0, 5.67, 6.0, 5.67, 4.0, 3.0, 2.0]
    >>> moving_average([2,3,4,5,8,5,4,3,2,1], 2)
    [None, 2.5, 3.5, 4.5, 6.5, 6.5, 4.5, 3.5, 2.5, 1.5]
    """
    # Your code here. Don't change anything above.
    ma = []
    for i in range(n-1):
        ma.append(None)
    for i in range(len(prices)-n+1):
        ma.append(round((sum(prices[i:i+n])/n),2))
    return ma
        

def cross_overs(prices1, prices2):
    """ 
    Identify cross-over indices for two equal-length lists of prices (here: moving averages)

    Parameters:
        prices1, prices2: lists of prices (ordered by time)

    Returns:
        list of crossover points

    Each item in the returned list is a list [time_index, higher_index], where:
        - time_index is the crossover time index (when it happends
        - higher_index indicates which price becomes higher at timeIndex: either 1 for first list or 2 for second list
    
    There are no crossovers before both price lists have values that are not None.
    You can start making comparisons from the point at which both have number values.
    
    Example use:
    >>> p1 = [1, 2, 4, 5]
    >>> p2 = [0, 2.5, 5, 3]
    >>> cross_overs(p1, p2)
    [[1, 2], [3, 1]]
    >>> p1 = [None, 2.5, 3.5, 4.5, 4.5, 3.5, 2.5, 1.5, 3.5, 3.5]
    >>> p2 = [None, None, 3.0, 4.0, 4.333333333333333, 4.0, 3.0, 2.0, 3.0, 2.6666666666666665]
    >>> cross_overs(p1, p2)
    [[5, 2], [8, 1]]
    >>> l3 = [1,22,5,14,8,20,4]
    >>> l4 = [38,21,4,15,10,17,6]
    >>> cross_overs(l3, l4)
    [[1, 1], [3, 2], [5, 1], [6, 2]]
    """
    # Your code here. Don't change anything above.
    crossovers = []
    for index in range(1,len(prices1)):
        if prices1[index-1] and prices2[index-1]:
            if prices1[index-1] < prices2[index-1] and prices1[index] > prices2[index]:
                crossovers.append([index,1])
            elif prices1[index-1] > prices2[index-1] and prices1[index] < prices2[index]:
                crossovers.append([index,2])
    return crossovers
                
            
    

def make_trades(starting_cash, prices, crossovers):
    """
    Given an initial cash position, use a list of crossovers to make trades

    Parameters:
        starting_cash: initial cash position
        prices: list of prices (ordered by time)
        crossovers: list of crossover points on the prices

    Returns:
        list containing current value of trading position (either in stock value or cash) at each time index
    
    Assume each item crossovers[i] is a list [time_index, buy_index]
    Assume that buy_index = 1 means "buy"
    Assume that buy_index = 2 means "sell"

    We buy stock at any time_index where crossover's buy_index indicates 1, and sell at 2.
    In more detail:
        - We want to buy at time_index whenever buy_index = 1 and we currently hold a cash position
            - We buy at the stock price at time_index. We buy with the entire cash position we have and only hold stock
        - We want to sell at time_index when buy_index = 2 and we hold a stock position
            - We sell at the stock price at time_index. We sell our entire stock position and will only hold cash

    Whenever we trade, we buy with our entire cash position, or sell our entire stock position.
    We will therefore always hold either stock or cash, but never both.
    
    Assume we can hold fractional stock quantities, and there are no transaction fees.

    Example use:
    # In the first example, We start with cash 1.0.
    # We hold cash until we buy at index 1 at the price 4. We then hold 0.25 shares. 
    # After that, our portfolio is in stock, so its value fluctuates with the stock price.
    # As the stock price goes from 4 to 6, our portfolio value goes from 1.0 to 1.5.
    # This goes on until we sell at index 3 at the price 5. 
    # Then we hold cash again and the value of the portfolio does not change as it is in cash.
    >>> starting_cash = 1.0
    >>> prices = [2,4,6,5,1]
    >>> cos = [[1, 1], [3, 2]] # not real crossovers, just to illustrate portfolio value when trading
    >>> values = make_trades(starting_cash, prices, cos)
    >>> values 
    [1.0, 1.0, 1.5, 1.25, 1.25]
    >>> starting_cash = 1000.0
    >>> prices = [2,3,4,5,4,3,2,1,6,1,5,7,8,10,7,9]
    >>> cos = [[5, 2], [8, 1], [10, 2], [11, 1], [15, 2]]
    >>> values = make_trades(starting_cash, prices, cos)
    >>> [round(v, 2) for v in values] # round every value of the returned list using list comprehension
    [1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 1000.0, 166.67, 833.33, 833.33, 952.38, 1190.48, 833.33, 1071.43]
    >>> prices =[38,21,20,13,7,14,22,23,27,23,44,26,48,32,48,60,70,40,34,35,33]
    >>> crossovers = [[7, 1], [19, 2]]
    >>> money = 100.0
    >>> values = make_trades(money, prices, crossovers)
    >>> [round(v, 2) for v in values] # round every value of the returned list using list comprehension
    [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 117.39, 100.0, 191.3, 113.04, 208.7, 139.13, 208.7, 260.87, 304.35, 173.91, 147.83, 152.17, 152.17]
    >>> l2 = [39,22,5,14,8,15,23,27,23,44,26,48,32,48,13,34,15,34,35]
    >>> c2 = [[4, 1], [5, 2], [6, 1], [11, 2], [12, 1], [13, 2], [16, 1], [17, 2], [18, 1]]
    >>> values = make_trades(10.0, l2, c2)
    >>> [round(v, 3) for v in values] # round every value of the returned list using list comprehension
    [10.0, 10.0, 10.0, 10.0, 10.0, 18.75, 18.75, 22.011, 18.75, 35.87, 21.196, 39.13, 39.13, 58.696, 58.696, 58.696, 58.696, 133.043, 133.043]
    """
    # Your code here. Don't change anything above.
    # Note: the rounding in the examples happens *after* the function call. Your function should not round the results.
    current_value = []  # value of portfolio
    holding_shares = 0
    cash_position = 1
    current_cash = starting_cash
    
    corssover_dict = {}    
    for crossover in crossovers:
        corssover_dict[crossover[0]] = crossover[1]
        
    for index in range(len(prices)):
        current_price = prices[index]
        if cash_position: # 目前持有现金
            if index in corssover_dict and corssover_dict[index] == 1: #买入
                """
                修改cash position
                更新holding_shares
                重复current_value
                修改current_cash
                """
                cash_position = 0
                holding_shares = current_cash / current_price
                current_value.append(current_cash)
                current_cash = 0
            elif index in corssover_dict and corssover_dict[index] == 2: # 建议卖出
                """
                cash position不变
                holding_shares不变
                重复current_value
                current_cash不变
                """
                current_value.append(current_cash)
            else:
                """
                更新current_value
                """
                current_value.append(current_cash)
        else: # 目前持有股票
            if index in corssover_dict and corssover_dict[index] == 1: # 建议买入
                """
                cash_positon不变
                holding_shares不变
                更新current_value
                current_cash不变
                """
                current_value.append(holding_shares*current_price)
            elif index in corssover_dict and corssover_dict[index] == 2: #建议卖出
                """
                修改cash position  
                修改holding_shares
                更新current_value
                修改current_cash
                """
                cash_position = 1
                current_value.append(holding_shares*current_price)
                current_cash = holding_shares*current_price
                holding_shares = 0
            else: 
                """
                更新current_value
                """
                current_value.append(holding_shares*current_price)
    return current_value
    
def palindrome(s, k):
    """
    Find highest-value palindrome from s with max k digit changes.
    
    Parameters:
        s - an integer in string format
        k - number of changes
        
    Returns:
        highest-value palindrome number in string format; 
        if creating a palindrome is not possible, returns the string 'Not possible.'
    
    Example use:
    >>> palindrome('1921', 2)
    '1991'
    >>> palindrome('1921', 3)
    '9999'
    >>> palindrome('11122', 1)
    'Not possible.'
    >>> palindrome('11119111', 4)
    '91199119'
    """    
    def is_odd(num):
        if (num % 2) == 0:
            return False
        else:
            return True
    
    def return_change_required(s,change_total):
        """
        return the modified string which is palindrome
        return the times required to change the digit, so L is palindrome
        """
        change_required = 0
        for index in range(len(s)//2):
            if s[index] != s[-1-index]:
                change_required += 1
                s[index] = s[-1-index] = max(s[index],s[-1-index])
                
        change_left = change_total - change_required
        return s,change_left

    string_list = list(s)
    s_modified,change_left = return_change_required(string_list,k)

    str_output = ''
    
    if change_left < 0:
        return 'Not possible.'
    elif change_left == 1:
        if is_odd(len(s)):
            s_modified[len(s)//2] = '9'
            return str_output.join(s_modified)
        else:
            mid_1 = s[len(s)//2]
            mid_2 = s[len(s)//2-1]
            if max(mid_1,mid_2) != '9':
                return str_output.join(s_modified)
            else:
                if min(mid_1,mid_2) == mid_2:
                    s_modified[len(s)//2-1] = '9'
                else:
                    s_modified[len(s)//2] = '9'
                return str_output.join(s_modified)
          
    starting_index = 0
    ending_index = len(s) - 1
    while (starting_index <= ending_index): 
        if (starting_index == ending_index): 
            if (change_left > 0): 
                s_modified[l] = '9'
        if (s_modified[l] < '9'): 
            if (change_left >= 2 and palin[l] == strr[l] and palin[r] == strr[r]): 
                change_left -= 1
                s_modified[l] = palin[r] = '9'
            elif (k >= 1 and (palin[l] != strr[l] or palin[r] != strr[r])): 
                change_left -= 1
                palin[l] = palin[r] = '9'
  
        l += 1
        r -= 1
  
    return palin
    return str_output.join(s_modified)

    

    
def reverse_engineer(seq):
    """
    Reverse engineer an input sequence
    
    Parameters:
        seq - list of strings
    
    Returns:
        list of values corresponding to each letter present in the sequences (smallest possible values)
        (in alphabetical order)
    
    Example use
    >>> reverse_engineer(["a", "ab", "c", "a", "ab", "ac"])
    [2, 4, 5]
    >>> reverse_engineer(["b", "bc", "ab", "bc", "b", "abc", "b"])
    [3, 1, 2]
    >>> reverse_engineer(["a", "b", "d", "c", "a", "ab"])
    [6, 9, 11, 10]
    """
    # Your code here.
    def return_letter_occurrence(seq):
        def return_letter_set(seq):
            letters_output = []
            letters_dict = {}
            for letters in seq:
                for letter in letters:
                    if letter not in letters_output:
                        letters_output.append(letter)
            for index in range(len(letters_output)):
                letters_dict[letters_output[index]] = index+1
            letters_dict_for_relationship = letters_dict.copy()
            for keys in letters_dict_for_relationship:
                letters_dict_for_relationship[keys] = {}
            return [letters_output,letters_dict,letters_dict_for_relationship]
        def find_the_index_of_smallest_element(letter_list,letters_output):
            for letter in letters_output:
                if letter in letter_list:
                    return letter_list.index(letter)
        [letters_output,letters_dict,letters_dict_for_relationship] = return_letter_set(seq)
        def update_occurrence_recorder_letters_dict_for_relationship(letters_output,letters_dict,letters_dict_for_relationship):
            occurrence_recorder = {}
            for letter in letters_output:
                occurrence_recorder[letter] = 0
            occurrence_list_collection = []
            for letters_index in range(len(seq)):
                occurrence_list = {}
                letters = seq[letters_index]
                for letter in letters:
                    occurrence_recorder[letter] += 1
                    occurrence_list[letter] = occurrence_recorder[letter]
                if len(letters) > 1:
                    letter_list = list(letters)
                    smallest_element = letter_list.pop(find_the_index_of_smallest_element(letter_list,letters_output))
                    for relationship in letter_list:
                        letters_dict_for_relationship[smallest_element][relationship] = occurrence_recorder[relationship] / occurrence_recorder[smallest_element]
                occurrence_list_collection.append(occurrence_list.copy())
            def complete_letters_dict_for_relationship(letters_dict_for_relationship):        
                for keys in letters_dict_for_relationship:
                    out_key = keys
                    letter_dict_for_relationship = letters_dict_for_relationship[out_key]
                    for keys in letter_dict_for_relationship:
                        in_key = keys
                        letters_dict_for_relationship[in_key][out_key] = 1/letters_dict_for_relationship[out_key][in_key] 
            complete_letters_dict_for_relationship(letters_dict_for_relationship)   
            return occurrence_list_collection,letters_dict_for_relationship
        occurrence_list_collection,letters_dict_for_relationship = update_occurrence_recorder_letters_dict_for_relationship(letters_output,letters_dict,letters_dict_for_relationship)
        return occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship
    def return_one_key(input_dict):
        for keys in input_dict:
            return keys,input_dict[keys]
    def verify_relationship_and_update(occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship):
        def is_int(input_num):
            if max(input_num, round(input_num)) - min(input_num, round(input_num)) < 0.000001:
                return True
            return False
        def verify_relationship_and_update_inner(occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship):
            for letter in letters_output:
                relationships = letters_dict_for_relationship[letter]
                letters_modified = list(relationships.keys())
                for letter_modified in letters_modified:
                    value_modified = letters_dict[letter] / relationships[letter_modified]
                    if not is_int(value_modified):
                        letters_dict[letter] += 1
                        return False
                    else:
                        letters_dict[letter_modified] = round(value_modified)
            return True
        while True:
            if verify_relationship_and_update_inner(occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship):
                break
    occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship = return_letter_occurrence(seq)
    def verify_size_relationship(occurrence_list_collection,letters_dict):
        for index in range(1,len(occurrence_list_collection)):
            occurrence_list_n = occurrence_list_collection[index]
            occurrence_list_n_1 = occurrence_list_collection[index-1]
            letter,letter_occurrence = return_one_key(occurrence_list_n_1)
            for keys in occurrence_list_n:
                if occurrence_list_n[keys] * letters_dict[keys] <= letters_dict[letter] * letter_occurrence:
                    letters_dict[keys] += 1
                    verify_relationship_and_update(occurrence_list_collection,letters_dict,letters_output,letters_dict_for_relationship)
                    return False
        return True

    while True:
        if verify_size_relationship(occurrence_list_collection,letters_dict):
            return_list = []
            for letter in sorted(letters_output):
                return_list.append(round(letters_dict[letter]))
            return return_list
        print(letters_dict)

# Other testing cases:
           
def the_teaser(n,letter_set_sorted,letters_dict):
    output_letter = ''
    for letter in letter_set_sorted:
        if n % letters_dict[letter] == 0:
            output_letter += letter
    if output_letter:
        return output_letter
def teaser_looper(n,letter_set_sorted,letters_dict):
    outbook_list = []
    for i in range(1,n):
        ou = the_teaser(i,letter_set_sorted,letters_dict)
        if ou:
             outbook_list.append(ou) 
    return outbook_list

n=3000

letter_set_sorted = ['a','b','c','d','e','f','g','h','i','j','k']
letters_dict_2 = {'a':4,'b':5,'c':9,'d':121,'e':150,'f':1502,'g':2110,'h':2129,'i':2301,'j':2549,'k':2608}
seq5 = teaser_looper(n,letter_set_sorted,letters_dict_2)



letter_set_sorted = ['a','b','c','d','e','f','g','h','i','j','k']
letters_dict_3 = {'a':4,'b':5,'c':9,'d':121,'e':150,'f':1501,'g':2110,'h':2129,'i':2301,'j':2549,'k':2608}
seq6 = teaser_looper(n,letter_set_sorted,letters_dict_3)

n=4000
letter_set_sorted = ['a','b','c']
letters_dict_4 = {'a':1000,'b':1999,'c':2999}
seq7 = teaser_looper(n,letter_set_sorted,letters_dict_4)
