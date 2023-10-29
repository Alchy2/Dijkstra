graph = [0, 4, 1, 0], [4, 0, 2, 0], [1, 2, 0, 3], [0, 0, 3, 0]
def Dijkstra (graph, start):
    vertices = [[i, 0 if i == start else float('inf'), None] for i in range(len(graph))]
    visitedVertices = []
    lowestVal = float('inf')
    currentVertex = 0
    for i in range (len(graph)):
        for j in range (len(graph)):
            if vertices[j][1] < lowestVal and (j not in visitedVertices):
                lowestVal = vertices[j][1]
                currentVertex = j
        for k in range (len(graph[currentVertex])):
            if (graph[currentVertex][k]) > 0:
                if (graph[currentVertex][k]) + vertices[currentVertex][1] < vertices[k][1]:
                    vertices[k][1] = (graph[currentVertex][k]) + vertices[currentVertex][1]
                    vertices[k][2] = currentVertex
        visitedVertices.append(currentVertex)
        lowestVal = float('inf')
    return vertices
print (Dijkstra(graph, 0))