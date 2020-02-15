import unittest
from .model_strings import teusnik2000
import rdflib


class Test(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test(self):

        g = rdflib.Graph()
        result = g.parse("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        print("graph has %s statements." % len(g))
        # prints graph has 79 statements.

        for subj, pred, obj in g:
            print(subj, pred, obj)

        s = g.serialize(format='n3')
        print(s)


    def test2(self):
        from rdflib import Graph
        g = Graph()
        print(g)
        g.parse('demo.nt', format='nt')
        print(g)
        from pprint import pprint
        pprint(g)
        for stmt in g:
            print(stmt)

    def test2(self):
        from rdflib import Graph, Namespace
        n = Namespace('http://www.sbml.org/sbml/level2')
        print(n)
        # g = Graph()
        # g.parse('http://www.sbml.org/sbml/level2')
        # print(g)

    def test4(self):
        from rdflib import Graph, Namespace
        import os
        g = Graph()

        f = os.path.join(os.path.dirname(__file__), 'BIOMD0000000064.xml')
        assert os.path.isfile(f)
        g.parse(f, format='xml')
        # print(g, len(g))
























if __name__ == '__main__':
    unittest.main()
