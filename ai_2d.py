

# Core localization functions used by Googles self-driving cars, which implement predictive algorithms based on Bayesian methods. This is a commented
# version of the homework assignment for the end of the first Unit in Udacity's AI for robotics class. It is implemented in Python. Enjoy!




                                   ##### ----- GIVEN VALUES FOR FUNCTION TESTS ----- #####


# Hypothetical color world. In reality, Google self-driving cars represent the roads they drive on as two dimensional matrices of values, representing positions.
colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

# Predetermined set of possible measurements sensed before this test. In reality, these measurements would be pushed by repeated calls to the sense method.
measurements = ['green', 'green', 'green' ,'green', 'green']

# Predetermined set of motions (no motion, right, down, down, right). In reality, the motions would be based on sense functions,
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

# This value is pre-chosen and represents the likelihood of the sensor taking a correct measurement.
sensor_right = 0.7

# This value represents the likelihood that the robot has moved.
p_move = 0.8

# Compliment of sensor_right value. Definding this now saves typing below.
sensor_wrong = 1.0 - sensor_right


p_stay = 1.0 - p_move


                                       ##### ----- CORE FUNCTIONS -----#####




# Checks the color currently measured against the position. If they match, hit is returned, aux is calculated
# then normalized to 1, in accordance with Bayes' Rule, and returned.
def sense(p, colors, measurement):
    aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]

    s = 0.0
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (measurement == colors[i][j])
            aux[i][j] = p[i][j] * (hit * sensor_right + (1 - hit) * sensor_wrong)
            s += aux[i][j]
    for i in range(len(aux)):
        for j in range(len(p[i])):
            aux[i][j] /= s
    return aux

# Moves through the motions vector and predicts current location based on probability of having moved or stayed. No normalization here.
def move(p, motions):
    aux = [[0.0 for row in range(len(p[0]))] for col in range(len(p))]

    for i in range(len(p)):
        for j in range(len(p[i])):
            aux[i][j] = (p_move * p[(i - motions[0]) % len(p)][(j - motions[1]) % len(p[i])]) + (p_stay * p[i][j])
    return aux

# Shows probability of being in each given location in the world matrix.
def show(p):
    for i in range(len(p)):
        print p[i]

# catching errors
if len(measurements) != len(motions):
    raise ValueError, "error in size of measurement or motions vector"

# caculates initial value for the elements in a matrix of variable length, based on uniform distribution
pinit = 1.0 / float(len(colors)) / float(len(colors[0]))

# wraps into a single var, a function that distributes the initial values for each element in the matrix
p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

# prints it out pretty
for k in range(len(measurements)):
    p = move(p, motions[k])
    p = sense(p, colors, measurements[k])

#Calling show function to display probabilistic weights against all possible locations
show(p)
