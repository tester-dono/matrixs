# TODO принимает матрицусмежности возвращает логическое значение является ли двудольной матрица или нетdef bipart(x, node, visited, set1, set2):
# Программа Python, чтобы узнать, является ли
# данный график является двудольным или нет


class Graph():

    def __init__(self, V):

        self.V = V

        self.graph = [[0 for column in range(V)] \
 \
                      for row in range(V)]
    # Эта функция возвращает true, если граф G [V] [V]
    # является двудольным, иначе ложным
    def isBipartite(self, src):
        # Создайте массив цветов для хранения цветов
        # присваивается всем вершинам. темя
        # Номер  # используется в качестве индекса в этом массиве.
        # Значение '-1' colorArr [i] используется для
        # означает, что цвет не назначен
        # вершина 'i'. Значение 1 используется для указания
        # назначен первый цвет и значение 0
        # указывает, что назначен второй цвет.
        colorArr = [-1] * self.V
        # Назначить первый цвет источнику
        colorArr[src] = 1
        # Создать очередь (FIFO) номеров вершин и
        # поставить в очередь исходную вершину для обхода BFS
        queue = []
        queue.append(src)
        # Запускать, пока в очереди есть вершины
        # (Аналогично BFS)
        while queue:
            u = queue.pop()
            # Вернуть false, если есть цикл
            if self.graph[u][u] == 1:
                return False;
            for v in range(self.V):
                # Существует ребро от u до v и пункт назначения
                # v не окрашен
                if self.graph[u][v] == 1 and colorArr[v] == -1:
                    # Назначьте альтернативный цвет этому
                    # рядом с тобой
                    colorArr[v] = 1 - colorArr[u]
                    queue.append(v)
                # Существует ребро от u до v и пункт назначения
                # v окрашен тем же цветом, что и вы
                elif self.graph[u][v] == 1 and colorArr[v] == colorArr[u]:
                    return False
        # Если мы доберемся сюда, то все смежные
        # вершины могут быть закрашены альтернативными
        # цвет
        return True


# Программа драйвера для проверки вышеуказанной функции
g = Graph(4)
g.graph = [[0, 1, 0, 1],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [1, 0, 1, 0]
           ]

print ("Yes" if g.isBipartite(0) else "No")

# Этот код предоставлен Divyanshu Mehta
