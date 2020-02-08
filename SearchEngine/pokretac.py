"""
Modul koji predstavlja pokretacki deo aplikacije.
"""
from ucitavanePodata import popunjavanjeStruktura
from unos import *
from rangiranjePretrage import rangiranjePretrage
import fnmatch, re
from unos import *
from parserGraph.loadGraphFromParser import loadGraphFromParser
from parserTrie.loadTriefromHTML import loadTrieViaHTML


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
                V = g.vertices()
                # dokumenti koji imaju link ka dokumentu X,dokumenti ka kojima dokument X ima link i proizvoljne informacije
                dokumentiKojiImajuLinkKaDokumentu = [] # [ [datoteka.html,[....lista datoteka....]], [datoteka.html,[....lista datoteka....]]... ]
                for v in V:
                    # print("--------------- DOKUMENT: ", v, " ---------------")
                    # print("DOKUMENTI KOJI IMAJU LINKA KA TOM DOKUMENTU: ")
                    a = []
                    for e in g.edges():
                        if str(v) == str(e._destination):
                            #print(str(e._origin))
                            a.append(str(e._origin))
                    dokumentiKojiImajuLinkKaDokumentu.append([str(v),a])

                # print(dokumentiKojiImajuLinkKaDokumentu)
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

    unesene_reci = unosUpit.split()

    globalResultSet = pretraga(unesene_reci,stablo,unos)

    #Rangiranje i stampanje pretrage
    rangiranjePretrage(globalResultSet, dokumentiKojiImajuLinkKaDokumentu, unesene_reci,g)



