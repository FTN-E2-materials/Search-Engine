"""
Modul koji implementira strukturu podataka Set.
"""


class Set:
    def __init__(self, iterable):
        self.elements = lst = []
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
        lst = []
        for value in other:
            if value not in lst:
                lst.append(value)

        for value in self:
            if value not in lst:
                lst.append(value)
        newSet.elements = lst
        return newSet

    # Metoda koja vrsi uniju skupova.
    def union(self, other):
        newSet = Set("")
        lst = []
        for value in other:
            if value not in lst:
                lst.append(value)

        for value in self:
            if value not in lst:
                lst.append(value)
        newSet.elements = lst
        return newSet

    # Magicna metoda koja vrsi presek tj. a&b
    def __and__(self, other):
        # print("and")
        newSet = Set("")
        elements = []
        for i in range(len(self)):
            for j in range(len(other)):
                if self.elements[i] == other.elements[j]:
                    elements.append(self.elements[i])
        newSet.elements = elements
        return newSet

    # Metoda koja vrsi presek skupova.
    def intersection(self, other):
        # print("presek")
        newSet = Set("")
        elements = []
        for i in range(len(self)):
            for j in range(len(other)):
                if self.elements[i] == other.elements[j]:
                    elements.append(self.elements[i])
        newSet.elements = elements
        return newSet

    # Magicna metoda koja vrsi komplement skupa tj. a-b
    def __sub__(self, other):
        # print("sub")
        newSet = Set("")

        newSet.elements.extend(self.elements)
        for element in other:
            if element in self:
                newSet.elements.remove(element)
        return newSet

    # Metoda koja vrsi komplement skupa.
    def complement(self, other):
        # print("komplement")
        newSet = Set("")

        newSet.elements.extend(self.elements)
        for element in other:
            if element in self:
                newSet.elements.remove(element)
        return newSet

    # Overide metoda za ispis seta.
    def __str__(self):
        # return str(self.__class__) + ": " + str(self.__dict__)
        return str(self.__dict__)
