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
    def __init__(self, n):
        self.color = color
        self.n = n
        self.graph2d = [[0 for _ in range(n)] for _ in range(n)]

        # Perform recursive division
        self.recursive_division(0, 0, n, n)

        start_x = random.randint(0, int(0.4 * (n - 1)))
        start_y = random.randint(0, int(0.4 * (n - 1)))
        end_x = random.randint(int(0.7 * (n - 1)), int((n - 1)))
        end_y = random.randint(int(0.5 * (n - 1)), int(0.9 * (n - 1)))

        self.graph2d[start_x][start_y] = -1
        self.graph2d[end_x][end_y] = -2

        self.start_adress = start_x * n + start_y
        self.end_adress = end_x * n + end_y

    def recursive_division(self, x, y, width, height):
        if width <= 1 or height <= 1:
            return

        horizontal = random.choice([True, False])

        if width > height:
            horizontal = False
        elif height > width:
            horizontal = True

        if horizontal:
            if height < 3:
                return
            wy = y + random.randint(1, height - 2)
            px = x + random.randint(0, width - 1)
            for i in range(x, x + width):
                if i == px:
                    continue
                self.graph2d[wy][i] = 1
            self.recursive_division(x, y, width, wy - y)
            self.recursive_division(x, wy + 1, width, y + height - wy - 1)
        else:
            if width < 3:
                return
            wx = x + random.randint(1, width - 2)
            py = y + random.randint(0, height - 1)
            for i in range(y, y + height):
                if i == py:
                    continue
                self.graph2d[i][wx] = 1
            self.recursive_division(x, y, wx - x, height)
            self.recursive_division(wx + 1, y, x + width - wx - 1, height)

    def output(self):
        print("▁" * (2 * self.n + 3))
        for row in self.graph2d:
            print(" ▏", end="")
            for cell in row:
                if cell == -3:
                    print(f"{color['yellow']}'{color['end']}", end=" ")
                elif cell == -2:
                    print(f"{color['red']}E{color['end']}", end=" ")
                elif cell == -1:
                    print(f"{color['green']}S{color['end']}", end=" ")
                elif cell == 1:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print("▏  ")
        print("─" * (2 * self.n + 3))

    def address_x_y(self, address):
        y = address % self.n
        x = (address - y) // self.n
        return int(x), int(y)

    def output_graph_array(self):
        counter = 0
        for row in self.graph2d:
            for cell in row:
                print(counter, ": ", cell, end="\n")
                counter += 1
            print()

    def solve_bfs(self):
        visited = [False] * (self.n ** 2)
        queue = []
        prev = [-1] * (self.n ** 2)
        queue.append(self.start_adress)
        visited[self.start_adress] = True
        while queue:
            s = queue.pop(0)
            if s == self.end_adress:
                print(f"Path found!")
                break

            x, y = self.address_x_y(s)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.n and 0 <= ny < self.n:
                    next_adress = nx * self.n + ny
                    if not visited[next_adress] and self.graph2d[nx][ny] != 1:
                        queue.append(next_adress)
                        visited[next_adress] = True
                        prev[next_adress] = s

        path = []
        i = self.end_adress
        while i != -1:
            path.append(i)
            i = prev[i]

        for i in range(len(path) - 1, -1, -1):
            if path[i] != self.end_adress:
                x, y = self.address_x_y(path[i])
                self.graph2d[x][y] = -3

        return path

    def test(self):
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
    graph = Graph(1000)

    graph.output()
    # graph.output_graph_array()
    end = time.time()
    # graph.test
    start2 = time.time()
    graph.solve_bfs()
    graph.output()

    end2 = time.time()
    print(f"Generated in {str(end - start)[:5]}")
    print(f"Solved in {str(end2 - start2)[:5]}")
    af = input()
