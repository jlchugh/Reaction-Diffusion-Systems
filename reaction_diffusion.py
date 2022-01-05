import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# given rates for coral growth simulation as given by Karl Sims https://www.karlsims.com/rd.html
feed_rate = .0545
kill_rate = .062
height = 1000
width = 1000
delta_t = 1.0
d_A = 1.0
d_B = .5

# kernel for convolution default values
top_left = .05
top_center = .2
top_right = .05
middle_left = .2
middle_center = -1.0
middle_right = .2
bottom_left = .05
bottom_center = .2
bottom_right = .05

# prompt the user for the height, width, feed_rate, kill_rate, delta_t, and diffusion rates for A and B


def get_user_input():
    feed_rate = float(input("enter feed rate: "))
    kill_rate = float(input("enter kill rate: "))
    height = int(input("enter height: "))
    width = int(input("enter width: "))
    delta_t = float(input("enter delta_t: "))
    d_A = float(input("enter diffusion rate for A: "))
    d_B = float(input("enter diffusion rate for B: "))

# prompt the user for a 3x3 kernel to define the laplacian via a 3x3 convolution


def get_kernel():
    top_left = float("enter 3x3 convolution matrix - top left: ")
    top_center = float("enter 3x3 convolution matrix - top center: ")
    top_right = float("enter 3x3 convolution matrix - top right: ")
    middle_left = float("enter 3x3 convolution matrix - middle left: ")
    middle_center = float("enter 3x3 convolution matrix - middle center: ")
    middle_right = float("enter 3x3 convolution matrix - middle right: ")
    bottom_left = float("enter 3x3 convolution matrix - bottom left: ")
    bottom_center = float("enter 3x3 convolution matrix - bottom center: ")
    bottom_right = float("enter 3x3 convolution matrix - bottom right: ")

# create a 2d grid of pairs that represents areas of distinct concentration of chemical A and B (not individual particls)


def initialize_grid(height=1000, width=1000):
    grid = []
    for x in range(width):
        grid.append([])
        for y in range(height):
            # initialize with all A = 1.0 all B = 0.0
            grid[x].append([1.0, 0.0])


# give a 2x2 grid and return a 2x2 grid with the convolution matrix applied to all elements
# need to make sure that the edges are not affected; we will keep them the same
def calculate_new_concentrations(grid, time):
    # for each item in the matrix
    for x in width:
        for y in height:
            # only calculate values within a frame of thickness 1
            # johnny you fucked this up you need to figure out how to do both a and b
            if x >= 1 and x <= width - 1 and y >= 1 and y <= height - 1:
                nabla_A = top_left * grid[x - 1][y - 1][0] + top_center * grid[x - 1][y][0] + top_right * grid[x - 1][y + 1][0] + middle_left * grid[x][y - 1][0] +
                middle_center * grid[x][y][0] + middle_right * grid[x][y + 1][0] + \
                    bottom_left * grid[x + 1][y - 1][0] + \
                    bottom_center * grid[x + 1][y][0]
                + bottom_right * grid[x + 1][y + 1][0]

                nabla_B = top_left * grid[x - 1][y - 1][1] + top_center * grid[x - 1][y][1] + top_right * grid[x - 1][y + 1][1] + middle_left * grid[x][y - 1][1] +
                middle_center * grid[x][y][1] + middle_right * grid[x][y + 1][1] + \
                    bottom_left * grid[x + 1][y - 1][1] + \
                    bottom_center * grid[x + 1][y][1]
                + bottom_right * grid[x + 1][y + 1][1]

                a = grid[x][y][0]
                b = grid[x][y][1]
                # A' = A + (d_A*nabla^2*A-AB^2 + f*(1-A))*delta_t
                new_A = a + (d_A * nabla_A**2 * a - a * b **
                             2 + feed_rate * (1 - a)) * delta_t
                # B' = B+(d_B*nabla^2*B+AB^2 - (k+f)B)*delta_t
                new_B = b + (d_B * nabla_B**2 * b * a * b**2 -
                             (kill_rate + feed_rate) * b) * delta_t
                grid[x][y][0] = new_A
                grid[x][y][1] = new_B
