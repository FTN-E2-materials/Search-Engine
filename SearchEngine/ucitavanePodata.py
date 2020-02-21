import os
import time

from SearchEngine.parserTrie.Tree import *
from SearchEngine.parserTrie.Parser import Parser
from SearchEngine.parserTrie.Tree import TreeNode
from SearchEngine.parserGraph.Parser import Parser
from SearchEngine.parserGraph.Graph import *
#from .set import Set
from SearchEngine.set import *
def popunjavanjeStruktura(path):
    trie = Tree()
    parser = Parser()
    directed = True
    g = Graph(directed)
    parser = Parser()

    """
        OS.Walk() prolazi kroz ceo zadati direktorijum i belezi imena fajlova, kao i path do njih.
        Zatim pomocu for petlje, uzimamo svaki .html fajl koji smo pronasli i parsiramo ga.
        Nakon sto isparsiramo svaki, u okviru polja parser.words ce se nalaziti Array Stringova koji predstavljaju
        reci. Taj Array onda prosledimo strukturi Trie, koja svaku rec ponaosob ubacuje u strukturu.
        Loop se ponavlja za svaki .html fajl dok ne popunimo drvo u potpunosti.
    """
    start = time.time()
    trie.root = TreeNode('*')
    E = []
    link = ''
    setSvihDatoteka = Set('')
    for root, dirs, files in os.walk(path, topdown=False):
        for filename in files:
            if r".html" in filename:
                absPath = os.path.join(root, filename)
                setSvihDatoteka.elements.append(absPath)
                parser.parse(os.path.join(root, filename))
                for word in parser.words:
                    add(trie.root, word.lower(),absPath)

                for links in parser.links:
                    for c in range(len(links)-1,0,-1):
                        if links[c] == "\\":
                            link = links
                            E.append([absPath, link, links])
                            break
    g = add_elements_to_Graph(E, directed)
    end = time.time()
    print("Parsed files and loaded the Trie and Graph structure in " + str((end - start).__round__(2)) + " seconds.")
    return trie,g,setSvihDatoteka