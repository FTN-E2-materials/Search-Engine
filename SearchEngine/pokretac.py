"""
Modul koji predstavlja pokretacki deo aplikacije.

"""
from Graph import Graph
from tree import *


def graph_from_edgelist(E, directed=False):
    """Kreira graf od ivica.

  Dozvoljeno je dva načina navođenje ivica:
        (origin,destination)
        (origin,destination,element).
  Podrazumeva se da se labele čvorova mogu hešovati.
  """
    g = Graph(directed)
    V = set()
    for e in E:
        V.add(e[0])
        V.add(e[1])

    vertices = {}  # izbegavamo ponavljanje labela između čvorova
    for v in V:
        vertices[v] = g.insert_vertex(v)

    for e in E:
        src = e[0]
        dest = e[1]
        element = e[2] if len(e) > 2 else None
        g.insert_edge(vertices[src], vertices[dest], element)

    return g


def figure_14_15():
    """Vraća težinski, neusmeren graf."""
    E = (
        ('SFO', 'LAX', 337), ('SFO', 'BOS', 2704), ('SFO', 'ORD', 1846),
        ('SFO', 'DFW', 1464), ('LAX', 'DFW', 1235), ('LAX', 'MIA', 2342),
        ('DFW', 'ORD', 802), ('DFW', 'JFK', 1391), ('DFW', 'MIA', 1121),
        ('ORD', 'BOS', 867), ('ORD', 'PVD', 849), ('ORD', 'JFK', 740),
        ('ORD', 'BWI', 621), ('MIA', 'BWI', 946), ('MIA', 'JFK', 1090),
        ('MIA', 'BOS', 1258), ('BWI', 'JFK', 184), ('JFK', 'PVD', 144),
        ('JFK', 'BOS', 187),
    )
    return graph_from_edgelist(E, False)


if __name__ == '__main__':

    # instanca stabla
    t = Tree()
    t.root = TreeNode(0)

    # kreiranje relacija između novih čvorova
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    a.add_child(b)
    t.root.add_child(a)
    t.root.add_child(c)

    # visina stabla
    print('Visina = %d' % t.height(t.root))

    # dubina čvora
    print('Dubina(a) = %d' % t.depth(a))

    # obilazak po dubini - preorder
    print('PREORDER')
    t.preorder(t.root)

    # obilazak po dubini - postorder
    print('POSTORDER')
    t.postorder(t.root)

    # obilazak po širini
    print('BREADTH FIRST')
    t.breadth_first()

    print("ITER")
    for node in t:
        print(node)

    # Testiranje grafa , ispisivanje svih cvorova
    graf = figure_14_15()
    for v in graf.vertices():
        print(v)

    # Testiranje grafa , ispisivanje svih cvorova
    for e in graf.edges():
        print(e)
