import os
import time
from SearchEngine.parserGraph.Graph import *
from SearchEngine.parserGraph.Parser import Parser


def loadGraphFromParser(path):
    directed = True
    g = Graph(directed)
    parser = Parser()

    #path = "C:\\Users\\Pufke\\Desktop\\OISISI-drugi-projektni-zadatak\\SearchEngine\\test-skup\\python-2.7.7-docs-html"

    start = time.time()


    E = []
    link = ''
    for root, dirs, files in os.walk(path, topdown = False):
        for filename in files:
            if r".html" in filename:
                #"Ova linija uzima filename, i spaja ga sa root directorijem, tako da dobijemo Absolute Path"
                absPath = os.path.join(root, filename)
                parser.parse(os.path.join(root, filename))
                #print(filename + " " + str(parser.links.__len__()))
                for links in parser.links:
                    for c in range(len(links)-1,0,-1):
                        if links[c] == "\\":
                            link = links
                            E.append([absPath, link, links])
                            break


                    #add_element_to_Graph(g,absPath,links)
                    #print(links)


    g = add_elements_to_Graph(E, directed)
    end = time.time()
    print("Parsed files and loaded the Graph structure in " + str((end - start).__round__(2  )) + " seconds.")

    return g