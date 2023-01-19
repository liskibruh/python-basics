#Lena is a graphic designer who has been working on a new project for her client.
#She needs to determine the probability that the client will approve of the design
#she has created.
#To do this, she uses an algorithm that considers several factors, including the 
#number of revisions the client has requested in the past and the overall design quality. 
#The equation for the algorithm is:
#probability = σ(a + 0.27b + 0.18c)

#Where:
# a: Indicates the number of revisions the client has requested in the past.
# b: Indicates the overall quality of the design on a scale from 1 to 10.
# c: Indicates the length of time Lena has spent working on the design.
# σ: Is the sigmoid function.

import math

def sigmoid(x):
    return 1/(1 + math.exp(-x))

probability = sigmoid(2 + 0.27 * 8 + 0.18 * 10)
print(probability)