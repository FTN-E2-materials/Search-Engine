
"""
Modul koji implementira strukturu podataka Set.
"""

class Set:
    def __init__(self, iterable):
        self.elements = lst = []
        self.listaPoena = []          # lista/niz zabroj pojavljivanja pretrazivane reci
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

    # Magicna metoda koja vrsi uniju tj. a|b
    def __or__(self, other):
        newSet = Set("")
        lst = []        # lista za elemente tj linkove
        #lstR= []        # lsita za broj ponavljanja reci

        i = 0
        for element in other.elements:
            if element not in lst:
                lst.append(element)
                #brojReci = other.brPojavljivanjaReci[i]
                #lstR.append(brojReci)
            i += 1
        i = 0
        for element in self.elements:
            if element not in lst:
                lst.append(element)
                #brojReci = self.brPojavljivanjaReci[i]
                #lstR.append(brojReci)
            i += 1

        newSet.elements = lst
        #newSet.brPojavljivanjaReci = lstR
        return newSet

    # Metoda koja vrsi uniju skupova.
    def union(self, other):
        newSet = Set("")
        lst = []  # lista za elemente tj linkove
        #lstR = []  # lsita za broj ponavljanja reci

        i = 0
        for element in other.elements:
            if element not in lst:
                lst.append(element)
                #brojReci = other.brPojavljivanjaReci[i]
                #lstR.append(brojReci)
            i += 1
        i = 0
        for element in self.elements:
            if element not in lst:
                lst.append(element)
                #brojReci = self.brPojavljivanjaReci[i]
                #lstR.append(brojReci)
            i += 1

        newSet.elements = lst
        #newSet.brPojavljivanjaReci = lstR
        return newSet

    # Magicna metoda koja vrsi presek tj. a&b
    def __and__(self, other):
        newSet = Set("")
        elements = []
        #reci=[]
        for i in range(len(self)):
            for j in range(len(other)):
                if self.elements[i] == other.elements[j]:
                    elements.append(self.elements[i])
                    #reci.append(self.brPojavljivanjaReci[i])
        newSet.elements = elements
        #newSet.brPojavljivanjaReci = reci
        return newSet

    # Metoda koja vrsi presek skupova.
    def intersection(self, other):
        newSet = Set("")
        elements = []
        #reci = []
        for i in range(len(self)):
            for j in range(len(other)):
                if self.elements[i] == other.elements[j]:
                    elements.append(self.elements[i])
                    #reci.append(self.brPojavljivanjaReci[i])
        newSet.elements = elements
        #newSet.brPojavljivanjaReci = reci
        return newSet

    # Magicna metoda koja vrsi komplement skupa tj. a-b
    def __sub__(self, other):
        newSet = Set("")

        newSet.elements.extend(self.elements)
        #newSet.brPojavljivanjaReci.extend(self.brPojavljivanjaReci)
        for element in other.elements:
            if element in self.elements:
                newSet.elements.remove(element)
                #idx = self.elements.index(element)
                #newSet.brPojavljivanjaReci.pop(idx)
        return newSet

    # Metoda koja vrsi komplement skupa.
    def complement(self, other):
        newSet = Set("")

        newSet.elements.extend(self.elements)
        #newSet.brPojavljivanjaReci.extend(self.brPojavljivanjaReci)
        for element in other.elements:
            if element in self.elements:
                newSet.elements.remove(element)
                #idx = self.elements.index(element)
                #newSet.brPojavljivanjaReci.pop(idx)
        return newSet

    # Overide metoda za ispis seta.
    def __str__(self):
        # return str(self.__class__) + ": " + str(self.__dict__)
        return str(self.__dict__)
