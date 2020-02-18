import site
import unittest
from .model_strings import teusnik2000
import rdflib
import os
import libsbml
import tellurium as te

site.addsitedir('..')
from semsim import Reader
from semsim.reader import ReaderWithLibSBML
from semsim.util import biomodels_download


class TestReaderWithLXML(unittest.TestCase):
    biomodels_id = 'BIOMD0000000064'
    tear_down = False

    def setUp(self) -> None:
        self.filename = os.path.join(os.path.dirname(__file__), self.biomodels_id + '.xml')
        biomodels_download(self.biomodels_id, self.filename)

    def tearDown(self) -> None:
        if self.tear_down:
            if os.path.isfile(self.filename):
                os.remove(self.filename)

    def test_read_from_file(self):
        reader = Reader(self.filename)
        self.assertIsInstance(reader, Reader)

    def test_read_from_string(self):
        with open(self.filename) as f:
            string = f.read()
        reader = Reader(string)
        self.assertIsInstance(reader, Reader)

    def test_make_graph(self):
        from rdflib import Graph
        reader = Reader(self.filename)
        rdf = reader.make_graph()
        self.assertIsInstance(rdf, Graph)

    def test_has_annotation(self):
        reader = Reader(self.filename)
        self.assertTrue(reader.is_annotated())


class TestReaderWithLibSBML(unittest.TestCase):
    filename = os.path.join(os.path.dirname(__file__), 'teusnik2000.xml')

    def setUp(self) -> None:
        # write to file
        with open(self.filename, 'wb') as f:
            f.write(teusnik2000.encode('utf-8'))

    def test_read_from_string(self):
        reader = ReaderWithLibSBML(teusnik2000)
        doc = reader._read_sbml()
        self.assertIsInstance(doc, libsbml.SBMLDocument)

    def test_read_from_file(self):
        reader = ReaderWithLibSBML(self.filename)
        doc = reader._read_sbml()
        self.assertIsInstance(doc, libsbml.SBMLDocument)

    def test_isannotated(self):
        reader = ReaderWithLibSBML(self.filename)
        reader.is_annotated()


class TestReaderBIOMD(TestReaderWithLXML):
    biomodels_id = 'BIOMD0000000065'
    tear_down = False


class TestReaderBIOMD2(TestReaderWithLXML):
    biomodels_id = 'BIOMD0000000066'
    tear_down = False


class TestReaderBIOMD3(TestReaderWithLXML):
    biomodels_id = 'BIOMD0000000495'
    tear_down = False


class TestReaderBIOMD4(TestReaderWithLXML):
    biomodels_id = 'BIOMD0000000001'
    tear_down = False


class TestReaderNoExistingAnnotation(unittest.TestCase):
    fname = os.path.join(os.path.dirname(__file__), 'no_annotation.xml')
    tear_down = False

    def setUp(self) -> None:
        rr = te.loada("""
            model new_model
                A => B ; k1*A;
                B => A ; k2*B;
                
                A = 100;
                B = 100;
                k1 = 0.1;
                k2 = 0.01;
            end
            """)

        rr.exportToSBML(self.fname)

    def tearDown(self) -> None:
        if self.tear_down and os.path.isfile(self.fname):
            os.remove(self.fname)

    def test_has_annotation(self):
        reader = Reader(self.fname)
        self.assertFalse(reader.is_annotated())

    def test_make_graph_fails(self):
        reader = Reader(self.fname)
        with self.assertRaises(ValueError):
            graph = reader.make_graph()


if __name__ == '__main__':
    unittest.main()
