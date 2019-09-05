import numpy as np
import random
# This first part of the program is desinged to create a random sample from 1 to 7, and the second will calculate all sample's(sample [1,1000]) x bar and you can compare it with the real population M.

def create_random_sample():
    return np.random.randint(1, 7)


def calculate_random_samples():
    sample = 0.0
    
    for i in range(1000):
        random_sample = random.random()
        sample += random_sample

    return sample / 1000


print(calculate_random_samples())

print(random.random())
random.randint()
