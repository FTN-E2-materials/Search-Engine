"""
Modul koji predstavlja pokretacki deo aplikacije.
"""
from SearchEngine.ucitavanePodata import popunjavanjeStruktura
from SearchEngine.unos import *
from SearchEngine.rangiranjePretrage import rangiranjePretrage
from SearchEngine.pagination import *
import fnmatch, re
from SearchEngine.unos import *
import sys

import time


if __name__ == '__main__':

    globalResultSet = Set('')
    resultSet = Set('')
    setSvihDatoteka = Set('')
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
                print("Please wait...")
                #stablo = loadTrieViaHTML(unos)
                stablo,g,setSvihDatoteka = popunjavanjeStruktura(unos)
                #g = loadGraphFromParser(unos)

            else:
                print("Putanja nije validna!")
                unos = ''

    unosUpit = ''
    # petlja ce da se izvrsava sve dok korisnik ne unese nesto
    while unosUpit == '':
        # Kompajlujemo objekat na kom kasnije mozemo da vrsimo regex metode
        regexObj111 = re.compile("(([\w]+\s){1}(and|or|not){1}(\s[\w]+){1})|([\w\s]+)")

        print("Unesite pretragu:")
        unosUpit = input()
        if unosUpit != '':  # Mora prvo ova provera zato sto regex.match puca ako mu se prosledi prazan string
            if regexObj111.fullmatch(unosUpit):
                print("Please wait...")
            else:
                print("Niste uneli validnu pretragu!")
                unosUpit = ''

    unesene_reci = unosUpit.split()
    if len(unesene_reci) == 3:
        if 'and' == unesene_reci[0] or 'or' == unesene_reci[0] or 'not' == unesene_reci[0] or 'and' == unesene_reci[2] or 'or' == unesene_reci[2] or 'not' == unesene_reci[2]:
            print("Warning: Neispravno koriscenje logickih operatora")
            sys.exit(0)

    V = g.vertices()

    dokumentiKojiImajuLinkKaDokumentu = {}
    bekLinkovi = {}
    for v in V:
        backlinks = 0
        a = []
        for e in g.edges():
            if str(v) == str(e._destination):
                a.append(str(e._origin))
                backlinks = backlinks + 1

        dokumentiKojiImajuLinkKaDokumentu[str(v)] = a
        bekLinkovi[str(v)] = backlinks

    start = time.time()
    globalResultSet = pretraga(unesene_reci,stablo,unos)
    end = time.time()
    print("Za pretragu je potrebno " + str((end - start).__round__(2)) + " sekundi.")

    if len(globalResultSet.elements) != 0:
    #Rangiranje i stampanje pretrage
        start = time.time()
        rangiranSet = rangiranjePretrage(setSvihDatoteka,globalResultSet, dokumentiKojiImajuLinkKaDokumentu,bekLinkovi, unesene_reci)
        end = time.time()
        print("Za rangiranje pretrage je potrebno " + str((end - start).__round__(2)) + " sekundi.")
        paginacija(rangiranSet)
    else:
        print("Not successful search!")




