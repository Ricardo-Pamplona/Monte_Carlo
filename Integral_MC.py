import random
import math
import matplotlib.pyplot as plt
import numpy as np

def estimate_integral(n):
    inside_area_x = []
    inside_area_y = []
    outside_area_x = []
    outside_area_y = []

    for i in range(n):
        x = random.random()
        y = random.random()
        if y <= math.e**-x:
            inside_area_x.append(x)
            inside_area_y.append(y)
        else:
            outside_area_x.append(x)
            outside_area_y.append(y)

    integral_estimate = len(inside_area_x)/n
    return integral_estimate, inside_area_x, inside_area_y, outside_area_x, outside_area_y

def plot_graph(inside_x, inside_y, outside_x, outside_y):
    x = np.linspace(0, 1, 100)
    y = math.e**-x
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.scatter(inside_x, inside_y, color='green', s=1)
    plt.scatter(outside_x, outside_y, color='red', s=1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


N1 = 1000
integral_value, inside_x, inside_y, outside_x, outside_y = estimate_integral(N1)
print(f"Estimativa da integral = {integral_value}")

plot_graph(inside_x, inside_y, outside_x, outside_y)