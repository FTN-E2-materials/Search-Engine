import os

from parserTrie.Parser import Parser
from set import Set

# Metoda koja saopstava u kom se sve fajlu nalaze prosledjene reci.
def proveriReciAND(setPod,path,rec1: str,rec2: str):
    resultSet=setPod

    parser = Parser()
    for root, dirs, files in os.walk(path, topdown=False):
        for filename in files:
            if r".html" in filename:
                # "Ova linija uzima filename, i spaja ga sa root directorijem, tako da dobijemo Absolute Path"
                parser.parse(os.path.join(root, filename))
                for word in parser.words:
                    if rec1.lower() == word.lower() and rec2.lower() in word.lower():
                        #print("Reci se nalaze u fajlu " + filename)
                        resultSet.elements.append(filename)
                        break

    return resultSet


# Metoda koja saopstava u kom se nalazi prosledjena rec.
def proveriRecOR(setPod,path,rec1: str):
    resultSet=setPod
    parser = Parser()
    for root, dirs, files in os.walk(path, topdown=False):
        for filename in files:
            if r".html" in filename:
                # "Ova linija uzima filename, i spaja ga sa root directorijem, tako da dobijemo Absolute Path"
                parser.parse(os.path.join(root, filename))
                for word in parser.words:
                    if rec1.lower() == word.lower():
                        #print("Reci se nalaze u fajlu " + filename)
                        resultSet.elements.append(filename)
                        break
    return resultSet