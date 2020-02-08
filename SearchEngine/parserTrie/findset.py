import os

from parserTrie.Parser import Parser
from set import Set

# Metoda koja za prosledjenu rec i path, vraca set podataka sa HTML stranicama.
def nadjiSet(path,rec:str):
    resultSet = Set('')
    parser = Parser()
    for root, dirs, files in os.walk(path, topdown=False):
        for filename in files:
            if r".html" in filename:
                parser.parse(os.path.join(root, filename))
                absPath = os.path.join(root, filename)
                for word in parser.words:
                    if rec.lower() == word.lower():
                        if absPath not in resultSet.elements:
                            resultSet.elements.append(absPath)
                            break
    return resultSet