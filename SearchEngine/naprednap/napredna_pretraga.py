import parglare

from SearchEngine.parserTrie.Tree import *
from SearchEngine.set import *


class Operacije:
    def __init__(self, levi, desni, flegOperacije):
        self.levi = levi
        self.desni = desni
        self.flegOperacije = flegOperacije

    def evaluiraj(self, sveStranice, stablo):
        if self.flegOperacije == 1:
            # Unija
            #print("pozvana evaluacija za uniju")
            set1 = self.levi.evaluiraj(sveStranice, stablo)
            set2 = self.desni.evaluiraj(sveStranice, stablo)
            return set1 | set2

        if self.flegOperacije == 2:
            # Presek
            #print("pozvana evaluacija za presek")
            set1 = self.levi.evaluiraj(sveStranice, stablo)
            set2 = self.desni.evaluiraj(sveStranice, stablo)
            return set1 & set2
        if self.flegOperacije == 3:
            # Komplement
            #print("pozvana evaluacija za komplement")
            set1 = sveStranice
            set2 = self.desni.evaluiraj(sveStranice, stablo)
            return set1 - set2

        print("GRESKA TOKOM EVALUIRANJA")
        return Set('')


class Rec():
    def __init__(self, rec):
        self.rec = rec

    def evaluiraj(self, sveStranice, stablo):
        #print("pozvana evaluacija za rec" + self.rec)
        # Vracamo skup stranica za tu rec.
        t = find_prefix(stablo.root, self.rec)
        if t[0] == True:  # u slucaju da je uspesno nadjeno i imamo set, vratimo taj set
            return t[2]  # u t[2] se nalazi skup svih reci za nasu rec
        else:
            return Set('')


class NasParser():

    def __init__(self):
        grammar = r"""
            E: E "||" T
             | T
             ;

            T: T "&&" F
            | F
            ;

            F: "!" X
            | X
            ;

            X: reci
            | "(" E ")"
            ;

            terminals
            reci: /[a-zA-Z_][_a-zA-Z0-9]*/;
        """
        actions = {
            "E": [lambda _, nodes: Operacije(nodes[0], nodes[2],1),
                  lambda _, nodes: nodes[0]],
            "T": [lambda _, nodes: Operacije(nodes[0], nodes[2],2),
                  lambda _, nodes: nodes[0]],
            "F": [lambda _, nodes: Operacije(nodes[1],nodes[1],3),
                  lambda _, nodes: nodes[0]],
            "X": [lambda _, nodes: nodes[0],
                  lambda _, nodes: nodes[1]],
            "reci": lambda _, value: Rec(value),

        }

        g = parglare.Grammar.from_string(grammar)
        self.parser = parglare.Parser(g, actions=actions)

    def parsiraj(self, ulazniString):
        #print("CAOOO")
        r = self.parser.parse(ulazniString)
        return r

