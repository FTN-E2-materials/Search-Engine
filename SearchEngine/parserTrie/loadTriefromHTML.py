import os
import time

from SearchEngine.parserTrie.Tree import *
from SearchEngine.parserTrie.Parser import Parser
from SearchEngine.parserTrie.Tree import TreeNode

def loadTrieViaHTML(path):
    trie = Tree()
    parser = Parser()

    # path = "C:\\Users\\Pufke\\Desktop\\OISISI-drugi-projektni-zadatak\\SearchEngine\\test-skup\\python-2.7.7-docs-html"

    start = time.time()
    trie.root = TreeNode('*')
    for root, dirs, files in os.walk(path, topdown=False):
        for filename in files:
            if r".html" in filename:
                # "Ova linija uzima filename, i spaja ga sa root directorijem, tako da dobijemo Absolute Path"
                parser.parse(os.path.join(root, filename))
                #print(filename + " " + str(parser.words.__len__()))
                for word in parser.words:
                    #if word.lower() == ""
                    add(trie.root, word.lower())

    end = time.time()
    print("Parsed files and loaded the Trie structure in " + str((end - start).__round__(2)) + " seconds.")
    return trie