import site
import unittest
from .model_strings import teusnik2000
import rdflib
import os

site.addsitedir('..')
from semsim import Reader
from .model_strings import teusnik2000

class GraphTests(unittest.TestCase):

    def setUp(self) -> None:
        reader = Reader(teusnik2000)
        self.graph = reader.make_graph()

    def test(self):
        print(self.graph.serialize(format='turtle'))


if __name__ == '__main__':
    unittest.main()
