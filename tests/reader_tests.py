import site
import unittest
from .model_strings import teusnik2000
import rdflib
import os

site.addsitedir('..')
from semsim import Reader


class Test(unittest.TestCase):
    filename = os.path.join(os.path.dirname(__file__), 'teusnik2000.xml')

    def setUp(self) -> None:
        # write to file
        with open(self.filename, 'wb') as f:
            f.write(teusnik2000.encode('utf-8'))

    def tearDown(self) -> None:
        if os.path.isfile(self.filename):
            os.remove(self.filename)

    def test_read_from_file(self):
        reader = Reader(self.filename)
        self.assertIsInstance(reader, Reader)

    def test_read_from_string(self):
        reader = Reader(teusnik2000)
        self.assertIsInstance(reader, Reader)

    def test_get_rdf_element(self):
        reader = Reader(teusnik2000)
        rdf_element = reader._get_rdf_element()
        expected ='{http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF'
        actual = rdf_element.tag
        self.assertEqual(expected, actual)

    def test_make_graph(self):
        from rdflib import Graph
        reader = Reader(teusnik2000)
        rdf = reader.make_graph()
        self.assertIsInstance(rdf, Graph)

    def test_make_graph(self):
        from rdflib import Graph
        reader = Reader(teusnik2000)
        graph = reader.make_graph()
        print(graph.t)

if __name__ == '__main__':
    unittest.main()
