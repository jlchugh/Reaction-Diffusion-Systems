import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# given rates for coral growth simulation as given by Karl Sims https://www.karlsims.com/rd.html
feed_rate = .0545
kill_rate = .062
height = 1000
width = 1000
delta_t = 1.0
d_a = 1.0
d_t = .5

# prompt the user for the height, width, feed_rate, kill_rate, delta_t, and diffusion rates for A and B
def get_user_input():


#prompt the user for a 3x3 kernel to define the laplacian via a 3x3 convolution
def get_kernel():


# create a 2d grid of pairs that represents areas of distinct concentration of chemical A and B (not individual particls)
def initialize_grid(height=1000, width=1000):
    grid = []
    for x in range(width):
        grid.append([])
        for y in range(height):
            # initialize with all A = 1.0 all B = 0.0
            grid[x].append([1.0, 0.0])



def calculate_new_concentrations()
