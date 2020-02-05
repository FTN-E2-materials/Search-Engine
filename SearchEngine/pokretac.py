"""
Modul koji predstavlja pokretacki deo aplikacije.

"""
from Graph import Graph
from parserTrie.loadTriefromHTML import loadTrieViaHTML
from parserTrie.Tree import *
import fnmatch, re
from set import Set


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
    stablo = Tree()
    # C:\Users\Vaxi\Desktop\Desktop\FAKS\3 godina\5-semestar\OISISI-Projekat[Python]\OISISI-drugi-projektni-zadatak\SearchEngine
    # C:\Users\Vaxi\Desktop\Desktop\FAKS\3 godina\5-semestar\OISISI-Projekat[Python]\OISISI-drugi-projektni-zadatak\SearchEngine\test-skup\python-2.7.7-docs-html\tutorial
    unos = ''
    #petlja ce da se izvrsava sve dok korisnik ne unese nesto
    while unos == '':
        regexPattern1 = fnmatch.translate('[A-Z]:\*')
        regexPattern2 = fnmatch.translate('/*')
        # Kompajlujemo objekat na kom kasnije mozemo da vrsimo regex metode
        regexObj1 = re.compile(regexPattern1)
        regexObj2 = re.compile(regexPattern2)
        print("Unesite putanju korenskog direktorijuma u okviru kojeg zelite da pretrazujete:")
        unos = input()
        if unos!='': #Mora prvo ova provera zato sto regex.match puca ako mu se prosledi prazan string
            if regexObj1.match(unos) or regexObj2.match(unos):
               print("Validna putanja!")
               stablo = loadTrieViaHTML(unos)
            else:
               print("Putanja nije validna!")
               unos = ''

    # obilazak po dubini - preorder
    print('PREORDER')
    stablo.preorder(stablo.root)

    #Testiranje set-a i magicnih metoda
    a = Set(["pufke", "vladislav"])
    b = Set(["pufke", "ana"])

    c = a | b
    print(c)

    # # instanca stabla
    # t = Tree()
    # t.root = TreeNode(0)

    # # kreiranje relacija između novih čvorova
    # a = TreeNode(1)
    # b = TreeNode(2)
    # c = TreeNode(3)