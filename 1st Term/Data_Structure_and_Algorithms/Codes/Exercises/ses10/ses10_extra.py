# Using Fantasy football data

import json

# This command imports the function greedy from ses08.py
# It will only work if the Spyder working directory is the one where the file is located
# Change the working directory using the folder icon in the top right corner
from ses10 import greedy, Item


##########################################
# Greedy fractional knapsack

def greedy_fractional(items, max_weight, key_function):
    """
    Greedy fractional knapsack solution

    Parameters:
        items - list of Items
        max_weight - knapsack size
        key_function - function to sort items with

    Returns:
        list with the highest-value set of items fitting the knapsack:
            each item of the list should be a tuple (item, fraction_of_item_in_knapsack)
        the value of the resulting knapsack
    """

    # Sort items
    sorted_items = sorted(items, key=key_function, reverse=True)
    result = []  # list of tuples: each item is (item, fraction of the item in knapsack), eg (item,0.8)
    total_value = 0.0  # knapsack value
    total_weight = 0.0  # knapsack weight <= max_weight

    # Loop through all items
    for i in range(len(sorted_items)):
        cur_item = sorted_items[i]
        # If we can fit item into knapsack, do it and update its weight and value
        if ...:
            pass
        else:  # If cannot fit full item, fill knapsack to capacity
            pass
    return result, total_value


def test_greedy_fractional():
    """
    Tests for greedy algorithm
    >>> names = ['clock', 'painting', 'radio']
    >>> values = [175,90,20]
    >>> weights = [10,9,4]
    >>> items = [Item(n, v, w) for n,v,w in zip(names, values, weights)]
    >>> res, val = greedy_fractional(items, 5, density)
    >>> val
    87.5
    >>> res, val = greedy_fractional(items, 13, density)
    >>> val
    205.0
    >>> res, val = greedy_fractional(items, 11, weight_inverse)
    >>> val
    90.0
    """
    # Please do not edit this function
    pass

###########################################
# Player class

class Player(object):
    """
    Player class for knapsack problem

    Has a name, a team, a value, and a weight, position.
    """
    def __init__(self, n, t, v, w, p):
        self.name = n
        self.team = t
        self.position = p
        self.value = int(v)
        self.weight = int(w)

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_position(self):
        return self.position

    def get_weight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + self.position + ', ' + self.team + ', ' + str(self.value) \
                 + ', ' + str(self.weight) + '>'
        return result

    __repr__ = __str__ # nice representation of objects in eg lists


###########################################
# Helper functions


def create_player_list(players, teams):
    """
    Create a list of player objects from list of player data lists
    """
    positions = {1:'Goalkeeper', 2:'Defender', 3:'Midfielder', 4:'Forward'}
    
    player_list = []
    for player in players:
        name = f"{player['first_name']} {player['second_name']}"
        team = teams[int(player['team'])]
        weight = int(player['now_cost'])
        value = int(player['total_points'])
        position = positions[int(player['element_type'])]
        player_list.append(Player(name, team, value, int(weight), position))
    return player_list


def read_players(filename):
    """
    Get player data from JSON

    Assumes JSON from the Premier League API https://fantasy.premierleague.com/api/bootstrap-static/
    
    Could also do directly
    >>> import requests
    >>> r = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    >>> data = r.json()
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    
    teams = data["teams"]
    team_mapping = {team["id"]:team["name"] for team in teams}
    players = data["elements"]
    
    # Get players as list
    player_list = create_player_list(players, team_mapping)

    return player_list, players


def value(item):
    """
    Return the value of the item

    Parameters:
        item - an Item object

    Returns:
        the value of the item
    """
    return item.get_value()


def weight_inverse(item):
    """
    Return the inverse of item weights

    Parameters:
        item - an Item object

    Returns:
        the inverse of the item's weight
    """
    return 1/item.get_weight()


def density(item):
    """
    Return the item's ratio of value to weight

    Parameters:
        item - an Item object

    Returns:
        the ratio of value to weight
    """
    return item.get_value() / item.get_weight()


# json_data = 'fantasy.json'
# pl_items, players = read_players(json_data)


## Solve problem with greedy algorithm
#rs, v = greedy(pl_items, 900, density)
#print(v)
#for item in rs:
#   print(item)


# Greedy heuristic with team constraints

def greedy_heuristic(items, max_weight, key_function, max_players):
    """
    Greedy knapsack solution with team constraints

    Parameters:
        items - list of Items
        max_weight - knapsack size
        key_function - function to sort items with

    Returns:
        list with the highest-value set of items fitting the knapsack
        the value of the resulting knapsack
    """

    # max players for each position
    max_goal = 1
    max_def = 4
    max_mid = 4
    max_fw = 2

    # init: sort items
    sorted_items = sorted(items, key=key_function, reverse=True)
    result = []
    total_value = 0.0  # knapsack value
    total_weight = 0.0  # knapsack weight <= max_weight
    pass

