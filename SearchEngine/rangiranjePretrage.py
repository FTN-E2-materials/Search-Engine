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
def rangiranjePretrage(globalResultSet,dokumentiKojiImajuLinkKaDokumentu,bekLinkovi, unesene_reci):
    rankedStructure = [] #[ [elementizPretrage1, poeni1], [elementizPretrage2, poeni2]....]
    for element in iter(globalResultSet):

        brojponavljanjaReciuDatotekamaKojeLinkuju = 0
        for z in dokumentiKojiImajuLinkKaDokumentu[element]:
            for ureci in unesene_reci:
                if ureci.lower() not in ['and', 'or', 'not']:
                    brojponavljanjaReciuDatotekamaKojeLinkuju = brojponavljanjaReciuDatotekamaKojeLinkuju + brojPonavaljanjaReciuDatoteci(z, ureci)

        for urecii in unesene_reci:
            brojponavljanjaReci = brojPonavaljanjaReciuDatoteci(element, urecii)


        rank = [element, bekLinkovi[element] + (brojponavljanjaReci*0.7) + (brojponavljanjaReciuDatotekamaKojeLinkuju*0.4)]
        rankedStructure.append(rank)

    #Samostalna implementacija algoritma za sortiranje u metodi quickSort)
    n = len(rankedStructure)
    quickSort(rankedStructure, 0, n - 1)

    povratniSet = Set('')
    for element in rankedStructure:
        povratniSet.elements.append(element[0])
        povratniSet.listaPoena.append(element[1])

    return povratniSet
