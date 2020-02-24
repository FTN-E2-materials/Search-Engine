import parglare
from parglare.actions import pass_inner, pass_single

from SearchEngine.parserTrie.Tree import *
from SearchEngine.set import *



class Unija:
    def __init__(self, levi, desni):
        self.levi = levi
        self.desni = desni

    def evaluiraj(self, sveStranice, stablo):
        pass


class Presek():
    def __init__(self, levi, desni):
        self.levi = levi
        self.desni = desni

    def evaluiraj(self, sveStranice, stablo):
        pass


class Komplement():
    def __init__(self, desni):
        self.desni = desni

    def evaluiraj(self, sveStranice, stablo):
        pass


class Rec():
    def __init__(self, rec):
        self.rec = rec

    def evaluiraj(self, sveStranice, stablo):
        pass


class NasParser():

    def __init__(self):
        # grammar_string = r"""
        # E: E '||' E {left,1}
        #  | E '&&' E {left,2}
        #  | '!' E {left,3}
        #  | '(' E ')'
        #  | ReciRef
        #  ;
        #
        # ReciRef: Reci;
        #
        # terminals
        # Reci: /[a-zA-Z_][_a-zA-Z0-9]*/;
        # """
        # Po ugledu na +,-,*,/
        # E -> E + T | E - T | T
        # T -> T * F | T / F | F
        # F -> F ^ X | B
        # B -> i | (E)
        # X -> i | (E)

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
            "E": [lambda _, nodes: Unija(nodes[0], nodes[2]),
                  lambda _, nodes: nodes[0]],
            "T": [lambda _, nodes: Presek(nodes[0], nodes[2]),
                  lambda _, nodes: nodes[0]],
            "F": [lambda _, nodes: Komplement(nodes[1]),
                  lambda _, nodes: nodes[0]],
            "X": [lambda _, nodes: nodes[0],
                  lambda _, nodes: nodes[1]],
            "reci": lambda _, value: Rec(value),

        }

        g = parglare.Grammar.from_string(grammar)
        self.parser = parglare.Parser(g, actions=actions)

    def parse(self, ulazniString):
        return self.parser.parse(ulazniString)


