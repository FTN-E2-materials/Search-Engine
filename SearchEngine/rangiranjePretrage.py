from quickSortMultiList import quickSort
from parserGraph.Parser import Parser
from set import Set
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
                    # brojponavljanjaReciuDatotekamaKojeLinkuju = brojponavljanjaReciuDatotekamaKojeLinkuju + brojPonavaljanjaReciuDatoteci(z, unesene_reci[0])
                    # if len(unesene_reci) > 1:
                    #     if unesene_reci[0] != unesene_reci[1]:
                    #         brojponavljanjaReciuDatotekamaKojeLinkuju = brojponavljanjaReciuDatotekamaKojeLinkuju + brojPonavaljanjaReciuDatoteci(z, unesene_reci[0])
        for urecii in unesene_reci:
            brojponavljanjaReci = brojPonavaljanjaReciuDatoteci(element, urecii)
        # brojponavljanjaReci = brojPonavaljanjaReciuDatoteci(element, unesene_reci[0])
        # if len(unesene_reci) > 1:
        #     if unesene_reci[0] != unesene_reci[1]:
        #         brojponavljanjaReci = brojPonavaljanjaReciuDatoteci(element, unesene_reci[1])

        rank = [element, backlinks + (brojponavljanjaReci*0.7) + (brojponavljanjaReciuDatotekamaKojeLinkuju*0.4)]
        rankedStructure.append(rank)


    #Kod koji radi ugradjeno sortiranje
    #rankedStructure.sort(reverse=True,key=takeSecond)
    #print(rankedStructure)

    #Samostalna implementacija algoritma za sortiranje u metodi quickSort
    n = len(rankedStructure)
    quickSort(rankedStructure, 0, n - 1)
    #print(rankedStructure)


    povratniSet = Set('')
    for element in rankedStructure:
        povratniSet.elements.append(element[0])
        povratniSet.listaPoena.append(element[1])

    return povratniSet
    # print("\t\t\t\t\t --------------------------------------------------------------------------------- REZULTAT RANGIRANE PRETRAGE -----------------------------------------------------------------------------------")
    # for elem in iter(c):
    #     print("\t\t\t\t\t  " , elem[0])