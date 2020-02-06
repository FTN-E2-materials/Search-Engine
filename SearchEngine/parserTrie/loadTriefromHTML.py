import os
import time

from parserTrie.Tree import *
from parserTrie.Parser import Parser
from parserTrie.Tree import TreeNode



def loadTrieViaHTML(path):
    trie = Tree()
    parser = Parser()

    # path = "C:\\Users\\Pufke\\Desktop\\OISISI-drugi-projektni-zadatak\\SearchEngine\\test-skup\\python-2.7.7-docs-html"

    start = time.time()
    """
        OS.Walk() prolazi kroz ceo zadati direktorijum i belezi imena fajlova, kao i path do njih.
        Zatim pomocu for petlje, uzimamo svaki .html fajl koji smo pronasli i parsiramo ga.
        Nakon sto isparsiramo svaki, u okviru polja parser.words ce se nalaziti Array Stringova koji predstavljaju
        reci. Taj Array onda prosledimo strukturi Trie, koja svaku rec ponaosob ubacuje u strukturu.
        Loop se ponavlja za svaki .html fajl dok ne popunimo drvo u potpunosti.
    """
    trie.root = TreeNode('*')
    for root, dirs, files in os.walk(path, topdown=False):
        for filename in files:
            if r".html" in filename:
                # "Ova linija uzima filename, i spaja ga sa root directorijem, tako da dobijemo Absolute Path"
                parser.parse(os.path.join(root, filename))
                print(filename + " " + str(parser.words.__len__()))
                for word in parser.words:
                    add(trie.root, word.lower())

    end = time.time()
    print("Parsed files and loaded the Trie structure in " + str((end - start).__round__(2)) + " seconds.")
    return trie