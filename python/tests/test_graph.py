import pytest

from code_challenges.graph.graph import  Graph, Vertex

def test_add_node():
  graph = Graph()
  expected = "test"
  actual = graph.add_node('test').value
  assert actual == expected

def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)
def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44

def test_breadth_one():
    graph = Graph()
    Pandora = graph.add_node('Pandora')
    Arendelle = graph.add_node('Arendelle')
    Metroville = graph.add_node('Metroville')
    Monstroplolis = graph.add_node('Monstroplolis')
    Narnia = graph.add_node('Narnia')
    Naboo = graph.add_node('Naboo')

    graph.add_edge(Pandora,Arendelle)
    graph.add_edge(Arendelle,Metroville)
    graph.add_edge(Arendelle,Monstroplolis)
    graph.add_edge(Metroville,Monstroplolis)
    graph.add_edge(Metroville,Narnia)
    graph.add_edge(Metroville,Naboo)
    graph.add_edge(Monstroplolis,Naboo)
    assert graph.breadth_first_search(Pandora) == ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']

def test_trip_one():
    G4 = Graph()
    pandora = G4.add_node('pandora')
    arendelle = G4.add_node('arendelle')
    metroville = G4.add_node('metroville')
    narina = G4.add_node('narina')
    naboo = G4.add_node('naboo')
    manstropolis = G4.add_node('manstropolis')
    G4.add_edge(pandora, arendelle, 150)
    G4.add_edge(pandora, metroville, 82)
    G4.add_edge(arendelle, pandora, 150)
    G4.add_edge(arendelle, metroville, 99)
    G4.add_edge(arendelle, manstropolis, 42)
    G4.add_edge(metroville, pandora, 82)
    G4.add_edge(metroville, arendelle, 99)
    G4.add_edge(metroville, manstropolis, 105)
    G4.add_edge(metroville, naboo, 26)
    G4.add_edge(metroville, narina, 37)
    G4.add_edge(narina, metroville, 37)
    G4.add_edge(narina, naboo, 250)
    G4.add_edge(naboo, narina, 250)
    G4.add_edge(naboo, metroville, 26)
    G4.add_edge(naboo, manstropolis, 73)
    G4.add_edge(manstropolis, naboo, 73)
    G4.add_edge(manstropolis, arendelle, 42)
    G4.add_edge(manstropolis, metroville, 105)
    assert G4.businesstrip( [naboo, pandora]) == "False,$0"

def test_trip_two():
    G4 = Graph()
    pandora = G4.add_node('pandora')
    arendelle = G4.add_node('arendelle')
    metroville = G4.add_node('metroville')
    narina = G4.add_node('narina')
    naboo = G4.add_node('naboo')
    manstropolis = G4.add_node('manstropolis')
    G4.add_edge(pandora, arendelle, 150)
    G4.add_edge(pandora, metroville, 82)
    G4.add_edge(arendelle, pandora, 150)
    G4.add_edge(arendelle, metroville, 99)
    G4.add_edge(arendelle, manstropolis, 42)
    G4.add_edge(metroville, pandora, 82)
    G4.add_edge(metroville, arendelle, 99)
    G4.add_edge(metroville, manstropolis, 105)
    G4.add_edge(metroville, naboo, 26)
    G4.add_edge(metroville, narina, 37)
    G4.add_edge(narina, metroville, 37)
    G4.add_edge(narina, naboo, 250)
    G4.add_edge(naboo, narina, 250)
    G4.add_edge(naboo, metroville, 26)
    G4.add_edge(naboo, manstropolis, 73)
    G4.add_edge(manstropolis, naboo, 73)
    G4.add_edge(manstropolis, arendelle, 42)
    G4.add_edge(manstropolis, metroville, 105)
    assert G4.businesstrip([pandora, arendelle, metroville]) == "True,$249"

def test_trip_three():
    G4 = Graph()
    pandora = G4.add_node('pandora')
    arendelle = G4.add_node('arendelle')
    metroville = G4.add_node('metroville')
    narina = G4.add_node('narina')
    naboo = G4.add_node('naboo')
    manstropolis = G4.add_node('manstropolis')
    G4.add_edge(pandora, arendelle, 150)
    G4.add_edge(pandora, metroville, 82)
    G4.add_edge(arendelle, pandora, 150)
    G4.add_edge(arendelle, metroville, 99)
    G4.add_edge(arendelle, manstropolis, 42)
    G4.add_edge(metroville, pandora, 82)
    G4.add_edge(metroville, arendelle, 99)
    G4.add_edge(metroville, manstropolis, 105)
    G4.add_edge(metroville, naboo, 26)
    G4.add_edge(metroville, narina, 37)
    G4.add_edge(narina, metroville, 37)
    G4.add_edge(narina, naboo, 250)
    G4.add_edge(naboo, narina, 250)
    G4.add_edge(naboo, metroville, 26)
    G4.add_edge(naboo, manstropolis, 73)
    G4.add_edge(manstropolis, naboo, 73)
    G4.add_edge(manstropolis, arendelle, 42)
    G4.add_edge(manstropolis, metroville, 105)
    assert G4.businesstrip([pandora, metroville]) == "True,$82"
