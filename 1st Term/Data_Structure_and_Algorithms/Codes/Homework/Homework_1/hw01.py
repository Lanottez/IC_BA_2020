# -*- coding: utf-8 -*-
"""
Homework 1
"""

#####
# Wind chill calculator
#####


def wind_chill(temp, wind_speed, a=13.12, b=0.6215, c=-11.37, d=0.16, e=0.3965):
    """
    Converts temperature and wind speed into wind-chill index.

    Formula: wci = a + b*T + c*W^d + e*T*W^d, where T is temperature and W is wind speed

    Parameters
        temp: temperature in Celsius
        wind_speed: wind speed in km/h
        a: constant with default value
        b: constant with default value
        c: constant with default value
        d: constant with default value
        e: constant with default value

    Returns:
        Wind chill index.
        If wind speed is lower than 5, return the temperature.
        Otherwise, return the index according to the formula, rounded to integer value

    Example use:
    >>> wind_chill(10, 0)
    10
    >>> wind_chill(-10, 20)
    -18
    >>> wind_chill(-20, 30)
    -33
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if wind_speed < 5:
        return temp
    else:
        return round(a + b*temp + c*wind_speed**d + e*temp*wind_speed**d)


#####
# A brainteaser
#####


def the_35_teaser(n):
    """
    A typical coding interview brainteaser.

    Parameters:
        n: integer

    Returns:
        For n divisible by 3, return '3'
        For n divisible by 5, return '5'
        For n divisible by both 3 and 5, return '35'
        Otherwise, return None.

    Example use:
    >>> the_35_teaser(9)
    '3'
    >>> the_35_teaser(95)
    '5'
    >>> the_35_teaser(300)
    '35'
    """
    if not n%3 and not n%5:
        return('35')
    elif not n%5:
        return('5')
    elif not n%3:
        return('3')
    else:
        return None


def the_35_looper(n):
    """
    Prints the first n values of the_35_teaser starting from 1
    
    Note you may call the function the_35_teaser
    
    Parameters:
        n: integer
    
    Example use:
    >>> the_35_looper(15)
    None
    None
    3
    None
    5
    3
    None
    None
    3
    5
    None
    3
    None
    None
    35
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    for i in range(1,n+1):
        print(the_35_teaser(i))
    

#####
# Date string conversion: slash-date format to dash-date format
#####


def convert_day(day_string):
    """
    Converts day string from slash-date to dash-date format

    Assumes day between '1' or '01' and '31'

    Parameters:
    day_string: string containing day number in slash-date format

    Returns:
    string containing day number in dash-date format

    Example use:
    >>> convert_day('8')
    '08'
    >>> convert_day('15')
    '15'
    """
    # Your code here. Don't change anything above.
    if len(day_string) == 1:
        day_string = '0' + day_string
    return day_string
    


def convert_month(month_string):
    """
    Converts month string from slash-date to dash-date format

    Assumes month between '1' or '01' and '12'

    Parameters:
    month_string: string containing month number in slash-date format

    Returns:
    string containing month number in dash-date format

    Example use:
    >>> convert_month('3')
    '03'
    >>> convert_month('11')
    '11'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if len(month_string) == 1:
        month_string = '0' + month_string
    return month_string


def convert_year(year_string):
    """
    Converts year string from slash-date to dash-date format

    Assumes the year is either between '00' and '99' or between '1000' and '9999'
    
    If the year is between '00' and '99', assumes the year is in 1921-2020
    
    Parameters:
    year_string: string containing year number in slash-date format

    Returns:
    string containing year number in dash-date format

    Example use:
    >>> convert_year('03')
    '2003'
    >>> convert_year('25')
    '1925'
    >>> convert_year('1945')
    '1945'
    >>> convert_year('1389')
    '1389'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if len(year_string) == 2:
        if int(year_string) <= 20:
            year_string = '20' + year_string
        else:
            year_string = '19' + year_string
    return year_string



