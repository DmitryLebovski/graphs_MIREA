# Мостом графа G называется каждое ребро, удаление которого приводит к увеличению числа связных компонент графа.
# Представить алгоритм нахождения всех мостов графа.

# Список смежности

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.used = {}
        self.low = {}
        self.timer = 0
        self.bridges = []

    def add_v(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}

    def add_e(self, vertex1, vertex2, weight):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1][vertex2] = weight
            self.adj_list[vertex2][vertex1] = weight  # For an undirected graph

    def find_bridges(self):
        self.used = {v: False for v in self.adj_list}
        self.low = {v: -1 for v in self.adj_list}
        self.timer = 0
        self.bridges = []

        for v in self.adj_list:
            if not self.used[v]:
                self.dfs(v, None)

        return self.bridges

    def dfs(self, v, parent):
        self.used[v] = True
        self.low[v] = self.timer
        self.timer += 1

        for neighbor in self.adj_list[v]:
            if not self.used[neighbor]:
                self.dfs(neighbor, v)
                self.low[v] = min(self.low[v], self.low[neighbor])
                if self.low[neighbor] > self.used[v]:
                    self.bridges.append((v, neighbor))
            elif neighbor != parent:
                self.low[v] = min(self.low[v], self.used[neighbor])

    def __str__(self):
        result = ""
        for vertex, weight in self.adj_list.items():
            result += f"{vertex}: {weight}\n"
        return result


if __name__ == "__main__":
    g = Graph()
    g.add_v('A')
    g.add_v('B')
    g.add_v('C')
    g.add_v('D')
    g.add_e('A', 'B', 1)
    g.add_e('A', 'C', 2)
    g.add_e('C', 'D', 3)

    print(g)

    bridges = g.find_bridges()
    print("Bridges in the graph:")
    for bridge in bridges:
        print(bridge)

#
# 0: [1, 2]
# 1: [0, 2, 3]
# 2: [0, 1, 4]
# 3: [1]
# 4: [2, 5]
# 5: [4]