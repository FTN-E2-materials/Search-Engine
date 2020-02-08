"""
Modul koji predstavlja pokretacki deo aplikacije.
"""
from ucitavanePodata import popunjavanjeStruktura
from unos import *
from rangiranjePretrage import rangiranjePretrage
import fnmatch, re
from unos import *
import time

if __name__ == '__main__':

    globalResultSet = Set('')
    resultSet = Set('')
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
                #stablo = loadTrieViaHTML(unos)
                stablo,g = popunjavanjeStruktura(unos)
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
                print("")   # da nije prazan if samo
            else:
                print("Niste uneli validnu pretragu!")
                unosUpit = ''

    unesene_reci = unosUpit.split()
    V = g.vertices()

    # dokumenti koji imaju link ka dokumentu X,dokumenti ka kojima dokument X ima link i proizvoljne informacije
    # dokumentiKojiImajuLinkKaDokumentu = []  # [ [datoteka.html,[....lista datoteka....]], [datoteka.html,[....lista datoteka....]]... ]
    # for v in V:
    #     a = []
    #     for e in g.edges():
    #         if str(v) == str(e._destination):
    #             a.append(str(e._origin))
    #     dokumentiKojiImajuLinkKaDokumentu.append([str(v), a])
    dokumentiKojiImajuLinkKaDokumentu = {}
    for v in V:
        a = []
        for e in g.edges():
            if str(v) == str(e._destination):
                a.append(str(e._origin))
        dokumentiKojiImajuLinkKaDokumentu[str(v)] = a

    print(dokumentiKojiImajuLinkKaDokumentu)

    start3 = time.time()
    globalResultSet = pretraga(unesene_reci,stablo,unos)
    end3 = time.time()
    print("PRETRAGA: " + str((end3 - start3).__round__(2)) + " seconds.")

    print("Pretraga prosla")
    #Rangiranje i stampanje pretrage
    start2 = time.time()
    rangiranSet = rangiranjePretrage(globalResultSet, dokumentiKojiImajuLinkKaDokumentu, unesene_reci,g)
    end2 = time.time()
    print("RANGIRANJE: " + str((end2 - start2).__round__(2)) + " seconds.")
    #print(dokumentiKojiImajuLinkKaDokumentu)
    paginacija(rangiranSet)


