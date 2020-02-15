import site
import unittest
from .model_strings import teusnik2000
import rdflib
import os

site.addsitedir('..')
from semsim.reader import Reader

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

    def test_r(self):
        reader = Reader(teusnik2000)
        print(reader._get_rdf_element())






















if __name__ == '__main__':
    unittest.main()
