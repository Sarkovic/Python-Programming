import math
import csv
import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from collections import defaultdict
from heapq import heapify, heappop, heappush

COORDINATES_FILE = "Coordinates.csv"
DISTANCE_FILE = "distances.csv"

x_points = []               # List of X-Axis Coordinates of all stars
y_points = []               # List of Y-Axis Coordinates of all stars
z_points = []               # List of Z-Axis Coordinates of all stars
stars = []                  # List of the name of all stars

# Dictionary to store the 3D coordinates of each star in the form of (x,y,z) tuples.
coordinates = {}
# Dictionary like object where key = star and its value = list of neighboring stars and their distances
adjacency_list = defaultdict(list)

# Reads the coordinates of each star from the specified CSV file
with open(COORDINATES_FILE, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for star_name, x, y, z in reader:
        stars.append(star_name)                                     # Adding Star names in the list called Stars
        x_points.append(int(x))                                     # Adding X-Axis values of all stars in the list called x_points
        y_points.append(int(y))                                     # Adding Y-Axis values of all stars in the list called y_points
        z_points.append((int(z)))                                   # Adding Z-Axis values of all stars in the list called z_points
        coordinates[star_name] = (int(x), int(y), int(z))           # Storing the 3D coordinates of each star in the form of (x,y,z) tuples in the coordinates dictionary

# Reads the Source star, Destination star & Distance between them from the specified CSV file
with open(DISTANCE_FILE, "r") as file:
    reader = csv.reader(file)
    for source, destination, dist in reader:
        adjacency_list[source].append((destination, int(dist)))    # Creating adjacency List for all stars where key = star & value = neighbour star & distance from source

SOURCE_STAR = "Sun"
DESTINATION_STAR = "Upsilon Andromedae"
#SOURCE_STAR = "TRAPPIST-1"
#DESTINATION_STAR = "55 Cancri"

choice = input("Choose algorithm: \n1. Dijkstra \n2. A*\n")        # Algorithm choosing option

# Dijkstra Algorithm
if choice == "1":
    algorithm = "Dijkstra"
    DIJKSTRA = True

    priority_queue = [(0, SOURCE_STAR, None)]           # Priority queue = (Distance from source, Current star, Parent)
    visited = set()                                     # Keeping track of visited stars in a set
    parent_map = {}                                     # Keeping track of star's parent in parent_map dictionary

    # Initially the distance g(n) for every star from source is set to infinity except source star
    distance_from_src = {star_name: float('inf') for star_name in coordinates.keys()}
    distance_from_src[SOURCE_STAR] = 0

    while priority_queue:
        # Pop from priority queue will be based on f(n) value....min value will pick first as minheap
        path_distance_from_src, current_star, parent_star = heappop(priority_queue)

        # Skipping the star that appeared more than once
        if current_star in visited:
            continue

        # Goal/Destination Star checking , If found return else continue searching
        if current_star == DESTINATION_STAR:
            print("From" + " " + SOURCE_STAR + " " + "to" + " " + DESTINATION_STAR + " , total Distance = " + str(
                path_distance_from_src))
            break

        # Visited star will be added in the set
        visited.add(current_star)

        # For Dijkstra , f(n) = g(n) where g(n) represents distance between two stars taken from adjacency list dictionary
        for neighborstar_name, neighborstar_distance in adjacency_list[current_star]:
            # Updating g(n) in every move , g(n) = g(n) + current star to next star distance
            new_path_distance_from_src = path_distance_from_src + neighborstar_distance

            # Updating g(n) by relaxing operation
            if new_path_distance_from_src < distance_from_src[neighborstar_name]:
                distance_from_src[neighborstar_name] = new_path_distance_from_src

                # priority queue,distance,neighbor & current star are being pushed in Queue to solve
                heappush(priority_queue, (new_path_distance_from_src, neighborstar_name, current_star))

                # Current star's parent will be its previous star from which current star comes from
                parent_map[neighborstar_name] = current_star


# A* Search Algorithm
else:
    algorithm = "A*"
    DIJKSTRA = False

    # Heuristic function (Euclidean distance between two points in 3D space) for A* Search Algorithm
    def distance(x1, y1, z1, x2, y2, z2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

    priority_queue = [(0, SOURCE_STAR)]                     # Priority queue = (Distance from source, Current star)
    visited = set()                                         # Keeping track of visited stars in a set
    parent_map = {}                                         # Keeping track of star's parent in parent_map dictionary

    # Initially the distance g(n) for every star from source is set to infinity except source star
    distance_from_src = {star_name: float('inf') for star_name in coordinates.keys()}
    distance_from_src[SOURCE_STAR] = 0

    # Pop from priority queue will be based on f(n) value....min value will pick first as minheap
    while priority_queue:
        path_distance_from_src, current_star = heappop(priority_queue)

        # Skipping the star that appeared more than once
        if current_star in visited:
            continue

        # Goal/Destination Star checking , If found return else continue searching
        if current_star == DESTINATION_STAR:
            print("From" + " " + SOURCE_STAR + " " + "to" + " " + DESTINATION_STAR + " , total Distance = " + str(
                path_distance_from_src))
            break

        # Visited star will be added in the set
        visited.add(current_star)

        # For A* Search , f(n) = g(n) + h(n) where h(n) = heuristic function & g(n) represents distance between two stars taken from adjacency list dictionary
        for neighbor_star, neighbor_distance in adjacency_list[current_star]:
            # Updating g(n) in every move , g(n) = g(n) + current star to next star distance
            new_path_distance_from_src = distance_from_src[current_star] + neighbor_distance

            # Updating g(n) by relaxing operation
            if new_path_distance_from_src < distance_from_src[neighbor_star]:
                distance_from_src[neighbor_star] = new_path_distance_from_src

                # Setting priority , f(n) = g(n) + h(n)
                priority = new_path_distance_from_src + distance(*coordinates[neighbor_star], *coordinates[DESTINATION_STAR])

                # priority queue,priority,neighbor star are being pushed in Queue to solve
                heappush(priority_queue, (priority, neighbor_star))

                # Current star's parent will be its previous star from which current star comes from
                parent_map[neighbor_star] = current_star


# Path printing from source to destination
if DESTINATION_STAR not in parent_map:
    print("Cannot reach destination")

# Finding the path by backtracking & printing the path from source to destination
else:
    path = []                                         # List of stars that are on the path from source to destination
    current_star = DESTINATION_STAR
    while current_star != SOURCE_STAR:
        path.append(current_star)
        current_star = parent_map[current_star]
    path.append(SOURCE_STAR)
    print(f"{algorithm} Path: {' -> '.join(reversed(path))}")

# # for 3D Drawing in 3D Plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Plot stars
# ax.scatter(x_points, y_points, z_points, c='black', marker='*', s=100)
#
# # Plot path from source to destination
# if DESTINATION_STAR in parent_map:
#     path = []
#     current_star = DESTINATION_STAR
#     while current_star != SOURCE_STAR:
#         path.append(current_star)
#         current_star = parent_map[current_star]
#     path.append(SOURCE_STAR)
#     path_x = [x_points[stars.index(star)] for star in path]
#     path_y = [y_points[stars.index(star)] for star in path]
#     path_z = [z_points[stars.index(star)] for star in path]
#     ax.plot(path_x, path_y, path_z, c='red', linestyle='-')
#
# # Set labels
# ax.set_xlabel('X Coordinate')
# ax.set_ylabel('Y Coordinate')
# ax.set_zlabel('Z Coordinate')
# ax.set_title('3D Coordinates of Stars')
#
# # Showing the figure
# plt.show()