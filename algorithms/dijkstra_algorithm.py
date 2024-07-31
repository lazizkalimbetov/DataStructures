import heapq

class Graph:
    '''
    Eng qisqa va tez yo'lni topishga qaratilgan algoritm
    '''

    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, weight))

def dijkstra(graph, source):
    distance = [float('inf')] * len(graph)
    distance[source] = 0
    pq = [(0, source)]  # Приоритетная очередь (расстояние, вершина)

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distance[current_vertex]:
            continue  # Устаревшая вершина

        for neighbor, weight in graph.edges[current_vertex]:
            distance_through_current_vertex = current_distance + weight
            if distance_through_current_vertex < distance[neighbor]:
                distance[neighbor] = distance_through_current_vertex
                heapq.heappush(pq, (distance_through_current_vertex, neighbor))

    return distance

# Пример использования
graph = Graph()
graph.add_edge(0, 1, 4)
graph.add_edge(0, 2, 2)
graph.add_edge(1, 2, 3)
graph.add_edge(2, 3, 6)
graph.add_edge(3, 0, 1)

distances = dijkstra(graph, 0)
print(distances)


# Вывод:
# [0, 4, 2, 9]
