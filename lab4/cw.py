### Z1
import numpy as np
weight = np.array([-1])
bias = 0.5

def activation_function(fx):
    return 1 if fx >= 0 else 0

inputs = np.array([[0], [1]])
for i in inputs:
    fx = np.dot(weight, i) + bias
    c=activation_function(fx)
    #print(f"Przed {i[0]},PO  {c}")
### z1.2
weight = np.array([1,1])

bias = -1.5

def actub_and(x, weight, bias):
    fx = np.dot(weight, x)  + bias
    if fx >= 0:
        return i, 1
    else:
        return i, 0

inputs = np.array([[0,1],[0,0],[1,1],[1,0]])
for i in inputs:
    fx = np.dot(weight, i) + bias
    c=actub_and(i,weight,bias)
    #print(f"Przed {i[0]},PO  {c}")
## z2 
weight = np.array([1,-1])

bias = -0.5

def actub_and_not(x, weight, bias):
    fx = np.dot(weight, x)  + bias
    if fx >= 0:
        return i, 1
    else:
        return i, 0

inputs = np.array([[0,1],[0,0],[1,1],[1,0]])
for i in inputs:
    fx = np.dot(weight, i) + bias
    c=actub_and(i,weight,bias)
    #print(f"Przed {i[0]},PO  {c}")
# zad 3 
"""
import numpy as np

# wagi dla perceptronów w sieci neuronowej
w_and1 = np.array([1, 1])
w_and2 = np.array([-1, -1])
w_or = np.array([1, 1])
w_not = np.array([1, -2])

bias_and1 = -1.5
bias_and2 = -0.5
bias_or = -0.5
bias_not = -0.5

# funkcja aktywacji - schodki
@np.vectorize
def step(x):
    return 1 if x > 0 else 0

# implementacja sieci neuronowej XOR
def xor_network(x1, x2):
    # warstwa perceptronów AND
    and1 = step(np.dot(w_and1, np.array([x1, x2])) + bias_and1)
    and2 = step(np.dot(w_and2, np.array([x1, x2])) + bias_and2)

    # warstwa perceptronów OR
    or_out = step(np.dot(w_or, np.array([and1, and2])) + bias_or)

    # perceptron NOT
    not_out = step(np.dot(w_not, or_out.reshape((2, 1))) + bias_not)

    # zwrócenie wyniku sieci
    return not_out

# testowanie sieci neuronowej XOR
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
for x in inputs:
    print(f"XOR({x[0]}, {x[1]}) = {xor_network(x[0], x[1])}")
    
    
    """
    
weight = np.array([1,1])

bias = -1.5

def actub_and(x, weight, bias):
    fx = np.dot(weight, x)  + bias
    if fx >= 0:
        return  1
    else:
        return  0
Hold=[]
inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
for i in inputs:
    fx = np.dot(weight, i) + bias
    c=actub_and(i,weight,bias)
    print(f"Przed {i[0]},PO  {c}")
    Hold.append(c)

weight = np.array([-1])
bias = 0.5

And_hold=[]
def activation_function(fx):
    return 1 if fx >= 0 else 0
for a in Hold:
    fx = np.dot(weight, a) + bias
    And_hold.append(activation_function(fx))


weight = np.array([1,1])
bias = -0.5
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
def OR_perceptron(x, weight, bias):
    
    fx = np.dot(weight, x)  + bias
    
    if fx >= 0:
        return  1
    else:
        return  0
holder_or=[]
for i in inputs:
    holder_or.append(OR_perceptron(i, weight, bias))
#print(holder_or)
#print(And_hold)
x = []
for a in range(4):
    x.append([holder_or[a],And_hold[a]])
weight = np.array([1,1])

bias = -1.5
for i in x:
    fx = np.dot(weight, i) + bias
    c=actub_and(i,weight,bias)
    print(f"Przed {i},PO  {c}")