"""
Modul koji predstavlja pokretacki deo aplikacije.
"""
from ucitavanePodata import popunjavanjeStruktura
from unos import *
from rangiranjePretrage import rangiranjePretrage
import fnmatch, re
from unos import *
import time
from parserGraph.Parser import Parser

from rangiranjePretrage import brojPonavaljanjaReciuDatoteci

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
        regexObj111 = re.compile("(([\w]+\s){1}(and|or|not)(\s[\w]+){1})|([\w\s]+)")

        print("Unesite pretragu:")
        unosUpit = input()
        if unosUpit != '':  # Mora prvo ova provera zato sto regex.match puca ako mu se prosledi prazan string
            if regexObj111.fullmatch(unosUpit):
                print("Please wait...")
            else:
                print("Niste uneli validnu pretragu!")
                unosUpit = ''

    unesene_reci = unosUpit.split()
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


    globalResultSet = pretraga(unesene_reci,stablo,unos)

    #Rangiranje i stampanje pretrage
    rangiranSet = rangiranjePretrage(setSvihDatoteka,globalResultSet, dokumentiKojiImajuLinkKaDokumentu,bekLinkovi, unesene_reci)


    paginacija(rangiranSet)


