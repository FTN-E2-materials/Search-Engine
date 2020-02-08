from quickSortMultiList import quickSort
from parserGraph.Parser import Parser
from set import Set
import time

def brojPonavaljanjaReciuDatoteci(datoteka, rec: str):
    parser = Parser()
    parser.parse(datoteka)
    brojPonavljanja = 0

    for word in parser.words:
        if rec.lower() == word.lower():
            brojPonavljanja = brojPonavljanja + 1

    return brojPonavljanja


# RANGIRANJE PRETRAGE
def rangiranjePretrage(globalResultSet,dokumentiKojiImajuLinkKaDokumentu, unesene_reci,g):
    rankedStructure = [] #[ [elementizPretrage1, poeni1], [elementizPretrage2, poeni2]....]
    for element in iter(globalResultSet):
        # za svaki element iz pretrage treba naci koliko cvorova pokazuje na njega u grafu
        backlinks = 0 #za svaki element iz pretrage restartujemo broj backlinkova
        for e in g.edges():
            if str(e._destination) == element:
                backlinks = backlinks + 1

        brojponavljanjaReciuDatotekamaKojeLinkuju = 0
        for x in dokumentiKojiImajuLinkKaDokumentu:
            if str(x[0]) == element:
                for z in x[1]:
                    for ureci in unesene_reci:
                        brojponavljanjaReciuDatotekamaKojeLinkuju = brojponavljanjaReciuDatotekamaKojeLinkuju + brojPonavaljanjaReciuDatoteci(z, ureci)

        for urecii in unesene_reci:
            brojponavljanjaReci = brojPonavaljanjaReciuDatoteci(element, urecii)


        rank = [element, backlinks + (brojponavljanjaReci*0.7) + (brojponavljanjaReciuDatotekamaKojeLinkuju*0.4)]
        rankedStructure.append(rank)

    #Samostalna implementacija algoritma za sortiranje u metodi quickSort
    start = time.time()
    n = len(rankedStructure)
    quickSort(rankedStructure, 0, n - 1)
    end = time.time()
    print("QuickSort " + str((end - start).__round__(5)) + " seconds.")

    povratniSet = Set('')
    for element in rankedStructure:
        povratniSet.elements.append(element[0])
        povratniSet.listaPoena.append(element[1])

    return povratniSet
