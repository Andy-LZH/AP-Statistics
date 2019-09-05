import numpy as np
import random


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