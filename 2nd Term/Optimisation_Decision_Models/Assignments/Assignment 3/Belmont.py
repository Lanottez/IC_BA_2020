from pulp import *

# define the town names
names = ['Arlington', 'Belmont', 'Cambridge', 'Lexington', 'Somerville', 'Winchester']

# define the distance matrix
distances = [[ 0,  5, 10, 15, 20, 15],
             [ 5,  0,  8, 10, 15, 12],
             [10,  8,  0, 15, 20, 10],
             [15, 10, 15,  0, 10, 12],
             [20, 15, 20, 10,  0, 12],
             [15, 12, 10, 12, 12,  0]]

# define a binary decision variable for each town
x = []
for n in names:
    x += [ LpVariable (n, cat = 'Binary') ]
    
# define the objective function
Belmont_model = pulp.LpProblem ("Belmont Model", pulp.LpMinimize)
Belmont_model += sum (x)

# define the constraints
for i in range (len (names)):
    curr_expr = 0
    for j in range (len (names)):
        if distances[i][j] <= 10:
            curr_expr += x[j]
    Belmont_model += curr_expr >= 1

# solve the problem
Belmont_model.solve()

# print the result
for i in range (len (names)):
    print ("{}:\t{}".format (names[i], x[i].value()))
