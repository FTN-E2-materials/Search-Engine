
from SearchEngine.pagination import paginacija
from SearchEngine.parserTrie.findset import *

from SearchEngine.set import *
from SearchEngine.parserTrie.Tree import *
import fnmatch, re
from SearchEngine.ucitavanePodata import popunjavanjeStruktura

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
    globalResultSet = Set('')
    skupoviHTMLstranica = []
    if 'and' in unesene_reci:
        if len(unesene_reci) == 3:
            index = unesene_reci.index('and')
            unesene_reci.remove('and')
            """
            Preko indeksa znam koja 2 elementa iz liste, trebaju obavezno da budu prilikom pretrage.
            t1,t2 - Cuvamo dvojku [uspesnost_trazenja, broj_pojavljivanja]
            """
            t1 = find_prefix(stablo.root, unesene_reci[index - 1])
            t2 = find_prefix(stablo.root, unesene_reci[index])

            # for e in t1[2]:
            #     print(e)

            if (t1[0] == True and t2[0] == True):
                #set1 = nadjiSet(unos, unesene_reci[index - 1])
                #set2 = nadjiSet(unos, unesene_reci[index])

                set1 = t1[2]
                set2 = t2[2]
                skupoviHTMLstranica.append(set1)
                skupoviHTMLstranica.append(set2)

                #resultSet = set1.intersection(set2)
                resultSet = set1 & set2
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

            t1 = find_prefix(stablo.root, unesene_reci[index - 1])
            t2 = find_prefix(stablo.root, unesene_reci[index])

            # set1 = nadjiSet(unos, unesene_reci[index - 1])
            # set2 = nadjiSet(unos, unesene_reci[index])
            set1 = t1[2]
            set2 = t2[2]

            skupoviHTMLstranica.append(set1)
            skupoviHTMLstranica.append(set2)
            resultSet = set1 - set2
            #resultSet = set1.complement(set2)
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
                # set1 = nadjiSet(unos,unesene_reci[index-1])
                # set2 = nadjiSet(unos,unesene_reci[index])
                t1 = find_prefix(stablo.root, unesene_reci[index - 1])
                t2 = find_prefix(stablo.root, unesene_reci[index])
                set1 = t1[2]
                set2 = t2[2]

                skupoviHTMLstranica.append(set1)
                skupoviHTMLstranica.append(set2)

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

                #set = nadjiSet(unos,unesene_reci[i])
                set = t[2]

                skupoviHTMLstranica.append(set)
                resultSet = resultSet | set
                #resultSet = resultSet.union(set)

        globalResultSet = resultSet

    return globalResultSet

def unosPutanje():
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
                print("Please wait...")
                # stablo = loadTrieViaHTML(unos)
                stablo, g, setSvihDatoteka, recnikStranicaReci = popunjavanjeStruktura(unos)
                # g = loadGraphFromParser(unos)

            else:
                print("Putanja nije validna!")
                unos = ''
    return stablo,g,setSvihDatoteka,recnikStranicaReci, unos

def unosProstePretrage():
    unosUpit = ''
    # petlja ce da se izvrsava sve dok korisnik ne unese nesto
    while unosUpit == '':
        # Kompajlujemo objekat na kom kasnije mozemo da vrsimo regex metode
        regexObj111 = re.compile("(([\w]+\s){1}(and|or|not){1}(\s[\w]+){1})|([\w\s]+)")

        print("Unesite pretragu:")
        unosUpit = input()
        unosUpit = unosUpit.strip().lower()
        if unosUpit != '':  # Mora prvo ova provera zato sto regex.match puca ako mu se prosledi prazan string
            if regexObj111.fullmatch(unosUpit):
                print("Please wait...")
            else:
                print("Niste uneli validnu pretragu!")
                unosUpit = ''

    unesene_reci = unosUpit.split()
    return unesene_reci