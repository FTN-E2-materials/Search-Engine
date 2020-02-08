
from pagination import paginacija
from parserTrie.proveriRec import *
from set import *
from parserTrie.loadTriefromHTML import loadTrieViaHTML
from parserTrie.Tree import *
import fnmatch, re
from parserTrie.Parser import *
from parserGraph.loadGraphFromParser import loadGraphFromParser

def pretraga(unesene_reci,stablo,unos):

    if 'and' in unesene_reci:
        if len(unesene_reci) == 3:
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
                globalResultSet = resultSet
                paginacija(resultSet)

            else:
                print("Error: Nisu se obe reci pojavile!!")
        else:
            print("Error: Nije unesena validna pretraga sa and operatorom")
    elif 'not' in unesene_reci:
        if len(unesene_reci) == 3:
            index = unesene_reci.index('not')
            unesene_reci.remove('not')

            resultSet = Set('')
            resultSet = proveriReciNOT(resultSet, unos, unesene_reci[index - 1], unesene_reci[index])
            globalResultSet = resultSet
            paginacija(resultSet)
        else:
            print("Error: Nije unesena validna pretraga sa not operatorom")
    elif 'or' in unesene_reci:
        if len(unesene_reci) == 3:
            index = unesene_reci.index('or')
            unesene_reci.remove('or')

            t1 = find_prefix(stablo.root, unesene_reci[index - 1])
            t2 = find_prefix(stablo.root, unesene_reci[index])

            if (t1[0] == True or t2[0] == True):
                setPodatka = Set('')
                resultSet = Set('')
                if (t1[0] == True and t2[0] == True):
                    resultSet = proveriRecOR(setPodatka, unos, unesene_reci[index - 1])
                    resultSet = proveriRecOR(resultSet, unos, unesene_reci[index])
                    # resultSet = proveriReciAND(setPodatka, unos, unesene_reci[index - 1], unesene_reci[index])
                elif (t1[0] == True and t2[0] == False):
                    resultSet = proveriRecOR(setPodatka, unos, unesene_reci[index - 1])
                elif (t1[0] == False and t2[0] == True):
                    resultSet = proveriRecOR(setPodatka, unos, unesene_reci[index])

                paginacija(resultSet)
                globalResultSet = resultSet

            else:
                print("Error: Obe reci se uopste nisu pojavile!!")
        else:
            print("Error: Nije unesena validna pretraga sa and operatorom")

    else:
        resultSet = Set('')
        pojavljivane_reci = []
        for i in range(len(unesene_reci)):
            t = find_prefix(stablo.root, unesene_reci[i])
            if (t[0] == True):
                pojavljivane_reci.append(unesene_reci[i])
                resultSet = proveriRecOR(resultSet, unos, unesene_reci[i])

        paginacija(resultSet)
        print("\t\t\t\t\t Reci koje su se zapravo pojavile su: " + str(pojavljivane_reci))
        print(
            "\t\t\t\t\t ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        globalResultSet = resultSet

    return globalResultSet