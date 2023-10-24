class Graph:
    def __init__(self):  # конструктор для инициализации объектов
        self.adj_list = {}  # словарь хранения списка смежности
        self.visited = {}  # словарь для отметки о посещенных вершинах
        self.low = {}  # словарь для минимального времени захода среди вершин, достижимых из текущей или из ее потомков
        self.source = {}  # словарь для отслеживания времени захода обхода графа в текущую вершину
        self.timer = 0  # одной единицей времени этого таймера будет один заход обхода в глубину в определенную вершину

    def first(self, v):  # индекс первой вершины, смежной с вершиной v
        if v in self.adj_list:
            neighbors = list(self.adj_list[v].keys())
            if neighbors:
                return neighbors[0]
        return 0

    def next(self, v, i):  # индекс вершины, смежной с вершиной v, следующей за индексом i
        if v in self.adj_list and i in self.adj_list[v]:
            neighbors = list(self.adj_list[v].keys())
            index = neighbors.index(i)
            if index < len(neighbors) - 1:
                return neighbors[index + 1]
        return 0

    def vertex(self, v, i):  # вершина с индексом i из множества вершин, смежных с v
        if v in self.adj_list and i in self.adj_list[v]:
            return i

    def del_v(self, vertex):  # удаление вершины и всех принадлежащих ребер из графа
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for v in self.adj_list:
                if vertex in self.adj_list[v]:
                    del self.adj_list[v][vertex]

    def del_e(self, v1, v2):  # удаление ребра между вершинами v и w
        if v1 in self.adj_list and v2 in self.adj_list[v1]:
            del self.adj_list[v1][v2]
            del self.adj_list[v2][v1]

    def edit_v(self, old_v, new_v):  # изменение имени вершины
        if old_v in self.adj_list:
            neighbors = self.adj_list[old_v]
            self.adj_list[new_v] = neighbors
            del self.adj_list[old_v]
            for v in self.adj_list:
                if old_v in self.adj_list[v]:
                    self.adj_list[v][new_v] = self.adj_list[v].pop(old_v)

    def edit_e(self, v1, v2, new_weight):  # изменение веса ребра
        self.add_e(v1, v2, new_weight)

    def add_v(self, v):  # добавление вершины
        if v not in self.adj_list:
            self.adj_list[v] = {}

    def add_e(self, v1, v2, weight):  # добавление ребра
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1][v2] = weight
            self.adj_list[v2][v1] = weight

    def dfs(self, v, parent):  # выполнение поиска в глубину
        self.visited[v] = True
        self.source[v] = self.timer
        self.low[v] = self.timer
        self.timer += 1

        for neighbor in self.adj_list[v]:
            if not self.visited[neighbor]:
                parent[neighbor] = v
                self.dfs(neighbor, parent)
                self.low[v] = min(self.low[v], self.low[neighbor])
                if self.low[neighbor] > self.source[v]:
                    print(f"Найденный мост: {v} - {neighbor}")
            elif neighbor != parent[v]:
                self.low[v] = min(self.low[v], self.source[neighbor])

    def find_bridges(self):  # поиск постов в графе
        self.visited = {v: False for v in self.adj_list}
        self.source = {v: float('inf') for v in self.adj_list}
        self.low = {v: float('inf') for v in self.adj_list}
        parent = {v: None for v in self.adj_list}

        for v in self.adj_list:
            if not self.visited[v]:
                self.dfs(v, parent)

    def __str__(self):  # строковое представление графа
        result = ""
        for vertex, neighbors in self.adj_list.items():
            result += f"{vertex}: {neighbors}\n"
        return result


if __name__ == "__main__":
    g = Graph()
    g.add_v('1')
    g.add_v('2')
    g.add_v('3')
    g.add_v('4')
    g.add_v('5')
    g.add_v('6')
    g.add_e('1', '2', 1)
    g.add_e('1', '3', 2)
    g.add_e('2', '3', 3)
    g.add_e('3', '4', 4)
    g.add_e('4', '5', 5)
    g.add_e('4', '6', 6)
    g.add_e('5', '6', 7)
    print(g)
    g.find_bridges()

    print(g.first('1'))  # выведет '2'
    print(g.next('1', '2'))  # выведет '3'
    print(g.vertex('1', '2'))  # выведет '2'
    g.del_v('2')  # удалит вершину '2'
    g.del_e('1', '3')  # удалит дугу '1'-'3'
    g.edit_v('1', 'NNN')  # поменяет название вершины '1'
    g.edit_e('4', '5', 99)  # поменяет вес дуги '4' - '5' на 99
    print(g)
