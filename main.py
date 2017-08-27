#Binod Bhandari

import sys
import os
from _heapq import *


def dijkstra(G,start_node):

    S = set([start_node])
    for i in range(len(G)):
        d = [float("Inf")] * len(G)

    d[start_node] = 0.0
    Q = []
    for x in range(len(G)):
        heappush(Q,(d[x], x))
    while Q:
        u = heappop(Q)
        S.add(u)
        for v in range(len(G[u[1]])):
            if G[u[1]][v] != float('Inf') and G[u[1]][v] != 0.0:
                if d[v] > d[u[1]] + G[u[1]][v]:
                    d[v] = d[u[1]] + G[u[1]][v]
                    new_Q = []
                    for i in Q:
                        if i[1] == v:
                            heappush(new_Q, (d[v], v))
                        else:
                            heappush(new_Q, i)
    print(d)


def floyd(G):

    A = G
    for k in range(firstLine):
        for i in range(firstLine):
            for j in range(firstLine):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
    for i in range(firstLine):
        print(A[i])


if __name__ == '__main__':

    weight_of_node = []
    vertices_list = []

    filename = input("File containing graph: ")
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            firstLine = int(file.readline())
            for content in file:
                weight_of_node.append(content.split(None, 3)[2])

        weight_of_node = [float(i) for i in weight_of_node]

        with open(filename, 'r') as file:
            next(file)
            G = []
            for ver in range(0, firstLine):
                adj_matrix = []
                for vert in range(0, firstLine):
                    if ver == vert:
                        adj_matrix.append(float(0))
                    else:
                        adj_matrix.append(float('Inf'))
                G.append(adj_matrix)

            for content in file:
                vertices1, vertices2, weigh = content.split()
                vertices1 = int(vertices1)
                vertices2 = int(vertices2)
                weigh = float(weigh)
                G[vertices1][vertices2] = weigh

        print("Possible Commands are:\n"
              "dijkstra x - Runs Dijkstra starting at node X. X must be an integer\n"
              "floyd - Runs Floyd's algorithm\n"
              "help - prints this menu\n"
              "exit or ctrl-D - Exits the program")

        while True:
            try:
                command = input("Enter command: ")
                command = command.split()

            except EOFError:
                print("Bye")
                break
            if len(command) < 1:
                print("Please enter one of the command.")

            elif command[0] == "exit":
                print("Bye")
                sys.exit(0)

            elif command[0] == "help":
                print("Possible Commands are:\n"
                      "dijkstra x - Runs Dijkstra starting at node X. X must be an integer\n"
                      "floyd - Runs Floyd's algorithm\n"
                      "help - prints this menu\n"
                      "exit or ctrl-D - Exits the program")

            elif command[0] == "dijkstra":
                if len(command) < 2:
                    print("Please enter a starting node, type help for more information")
                else:
                    start_node = int(command[1])
                    if start_node <= len(G):
                        dijkstra(G, start_node)
                    else:
                        print("Index out of range")

            elif command[0] == "floyd":
                floyd(G)

            else:
                print("Wrong Command!!\n"
                      "Please type help for the Command list")
    else:
        print("Sorry file " + filename + " does not exist.\n"
                                         "Please check your current directory and run it again")
