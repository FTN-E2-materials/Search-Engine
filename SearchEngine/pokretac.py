"""
Modul koji predstavlja pokretacki deo aplikacije.

"""
from Graph import Graph
from parserTrie.loadTriefromHTML import *
from parserTrie.proveriRec import *
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
    # C:\Users\Vaxi\Desktop\Desktop\FAKS\3 godina\5-semestar\OISISI-Projekat[Python]\OISISI-drugi-projektni-zadatak\SearchEngine\test-skup\python-2.7.7-docs-html\AOBRISIOVO
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
               # print("Validna putanja!")
               stablo = loadTrieViaHTML(unos)
            else:
               print("Putanja nije validna!")
               unos = ''

    unosUpit=''
    # petlja ce da se izvrsava sve dok korisnik ne unese nesto
    while unosUpit == '':
        # Kompajlujemo objekat na kom kasnije mozemo da vrsimo regex metode
        regexObj111 = re.compile("(([\w]+\s){1}(and|or|not)(\s[\w]+){1})|([\w\s]+)")

        print("Unesite pretragu:")
        unosUpit = input()
        if unosUpit != '':  # Mora prvo ova provera zato sto regex.match puca ako mu se prosledi prazan string
            if regexObj111.fullmatch(unosUpit):
                print("Uneli ste validnu pretragu.")
            else:
                print("Niste uneli validnu pretragu!")
                unosUpit = ''

    #print(unosUpit)
    unesene_reci = unosUpit.split( )
    #print(unesene_reci)
    if 'and' in unesene_reci:
        # print("IMAMO AND OPERATOR")
        index = unesene_reci.index('and')
        unesene_reci.remove('and')
        """
        Preko indeksa znam koja 2 elementa iz liste, trebaju obavezno da budu prilikom pretrage.
        t1,t2 - Tuple u kome cuvamo [uspesnost_trazenja, broj_pojavljivanja]
        """
        #print(unesene_reci)

        t1=find_prefix(stablo.root, unesene_reci[index-1])
        t2=find_prefix(stablo.root, unesene_reci[index])
        #print("Imamo " + str(t1[1]) + " pojavljivanja reci " + unesene_reci[index-1] + " u fajlu \"TRENUTNO_NE_ZNAMO.html\"")
        #print("Imamo " + str(t2[1]) + " pojavljivanja reci " + unesene_reci[index]+ " u fajlu \"TRENUTNO_NE_ZNAMO.html\"")
        if(t1[0] == True and t2[0] == True):
            #print("Obe reci su se pojavile!!!!")
            setPodatka = Set('')
            resultSet =proveriReciAND(setPodatka,unos,unesene_reci[index-1],unesene_reci[index])
            print("-------------------- REZULTAT PRETRAGE ----------------------")
            for elem in iter(resultSet):
                print("\t\t\t\t\t  "+elem)
            print("-------------------------------------------------------------")
        else:
            print("Error: Nisu se obe reci pojavile!!")

    elif 'not' in unesene_reci:
        print("IMAMO NOT OPERATOR")
        unesene_reci.remove('not')
        # TODO: implementirati pretragu koja zahteva da prva ( leva rec u listi) bude u fajlu a druga ( desna u listi) ne
    elif 'or' in unesene_reci:
        index = unesene_reci.index('or')
        unesene_reci.remove('or')

        t1 = find_prefix(stablo.root, unesene_reci[index - 1])
        t2 = find_prefix(stablo.root, unesene_reci[index])

        if (t1[0] == True or t2[0] == True):
            setPodatka = Set('')
            resultSet = Set('')
            if(t1[0] == True and t2[0] == True):
                print("slucaj1")
                resultSet = proveriReciAND(setPodatka, unos, unesene_reci[index - 1], unesene_reci[index])
            elif(t1[0] == True and t2[0] == False):
                print("slucaj2")
                resultSet = proveriRecOR(setPodatka, unos, unesene_reci[index - 1])
            elif(t1[0] == False and t2[0] == True):
                print("slucaj3")
                resultSet = proveriRecOR(setPodatka, unos, unesene_reci[index])

            print("-------------------- REZULTAT PRETRAGE ----------------------")
            for elem in iter(resultSet):
                print("\t\t\t\t\t  " + elem)
            print("-------------------------------------------------------------")
        else:
            print("Error: Obe reci se uopste nisu pojavile!!")

    else:
        print("NEMAMO NI JEDAN OPERATOR")
        # TODO: implementirati da radi kao or samo da moze vise reci

