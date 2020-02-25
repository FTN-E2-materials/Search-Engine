import os

from .Parser import Parser
from set import Set
import time



# Metoda koja za prosledjenu rec i path, vraca set podataka sa HTML stranicama.
def nadjiSet(path,rec:str):
    start = time.time()

    resultSet = Set('')
    parser = Parser()
    for root, dirs, files in os.walk(path, topdown=False):
        for filename in files:
            if r".html" in filename:
                #start1 = time.time()
                parser.parse(os.path.join(root, filename))
                #end1 = time.time()
                #print("Za parsiranje je potrebno: " + str((end1-start1).__round__(3)) + " sekundi.")

                absPath = os.path.join(root, filename)
                #start2 = time.time()
                for word in parser.words:
                    if rec.lower() == word.lower():
                        if absPath not in resultSet.elements:
                            resultSet.elements.append(absPath)
                            break
                #end2 = time.time()
                #print("Za prolazak kroz reci je potrebno: " + str((end2 - start2).__round__(3)) + " sekundi.")



    end = time.time()
    print("Za nalazenje seta je potrebno " + str((end - start).__round__(2)) + " sekundi.")

    return resultSet