import random
import os
import time

color = {
    "end": "\x1b[0m",
    "red": "\x1b[1;31;50m",
    "green": "\x1b[1;32;50m",
    "yellow": "\x1b[1;33;50m",
    "blue": "\x1b[1;34;50m",
    "violet": "\x1b[1;35;50m",
    "cyan": "\x1b[1;36;50m"
}

print(f"{color['red']} KeyMap {color['end']}")


class Graph:
    def __init__(self):

        color = {
            "end": "\x1b[0m",
            "red": "\x1b[1;31;50m",
            "green": "\x1b[1;32;50m",
            "yellow": "\x1b[1;33;50m",
            "blue": "\x1b[1;34;50m",
            "violet": "\x1b[1;35;50m",
            "cyan": "\x1b[1;36;50m"
        }
        self.color = color

        graph2d = []
        self.graph2d = graph2d
        n = int(10)
        self.n = n
        counter = 0
        for i in range(n):
            layer = []
            for j in range(n):
                # possible connections
                p_c = {
                    "left": counter - 1,
                    "right": counter + 1,
                    "top": counter - n,
                    "bottom": counter + n,
                    "top-left": counter - n - 1,
                    "top-right": counter - n + 1,
                    "bottom-left": counter + n - 1,
                    "bottom-right": counter + n + 1,
                }
                connect = [p_c["left"], p_c["right"], p_c["top"], p_c["bottom"], p_c["top-right"], p_c["top-left"],
                           p_c["bottom-right"], p_c["bottom-left"]]

                if j == 0 or i == 0:
                    connect.remove(p_c["top-left"])
                    connect.remove(p_c["top-right"])
                    connect.remove(p_c["bottom-left"])

                if j == 0:
                    connect.remove(p_c["left"])

                if i == 0:
                    connect.remove(p_c["top"])

                if j == n - 1:
                    connect.remove(p_c["right"])
                    connect.remove(p_c["bottom-right"])
                    if p_c["top-right"] in connect:
                        connect.remove(p_c["top-right"])

                if i == n - 1:
                    connect.remove(p_c["bottom"])
                    if p_c["bottom-left"] in connect:
                        connect.remove(p_c["bottom-left"])
                    if p_c["bottom-right"] in connect:
                        connect.remove(p_c["bottom-right"])

                random_color = random.randint(0, 5)
                layer.append([connect, random_color])
                counter += 1
            graph2d.append(layer)

        # graph2d[random_start // n][random_start % 10][1] = -1
        # graph2d[random_end // n][random_end % 10][1] = -2

        start_x = random.randint(0, int(0.4 * (n - 1)))
        start_y = random.randint(0, int(0.4 * (n - 1)))
        end_x = random.randint(int(0.7 * (n - 1)), int((n - 1)))
        end_y = random.randint(int(0.5 * (n - 1)), int(0.9 * (n - 1)))

        graph2d[start_x][start_y][1] = -1
        graph2d[end_x][end_y][1] = -2

        start_adress = (start_x) * n + start_y
        self.start_adress = start_adress
        end_adress = (end_x) * n + end_y
        self.end_adress = end_adress

    def output(self):
        x2, y2 = graph.address_x_y(self.start_adress)
        self.graph2d[x2][y2][1] = -1
        counter = 0
        print("▁" * (2 * self.n + 3))
        for i in range(len(self.graph2d)):
            print(" ▏", end="")
            for j in self.graph2d[i]:
                if j[1] == -3:
                    print(f"{color['yellow']}'{color['end']}", end=" ")
                elif j[1] == -2:
                    print(f"{color['red']}E{color['end']}", end=" ")
                elif j[1] == -1:
                    print(f"{color['green']}S{color['end']}", end=" ")

                elif j[1] <= 1:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
                counter += 1
            print("▏  ")
        print("─" * (2 * self.n + 3))

    def address_x_y(self, address):
        y = address % self.n
        x = (address - y) / self.n
        return int(x), int(y)

    def output_graph_array(self):
        counter = 0
        for i in range(len(self.graph2d)):
            for j in self.graph2d[i]:
                print(counter, ": ", j, end="\n")
                # print(counter, end=" ")
                counter += 1
            print()

    def solve_bfs(self):
        visited = [0] * ((self.n) ** 2)
        queue = []
        prev = [-1] * (self.n ** 2)
        queue.append(self.start_adress)
        visited[self.start_adress] = True
        dist = 0
        while queue:
            s = queue.pop(0)
            if s == self.end_adress:
                print(f"Path found!")
                break

            x, y = graph.address_x_y(s)
            # os.system("clear")
            # graph.output()
            # time.sleep(0.01)

            # print(s, end=" ")
            for i in self.graph2d[x][y][0]:
                x1, y1 = graph.address_x_y(i)

                # if self.graph2d[x][y][1] <= 1 or self.graph2d[x][y][1] <= 0:
                if visited[i] == False and self.graph2d[x1][y1][1] != 0 and self.graph2d[x1][y1][1] != 1:
                    queue.append(i)
                    visited[i] = True
                    prev[i] = s

                    #
        path = []
        i = self.end_adress
        while i != -1:
            path.append(i)
            i = prev[i]

        final_path = []
        for i in range(len(path) - 1, -1, -1):
            final_path.append(path[i])
            if path[i] != self.end_adress:
                x, y = graph.address_x_y(path[i])
                self.graph2d[x][y][1] = -3

        return final_path

    def test(self):
        # print(self.start_adress)
        counter = 0
        for i in range(self.n):
            for j in range(self.n):
                print(counter, end=" ")
                counter += 1
            print()


for j in range(1000):
    start = time.time()
    # os.system("clear")
    print(f"Maze number: {j}")
    graph = Graph()

    graph.output()
    graph.output_graph_array()
    end = time.time()
    # graph.test
    start2 = time.time()
    graph.solve_bfs()
    graph.output()

    end2 = time.time()
    print(f"Generated in {str(end - start)[:5]}")
    print(f"Solved in {str(end - start)[:5]}")
    af = input()