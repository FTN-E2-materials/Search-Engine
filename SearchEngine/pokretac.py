"""
Modul koji predstavlja pokretacki deo aplikacije.

"""
from SearchEngine.parserTrie.loadTriefromHTML import loadTrieViaHTML
from SearchEngine.parserTrie.Tree import *
import fnmatch, re
from SearchEngine.parserTrie.Parser import *
from SearchEngine.parserGraph.loadGraphFromParser import loadGraphFromParser

if __name__ == '__main__':

    stablo = Tree()

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

               stablo = loadTrieViaHTML(unos)

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

