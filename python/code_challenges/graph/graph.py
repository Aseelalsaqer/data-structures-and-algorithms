from collections import deque


class Vertex:
    """
  Class for Adding a node to the graph
  Arguments: value
  Returns: The added node
  """
    def __init__(self, value):
        """
    Initalization for a Vertex to hold a value.

    """
        self.value = value


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        print(type(self.dq.pop()))

    def __len__(self):
        return len(self.dq)


class Stack:
    def __init__(self):
        """
		The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
		"""
        self.dq = deque()

    def push(self, value):
        """
		Store the passed value in a node and then push the node on top of the stack.

		PARAMETERS
		----------
			value: any
				The value that will get stored in a node to be pushed on top of the stack.
		"""
        self.dq.append(value)

    def pop(self):
        """
		Return the top node in a stack.
		"""
        self.dq.pop()


class Edge:
    """
    a class for Adding a new edge between two result in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 result to be connected by the edge, weight (optional)
    Returns: nothing

  """
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        """
    Initalization for a hashmap to hold the vertices
    """
        self.__adjacency_list = {}

    def add_node(self, value):
        """
      Method for Adding a node to the graph
      Arguments: value
      Returns: The added node
    """
        # new node
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_result(self):
        """
    Method to get all result in Graph
    Arguments: None
    return: All result
    """
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        """ """
        return self.__adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex, action=(lambda vertex: None)):
        queue = []
        visited = set()
        result = []

        queue.append(start_vertex)
        visited.add(start_vertex)

        while len(queue):

                current_vertex = queue.pop(0)
                result.append(current_vertex.value)
                action(current_vertex)
                neighbors = self.get_neighbors(current_vertex)

                for edge in neighbors:
                    neighbor = edge.vertex
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return result

    def businesstrip(Graph,array):
        path1 = False
        path2 = False
        total = 0
        for vertex in range(len(array) - 1):
            adjacency = Graph.__adjacency_list[array[vertex]]
            path2 = False
            for edges in adjacency:
                if array[vertex + 1] == edges.vertex:
                    total += edges.weight
                    path1 = True
                    path2 = True
        path = path1 and path2
        if not path:
            total = 0
            path = False
            return f'{path},${total}'
        return f'{path},${total}'

    def depthfirst(self, ver):
        finalresult = []
        finalresult.append(ver.value)
        if ver not in self.__adjacency_list:
            return 'vertex not found in graph '
        elif self.__adjacency_list[ver] == []:
            return 'verteix has no adjecent'
        def oredering(ver):
            neighbors = self.__adjacency_list[ver]
            for edge in neighbors:
                vertces = edge.vertex.value

                if vertces not in finalresult:
                    finalresult.append(vertces)
                    oredering(edge.vertex)
        oredering(ver)
        return finalresult
# graph = Graph()


# Pandora = graph.add_node('Pandora')
# Arendelle = graph.add_node('Arendelle')
# Metroville = graph.add_node('Metroville')
# Monstroplolis = graph.add_node('Monstroplolis')
# Narnia = graph.add_node('Narnia')
# Naboo = graph.add_node('Naboo')

# graph.add_edge(Pandora,Arendelle)
# graph.add_edge(Arendelle,Metroville)
# graph.add_edge(Arendelle,Monstroplolis)
# graph.add_edge(Metroville,Monstroplolis)
# graph.add_edge(Metroville,Narnia)
# graph.add_edge(Metroville,Naboo)
# graph.add_edge(Monstroplolis,Naboo)




# print(graph.breadth_first_search(Pandora))
# G4 = Graph()
# pandora = G4.add_node('pandora')
# arendelle = G4.add_node('arendelle')
# metroville = G4.add_node('metroville')
# narina = G4.add_node('narina')
# naboo = G4.add_node('naboo')
# manstropolis = G4.add_node('manstropolis')
# G4.add_edge(pandora, arendelle, 150)
# G4.add_edge(pandora, metroville, 82)
# G4.add_edge(arendelle, pandora, 150)
# G4.add_edge(arendelle, metroville, 99)
# G4.add_edge(arendelle, manstropolis, 42)
# G4.add_edge(metroville, pandora, 82)
# G4.add_edge(metroville, arendelle, 99)
# G4.add_edge(metroville, manstropolis, 105)
# G4.add_edge(metroville, naboo, 26)
# G4.add_edge(metroville, narina, 37)
# G4.add_edge(narina, metroville, 37)
# G4.add_edge(narina, naboo, 250)
# G4.add_edge(naboo, narina, 250)
# G4.add_edge(naboo, metroville, 26)
# G4.add_edge(naboo, manstropolis, 73)
# G4.add_edge(manstropolis, naboo, 73)
# G4.add_edge(manstropolis, arendelle, 42)
# G4.add_edge(manstropolis, metroville, 105)

# print(G4.businesstrip([metroville,pandora]))

G5 = Graph()
a = G5.add_node('a')
b = G5.add_node('b')
c = G5.add_node('c')
d = G5.add_node('d')
e = G5.add_node('e')
f = G5.add_node('f')
G5.add_edge(a, d)
G5.add_edge(a, c)
G5.add_edge(c, a)
G5.add_edge(b, d)
G5.add_edge(d, b)
G5.add_edge(d, e)
print(G5.depthfirst(a))

