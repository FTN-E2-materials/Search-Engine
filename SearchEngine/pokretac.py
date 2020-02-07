"""
Modul koji predstavlja pokretacki deo aplikacije.

"""

from SearchEngine.parserTrie.proveriRec import *
from SearchEngine.set import *
from SearchEngine.parserTrie.loadTriefromHTML import loadTrieViaHTML
from SearchEngine.parserTrie.Tree import *
import fnmatch, re
from SearchEngine.parserTrie.Parser import *
from SearchEngine.parserGraph.loadGraphFromParser import loadGraphFromParser


if __name__ == '__main__':
    globalResultSet = Set('')
    stablo = Tree()
    unos = ''
    # petlja ce da se izvrsava sve dok korisnik ne unese nesto
    while unos == '':
        regexPattern1 = fnmatch.translate('[A-Z]:\*')
        regexPattern2 = fnmatch.translate('/*')
        # Kompajlujemo objekat na kom kasnije mozemo da vrsimo regex metode
        regexObj1 = re.compile(regexPattern1)
        regexObj2 = re.compile(regexPattern2)
        print("Unesite putanju korenskog direktorijuma u okviru kojeg zelite da pretrazujete:")
        unos = input()
        if unos != '':  # Mora prvo ova provera zato sto regex.match puca ako mu se prosledi prazan string
            if regexObj1.match(unos) or regexObj2.match(unos):
                print("Validna putanja!")
                stablo = loadTrieViaHTML(unos)

                g = loadGraphFromParser(unos)
                V = g.vertices()
                # dokumenti koji imaju link ka dokumentu X,dokumenti ka kojima dokument X ima link i proizvoljne informacije
                for v in V:
                    print("--------------- DOKUMENT: ", v , " ---------------" )

                    print("DOKUMENTI KOJI IMAJU LINKA KA TOM DOKUMENTU: ")
                    for e in g.edges():
                        if str(v) == str(e._destination):
                            print(str(e._origin))
            else:
                print("Putanja nije validna!")
                unos = ''

    unosUpit = ''
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

    # print(unosUpit)
    unesene_reci = unosUpit.split()
    # print(unesene_reci)
    if 'and' in unesene_reci:
        # print("IMAMO AND OPERATOR")
        index = unesene_reci.index('and')
        unesene_reci.remove('and')
        """
        Preko indeksa znam koja 2 elementa iz liste, trebaju obavezno da budu prilikom pretrage.
        t1,t2 - Tuple u kome cuvamo [uspesnost_trazenja, broj_pojavljivanja]
        """
        print(unesene_reci)

        t1 = find_prefix(stablo.root, unesene_reci[index - 1])
        t2 = find_prefix(stablo.root, unesene_reci[index])
        # print("Imamo " + str(t1[1]) + " pojavljivanja reci " + unesene_reci[index-1] + " u fajlu \"TRENUTNO_NE_ZNAMO.html\"")
        # print("Imamo " + str(t2[1]) + " pojavljivanja reci " + unesene_reci[index]+ " u fajlu \"TRENUTNO_NE_ZNAMO.html\"")
        if (t1[0] == True and t2[0] == True):
            print("Obe reci su se pojavile!!!!")
            setPodatka = Set('')
            resultSet = proveriReciAND(setPodatka, unos, unesene_reci[index - 1], unesene_reci[index])
            globalResultSet=resultSet
            print("\t\t\t\t\t --------------------------------------------------------------------------------- REZULTAT PRETRAGE -----------------------------------------------------------------------------------")
            for elem in iter(resultSet):
                print("\t\t\t\t\t  " + elem)
            print("\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t Pojavljuje se na " + str(len(resultSet)) + " stranica")
            print("\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        else:
            print("Error: Nisu se obe reci pojavile!!")

    elif 'not' in unesene_reci:
        print("IMAMO NOT OPERATOR")
        index = unesene_reci.index('not')
        unesene_reci.remove('not')

        resultSet = Set('')
        resultSet = proveriReciNOT(resultSet, unos, unesene_reci[index - 1], unesene_reci[index])
        globalResultSet = resultSet
        print("\t\t\t\t\t --------------------------------------------------------------------------------- REZULTAT PRETRAGE -----------------------------------------------------------------------------------")
        for elem in iter(resultSet):
            print("\t\t\t\t\t  " + elem)
        print("\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t Pojavljuje se na " + str(len(resultSet)) +" stranica")
        print("\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        # TODO: implementirati pretragu koja zahteva da prva ( leva rec u listi) bude u fajlu a druga ( desna u listi) ne
    elif 'or' in unesene_reci:
        index = unesene_reci.index('or')
        unesene_reci.remove('or')

        t1 = find_prefix(stablo.root, unesene_reci[index - 1])
        t2 = find_prefix(stablo.root, unesene_reci[index])

        if (t1[0] == True or t2[0] == True):
            setPodatka = Set('')
            resultSet = Set('')
            if (t1[0] == True and t2[0] == True):
                resultSet = proveriReciAND(setPodatka, unos, unesene_reci[index - 1], unesene_reci[index])
            elif (t1[0] == True and t2[0] == False):
                resultSet = proveriRecOR(setPodatka, unos, unesene_reci[index - 1])
            elif (t1[0] == False and t2[0] == True):
                resultSet = proveriRecOR(setPodatka, unos, unesene_reci[index])

            print("\t\t\t\t\t --------------------------------------------------------------------------------- REZULTAT PRETRAGE -----------------------------------------------------------------------------------")
            for elem in iter(resultSet):
                print("\t\t\t\t\t  " + elem)
            print("\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("\t\t\t\t\t Pojavljuje/u se na " + str(len(resultSet)) + " stranica")
            print("\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            globalResultSet = resultSet
        else:
            print("Error: Obe reci se uopste nisu pojavile!!")

    else:
        # print("NEMAMO NI JEDAN OPERATOR")
        resultSet = Set('')
        pojavljivane_reci = []
        for i in range(len(unesene_reci)):
            t = find_prefix(stablo.root, unesene_reci[i])
            if (t[0] == True):
                pojavljivane_reci.append(unesene_reci[i])
                resultSet = proveriRecOR(resultSet, unos, unesene_reci[i])


        print("\t\t\t\t\t --------------------------------------------------------------------------------- REZULTAT PRETRAGE -----------------------------------------------------------------------------------")
        for elem in iter(resultSet):
            print("\t\t\t\t\t  " + elem)

        print("\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t Reci koje su se zapravo pojavile su: " + str(pojavljivane_reci))
        print("\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\t\t Pojavljuje/u se na " + str(len(resultSet)) + " stranica")
        print("\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        globalResultSet = resultSet


    def takeSecond(elem):
        return elem[1]

    #RANGIRANJE PRETRAGE
    #print(globalResultSet)
    rankedStructure = [] #[ [elementizPretrage1, backlinks], [elementizPretrage2, backlinks]....]
    for element in iter(globalResultSet):
        #za svaki element iz pretrage treba naci koliko cvorova pokazuje na njega u grafu
        backlinks = 0 #za svaki element iz pretrage restartujemo broj backlinkova
        #print("ELEMENT:", element)
        for e in g.edges():
            #print("GRANA:", e._destination)
            if str(e._destination) == element:
                backlinks = backlinks + 1
        rank = [element, backlinks]
        rankedStructure.append(rank)
    rankedStructure.sort(reverse=True,key=takeSecond)
    print(rankedStructure)

    print("\t\t\t\t\t --------------------------------------------------------------------------------- REZULTAT RANGIRANE PRETRAGE -----------------------------------------------------------------------------------")
    for elem in iter(rankedStructure):
        print("\t\t\t\t\t  " , elem[0])

    print(
        "\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t Reci koje su se zapravo pojavile su: " + str(pojavljivane_reci))
    print(
        "\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t Pojavljuje/u se na " + str(len(resultSet)) + " stranica")
    print(
        "\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    globalResultSet = resultSet




