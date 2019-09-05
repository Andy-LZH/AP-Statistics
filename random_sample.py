import numpy as np
import random
# create a random sample from 1 to 7

def create_random_sample():
    return np.random.randint(1, 7)

# calculate all sample's(sample [1,1000]) x bar and you can compare it with the population mean

def calculate_random_samples():
    sample = 0.0
    
    for i in range(1000):
        random_sample = random.random()
        sample += random_sample

    return sample / 1000


print(calculate_random_samples())

print(random.random())
random.randint()
