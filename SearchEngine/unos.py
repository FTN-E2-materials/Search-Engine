
from pagination import paginacija
from parserTrie.findset import *

from set import *
from parserTrie.Tree import *


# function to get unique values
def unique(list1):
    # intilize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def pretraga(unesene_reci,stablo,unos):

    if 'and' in unesene_reci:
        if len(unesene_reci) == 3:
            index = unesene_reci.index('and')
            unesene_reci.remove('and')
            """
            Preko indeksa znam koja 2 elementa iz liste, trebaju obavezno da budu prilikom pretrage.
            t1,t2 - Tuple u kome cuvamo [uspesnost_trazenja, broj_pojavljivanja]
            """
            t1 = find_prefix(stablo.root, unesene_reci[index - 1])
            t2 = find_prefix(stablo.root, unesene_reci[index])
            if (t1[0] == True and t2[0] == True):
                set1 = nadjiSet(unos, unesene_reci[index - 1])
                set2 = nadjiSet(unos, unesene_reci[index])
                resultSet = set1.intersection(set2)

                globalResultSet = resultSet
                #paginacija(resultSet)
            else:
                print("Error: Nisu se obe reci pojavile!!")
        else:
            print("Error: Nije unesena validna pretraga sa and operatorom")
    elif 'not' in unesene_reci:
        if len(unesene_reci) == 3:
            index = unesene_reci.index('not')
            unesene_reci.remove('not')

            set1 = nadjiSet(unos, unesene_reci[index - 1])
            set2 = nadjiSet(unos, unesene_reci[index])
            resultSet = set1.complement(set2)
            globalResultSet = resultSet
            #paginacija(resultSet)
        else:
            print("Error: Nije unesena validna pretraga sa not operatorom")
    elif 'or' in unesene_reci:
        if len(unesene_reci) == 3:
            index = unesene_reci.index('or')
            unesene_reci.remove('or')

            t1 = find_prefix(stablo.root, unesene_reci[index - 1])
            t2 = find_prefix(stablo.root, unesene_reci[index])
            if (t1[0] == True or t2[0] == True):
                set1 = nadjiSet(unos,unesene_reci[index-1])
                set2 = nadjiSet(unos,unesene_reci[index])
                resultSet = set1.union(set2)
                globalResultSet = resultSet
            else:
                print("Error: Obe reci se uopste nisu pojavile!!")
        else:
            print("Error: Nije unesena validna pretraga sa or operatorom")

    else:
        resultSet = Set('')
        pojavljivane_reci = []
        unesene_reci = unique(unesene_reci)
        for i in range(len(unesene_reci)):
            t = find_prefix(stablo.root, unesene_reci[i])
            if (t[0] == True):
                pojavljivane_reci.append(unesene_reci[i])
                set = nadjiSet(unos,unesene_reci[i])
                resultSet = resultSet.union(set)

        globalResultSet = resultSet

    return globalResultSet