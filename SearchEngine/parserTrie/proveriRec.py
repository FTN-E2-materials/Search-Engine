import os

from parserTrie.Parser import Parser
from set import Set

# Metoda koja saopstava u kom se sve fajlu nalaze prosledjene reci.
def proveriReciAND(setPod,path,rec1: str,rec2: str):
    resultSet=setPod
    #print(rec1.lower())
    #print(rec2.lower())
    parser = Parser()
    for root, dirs, files in os.walk(path, topdown=False):
        for filename in files:
            if r".html" in filename:
                # "Ova linija uzima filename, i spaja ga sa root directorijem, tako da dobijemo Absolute Path"
                parser.parse(os.path.join(root, filename))
                absPath = os.path.join(root, filename)
                flag1 = -1
                flag2 = -1
                for word in parser.words:
                    flag1 = -1
                    flag2 = -1
                    if rec1.lower() == word.lower():
                        flag1 = 1
                    if rec2.lower() == word.lower():
                        flag2 = 1
                    if flag1 == 1 and flag2 == 1:
                        if absPath not in resultSet.elements:
                            resultSet.elements.append(absPath)
                            resultSet.brPojavljivanjaReci.append(1)  # prvo pojavljivanje reci
                            # break
                        else:
                            indx = resultSet.elements.index(absPath)
                            resultSet.brPojavljivanjaReci[indx] += 1
    return resultSet

# Metoda koja saopstava u kom se sve fajlu nalazi rec1 a da se ne nalazi rec2
def proveriReciNOT(setPod,path,rec1: str,rec2: str):
    resultSet=setPod
    parser = Parser()
    for root, dirs, files in os.walk(path, topdown=False):
        for filename in files:
            if r".html" in filename:
                # "Ova linija uzima filename, i spaja ga sa root directorijem, tako da dobijemo Absolute Path"
                parser.parse(os.path.join(root, filename))
                absPath = os.path.join(root, filename)
                flag1 = -1
                flag2 = 1
                for word in parser.words:
                    flag1 = -1
                    flag2 = 1
                    if rec1.lower() == word.lower():
                        flag1 = 1
                    if rec2.lower() == word.lower():
                        flag2 = -1

                    if flag1 == 1 and flag2 == 1:
                        if absPath not in resultSet.elements:
                            resultSet.elements.append(absPath)
                            resultSet.brPojavljivanjaReci.append(1)  # prvo pojavljivanje reci
                            # break
                        else:
                            indx = resultSet.elements.index(absPath)
                            resultSet.brPojavljivanjaReci[indx] += 1

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
                absPath = os.path.join(root, filename)
                #print("root: " + root)
                #print("dir: " + str(dirs))
                #print("filename: "+ filename)
                #print("absPath:"+absPath)
                for word in parser.words:

                    if rec1.lower() == word.lower():
                        #print("Reci se nalaze u fajlu " + filename)
                        if absPath not in resultSet.elements:
                            resultSet.elements.append(absPath)
                            resultSet.brPojavljivanjaReci.append(1)         # prvo pojavljivanje reci
                            # break
                        else:
                            indx=resultSet.elements.index(absPath)
                            resultSet.brPojavljivanjaReci[indx] += 1
    return resultSet