def date_conversion(date_string):
    """
    Converts date string from slash format to dash format

    Assume European date ordering (day-month-year).
    Assume that two-digit years are in the past century (1921-2020 is "past century", 2021- is not...).
    Assume that the year of the date is in either range 00 - 99 or 1000 - 9999

    Parameters:
        date_string: string date in "slash" format, eg, 19/8/16, 1/12/1898, 1/1/25 (assume valid dates)

    Returns:
        string date in "dash" format, eg, 19-08-2016, 01-12-1898, 01-01-1925

    Example use:
    >>> print(date_conversion('19/8/16'))
    19-08-2016
    >>> print(date_conversion('01/12/1898'))
    01-12-1898
    >>> print(date_conversion('18/4/25'))
    18-04-1925
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

  
    # Your code should call the three functions above to solve the problem. 
    # You will need to implement them first.
    date_as_list = date_string.split('/')  # Use this to split slash format string into a list
    return convert_day(date_as_list[0]) + '-' + convert_month(date_as_list[1]) + '-' + convert_year(date_as_list[2])


##### 
# Robust version of date conversion
#####


def date_conversion_robust(date_string):
    """
    Converts date string from slash format to dash format.
    Checks if input date is valid; if not, prints an error and returns None.

    Valid dates are as follows:
    - European date ordering (day-month-year).
    - Two-digit years are in the past century (1921-2020 is "past century", 2021- is not...).
    - The year of the date is in either range 00 - 99 or 1000 - 9999
    - An actual date that has occurred or will occur

    Parameters:
        date_string: string date in "slash" format, eg, 19/8/16, 1/12/1898, 1/1/25 (DO NOT assume every input is a valid date)

    Returns:
        if input was valid: string date in "dash" format, eg, 19-08-2016, 01-12-1898, 01-01-1925
        if input was not valid: print out "Not a valid date", (return the default return value None)

    Example use:
    >>> print(date_conversion_robust('19/8/16'))
    19-08-2016
    >>> print(date_conversion_robust('1/12/1898'))
    01-12-1898
    >>> print(date_conversion_robust('16/3/25'))
    16-03-1925
    >>> print(date_conversion_robust('29/2/2017'))
    Not a valid date.
    None
    >>> date_conversion_robust('131/2/1928')
    Not a valid date.
    >>> print(date_conversion_robust(2))
    Not a valid date.
    None
    """
    
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    """
print(date_conversion_robust('131/2/1928'))
print(date_conversion_robust(19/2/1928))
print(date_conversion_robust(2))
print(date_conversion_robust('asd'))
print(date_conversion_robust('as/d'))
print(date_conversion_robust('a/s/d'))
print(date_conversion_robust('a/s/v/d'))
print(date_conversion_robust('11/13/1928'))
print(date_conversion_robust('11/12/11111'))
print(date_conversion_robust('11/12/111'))
print(date_conversion_robust('32/12/111'))
print(date_conversion_robust('31/11/111'))
    """
    
    def is_European_date_order(date_string):
        if not isinstance(date_string, str) or not '/' in date_string:
            return False
        return True

    def is_three_digit(date_string):
        date_as_list = date_string.split('/') 
        if len(date_as_list) !=3:
            return False
        return True


    def is_ints(date_string):
        
        def is_int(s):
            try: 
                int(s)
                return True
            except ValueError:
                return False
            
        date_as_list = date_string.split('/') 
        for date in date_as_list:
            if not is_int(date):
                return False
        return True    
    
    def is_in_range(day,month,year):
        if (year >= 0 and year <= 99) or (year >=1000 and year <=9999):
            return True
        return False
        
    def is_leap_year(year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
        
    def is_actual_date(day,month,year):
        month_31 = [1,3,5,7,8,10,12]
        month_30 = [4,6,9,11]
        month_29_28 = 2
        if month not in month_31 and month not in month_30 and month != month_29_28:
            return False
        else:
            if month in month_31 and day > 31:
                return False
            elif month in month_30 and day > 30:
                return False
            elif month == month_29_28:
                if is_leap_year and day > 29:
                    return False
                elif is_leap_year and day > 28:
                    return False
            return True

        

    if is_European_date_order(date_string) and is_three_digit(date_string) and is_ints(date_string):
        date_as_list = date_string.split('/')  # Use this to split slash format string into a list
        day = date_as_list[0]
        month = date_as_list[1]
        year= date_as_list[2]
        if is_in_range(int(day),int(month),int(year)) and is_actual_date(int(day),int(month),int(year)):
            return date_conversion(date_string)
        else:
            print('Not a valid date.')
    else:
        print('Not a valid date.')





def comparison_function(value):
    """
    Comparison function for counting_sort
    
    Parameter:
        value - integer
        
    Returns:
        ??? such that comparisons of return values work as described
    
    Example use:
    >>> comparison_function(99) > comparison_function(18783479)
    True
    >>> comparison_function(123) > comparison_function(321)
    False
    >>> comparison_function(1789) > comparison_function(96861)
    True
    """
    output = []
    digits = list(range(0,10))[::-1]
    list_value = list(str(value))
    for digit in digits:
        output.append(list_value.count(str(digit)))
    output.append(value)
    return output


def counting_sort(items):
    """
    Sorts a list of integers by counting different digits.
    
    Parameters:
        items - list of positive integers
        
    Returns:
        sorted copy of items
        
    Example use:
    >>> counting_sort([98, 19, 29, 41, 9999, 73, 241, 1111, 53, 3, 333])
    [1111, 3, 333, 41, 241, 53, 73, 19, 29, 98, 9999]
    >>> counting_sort([999, 19, 919, 111, 119, 1199, 911])
    [111, 19, 119, 911, 919, 1199, 999]
    >>> counting_sort([1234, 4321, 3214, 2413])
    [1234, 2413, 3214, 4321]
    """
    # Please do NOT edit this function.

    return sorted(items, key=comparison_function)

def date_conversion(date_string):
    """
    Converts date string from slash format to dash format

    Assume European date ordering (day-month-year).
    Assume that two-digit years are in the past century (1921-2020 is "past century", 2021- is not...).
    Assume that the year of the date is in either range 00 - 99 or 1000 - 9999

    Parameters:
        date_string: string date in "slash" format, eg, 19/8/16, 1/12/1898, 1/1/25 (assume valid dates)

    Returns:
        string date in "dash" format, eg, 19-08-2016, 01-12-1898, 01-01-1925

    Example use:
    >>> print(date_conversion('19/8/16'))
    19-08-2016
    >>> print(date_conversion('01/12/1898'))
    01-12-1898
    >>> print(date_conversion('18/4/25'))
    18-04-1925
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

  
    # Your code should call the three functions above to solve the problem. 
    # You will need to implement them first.
    date_as_list = date_string.split('/')  # Use this to split slash format string into a list
    return convert_day(date_as_list[0]) + '-' + convert_month(date_as_list[1]) + '-' + convert_year(date_as_list[2])
