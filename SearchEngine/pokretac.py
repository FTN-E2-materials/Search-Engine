"""
Modul koji predstavlja pokretacki deo aplikacije.
"""
from SearchEngine.ucitavanePodata import popunjavanjeStruktura
from SearchEngine.unos import *
from SearchEngine.rangiranjePretrage import rangiranjePretrage
from SearchEngine.pagination import *
from SearchEngine.naprednap.napredna_pretraga import *

import fnmatch, re
from SearchEngine.unos import *
import sys

import time


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

if __name__ == '__main__':
    np = NasParser()

    globalResultSet = Set('')
    resultSet = Set('')
    setSvihDatoteka = Set('')
    stablo = Tree()

    stablo, g, setSvihDatoteka, recnikStranicaReci, unos = unosPutanje()
    while True:
        print("\n\t\t\t\t ------------------------------------- GLAVNI MENI -------------------------------------")
        print("\t\t\t\t\t1 - Prosta pretraga [ AND, OR, NOT - operatori].")
        print("\t\t\t\t\t2 - Napredna pretraga.")
        print("\t\t\t\t\tK - Kraj programa.")
        print("\n\t\t\t\t ---------------------------------------------------------------------------------------")
        indexPretrage = input("Unos[1,2]: ")

        if indexPretrage == "K" or indexPretrage == "k":
            break

        if indexPretrage not in [str(1),str(2)]:
            continue


        if indexPretrage == str(1):
            unesene_reci = unosProstePretrage()

            if len(unesene_reci) == 3:
                if 'and' == unesene_reci[0] or 'or' == unesene_reci[0] or 'not' == unesene_reci[0] or 'and' == \
                        unesene_reci[2] or 'or' == unesene_reci[2] or 'not' == unesene_reci[2]:
                    print("Warning: Neispravno koriscenje logickih operatora")
                    sys.exit(0)

            start = time.time()
            globalResultSet = pretraga(unesene_reci, stablo, unos)
            end = time.time()
            print("Za pretragu je potrebno " + str((end - start).__round__(2)) + " sekundi.")
            #break
        if indexPretrage == str(2):
            print("Unesite pretragu:")
            unosUpit = input()
            unosUpit = unosUpit.strip().lower()
            unesene_reci = unosUpit.split()

            start = time.time()
            globalResultSet = np.parse(unosUpit).evaluiraj(setSvihDatoteka, stablo)
            print(len(globalResultSet))
            end = time.time()
            print("Za pretragu je potrebno " + str((end - start).__round__(2)) + " sekundi.")

            #break


        start1 = time.time()
        V = g.vertices()
        dokumentiKojiImajuLinkKaDokumentu = {}
        bekLinkovi = {}
        i = 0
        for v in V:
            # print(v)
            backlinks = 0
            a = []
            for e in g.edges():
                # print("\t\t"+str(e))
                if str(v) == str(e._destination):
                    a.append(str(e._origin))
                    backlinks = backlinks + 1

            dokumentiKojiImajuLinkKaDokumentu[str(v)] = a
            bekLinkovi[str(v)] = backlinks
        end1 = time.time()
        print("Za nesto sto je bitno za rangiranje kosta " + str((end1 - start1).__round__(2)) + " sekundi.")


        if len(globalResultSet.elements) != 0:
        #Rangiranje i stampanje pretrage
            start = time.time()
            rangiranSet = rangiranjePretrage(setSvihDatoteka,globalResultSet, dokumentiKojiImajuLinkKaDokumentu,bekLinkovi, unesene_reci,recnikStranicaReci)
            end = time.time()
            print("Za rangiranje pretrage je potrebno " + str((end - start).__round__(2)) + " sekundi.")
            paginacija(rangiranSet)
        else:
            print("Not successful search!")




