import random


def pi(num_samples):
    count_circle = 0
    count_square = 0

    for i in range(num_samples):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)

        if(x >= 0 and y >= 0):
            count_square += 1
        if(x ^ 2 + y ^ 2) <= 10000:
            count_circle += 1

    return count_circle / count_square

def run():
    num_samples = 1000000  # You can adjust this number to increase or decrease accuracy
    pi_estimate = pi(num_samples)
    print(f"Estimated Pi: {pi_estimate}")



'''import random

#MonteCarlo in Pi
def pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)  # Generate a random x-coordinate between 0 and 1
        y = random.uniform(0, 1)  # Generate a random y-coordinate between 0 and 1
        distance = x**2 + y**2  # Calculate the squared distance from the origin

        if distance <= 1:  # Check if the point is inside the quarter-circle (x^2 + y^2 <= 1)
            inside_circle += 1

    pi_estimate = 4 * inside_circle / num_samples  # Estimate Pi based on the ratio of points inside the quarter-circle
    return pi_estimate

def run():
    num_samples = 1000000  # You can adjust this number to increase or decrease accuracy
    pi_estimate = pi(num_samples)
    print(f"Estimated Pi: {pi_estimate}")'''