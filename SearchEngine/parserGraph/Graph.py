class Graph:

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    class Vertex:
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'

        def __init__(self, x):
            """Do not call constructor directly.
            Use Graph's insert_vertex(x).
            """
            self._element = x

        def element(self):
            """Return element associated with this vertex."""
            return self._element

        def __hash__(self):  # will allow vertex to be a map/set key
            return hash(id(self))

        def __str__(self):
            return str(self._element)

    class Edge:
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return (self._origin, self._destination)

        def opposite(self, v):
            if not isinstance(v, Graph.Vertex):
                raise TypeError('v must be a Vertex')
            return self._destination if v is self._origin else self._origin
            raise ValueError('v not incident to edge')

        def element(self):
            return self._element

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._element)

    def _validate_vertex(self, v):
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex expected')
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)  # returns None if v not adjacent

    def degree(self, v, outgoing=True):
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # need distinct map for incoming edges
        return v

    def insert_edge(self, u, v, x=None):
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e


def add_elements_to_Graph(E, directed=True):
    """Kreira graf od ivica.

  Dozvoljeno je dva načina navođenje ivica:
        (origin,destination)
        (origin,destination,element).
  Podrazumeva se da se labele čvorova mogu hešovati.
  """
    dokumentiKaDokumentuX = dict()
    dokumentiKaKojimaDokumentXImaLink = dict()

    cvoroviPocetka = dict()                     # dvojka [ dokumentX, listaDokumenata_koja_pokazuju_na_njega]
    cvoroviKraja = dict()                       # dvojka [ dokumentX, listaDokumenata_ka_kojima_on_pokazuje]
    bekLinkovi = {}
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

        if str(vertices[src]) not in cvoroviKraja:
            #print(str(src) + "[source] nije u cvorovima kraja pa ga kreiramo")
            cvoroviKraja[str(vertices[src])] = []
            #bekLinkovi[str(dest)] = 1
        #else:
        #print(str(src) + "[source] je vec u cvorovima kraja, pa dodajemo njegove destination")
        if str(vertices[dest]) not in cvoroviKraja[str(vertices[src])]:
            cvoroviKraja[str(vertices[src])].append(str(vertices[dest]))
            #bekLinkovi[str(dest)] += 1




        if str(vertices[dest]) not in cvoroviPocetka:
            cvoroviPocetka[str(vertices[dest])] = []              # pravimo listu cvorova kojima je on sve destination, tj listu onih koji pokazuju na dokument X
            bekLinkovi[str(dest)] = 1
        #else:
        if str(vertices[src]) not in cvoroviPocetka[str(vertices[dest])]:
            cvoroviPocetka[str(vertices[dest])].append(str(vertices[src]))
            bekLinkovi[str(dest)]+=1


        # ZA UBACIVANJE AKO ON SAM NA SEBE LINKUJE
        if str(vertices[src]) not in cvoroviPocetka:
            cvoroviPocetka[str(vertices[src])] = []              # pravimo listu cvorova kojima je on sve destination, tj listu onih koji pokazuju na dokument X
            bekLinkovi[str(src)] = 1
        #else:
        if str(vertices[src]) not in cvoroviPocetka[str(vertices[src])]:
            cvoroviPocetka[str(vertices[src])].append(str(vertices[src]))
            bekLinkovi[str(src)]+=1



    return g, cvoroviPocetka, bekLinkovi


