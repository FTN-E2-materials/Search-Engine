"""
Modul koji predstavlja pokretacki deo aplikacije.

"""
from parserTrie.loadTriefromHTML import loadTrieViaHTML
import fnmatch, re
from set import Set
from parserTrie.Parser import *
from SearchEngine.parserGraph.loadGraphFromParser import loadGraphFromParser

if __name__ == '__main__':
    unos = ''
    #petlja ce da se izvrsava sve dok korisnik ne unese nesto
    while unos == '':
        regexPattern1 = fnmatch.translate('[A-Z]:\*')
        regexPattern2 = fnmatch.translate('/*')
        # Kompajlujemo objekat na kom kasnije mozemo da vrsimo regex metode
        regexObj1 = re.compile(regexPattern1)
        regexObj2 = re.compile(regexPattern2)
        print("Unesite putanju korenskog direktorijuma u okviru kojeg zelite da pretrazujete:")
        unos = input()
        if unos!='': #Mora prvo ova provera zato sto regex.match puca ako mu se prosledi prazan string
            if regexObj1.match(unos) or regexObj2.match(unos):
               print("Validna putanja!")
               loadTrieViaHTML(unos)
               g = loadGraphFromParser(unos)
               #Testiranje grafa , ispisivanje svih cvorova
               for v in g.vertices():
                    print(v)
               # Testiranje grafa , ispisivanje svih listova
               for e in g.edges():
                    print(e)
            else:
               print("Putanja nije validna!")
               unos = ''

    # #Testiranje set-a i magicnih metoda
    # a = Set(["pufke", "vladislav"])
    # b = Set(["pufke", "ana"])
    #
    # c = a | b
    # print(c)

    # # Testiranje grafa , ispisivanje svih cvorova
    # for v in g.vertices():
    #     print(v)
    #
    # # Testiranje grafa , ispisivanje svih listova
    # for e in g.edges():
    #     print(e)
    # # instanca stabla
    # t = Tree()
    # t.root = TreeNode(0)

    # # kreiranje relacija između novih čvorova
    # a = TreeNode(1)
    # b = TreeNode(2)
    # c = TreeNode(3)
555