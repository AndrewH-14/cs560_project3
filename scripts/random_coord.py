# This code was generated with the help of Grok AI by xAI

import random
import math

# Function to generate random 2D coordinate within the specified square
def random_coordinate(min, max):
    x = random.uniform(min, max)
    y = random.uniform(min, max)

    return (x, y)

# Function to generate a random degree between 0 and 360
def random_degree():
    return random.uniform(0, 360) * (math.pi / 180)

coord  = random_coordinate(-3.5, 3.5)
coord  = random_coordinate(-7.5, 7.5)
degree = random_degree()

print(f"Random Coordinate: {coord}")
print(f"Random Degree (Radians): {degree:.2f}")
