from .graph import Graph
from lxml import etree
import libsbml


class Reader:
    """
    Reads rdf from an annotated xml (sbml) document and
    creates a :py:class:`Graph`
    """

    def __init__(self, input):
        """
        Args:
            input (str): either path to file or string
        """
        self.input = input
        self.tree = self._read_xml()

    def _read_xml(self):
        """
        Read input into :py:class:`lxml._ElementTree`
        :return:
        """
        # if input is xml string
        if self.input.startswith('<?xml'):
            # regular lxml parser does not work for utf8 so we define our own
            utf8_parser = etree.XMLParser(encoding='utf-8')
            element = etree.fromstring(self.input.encode('utf-8'), parser=utf8_parser)
            # get the tree from the element so we return same type as when parsing filename
            tree = element.getroottree()
            return tree
        else:
            # if input is a filename, we can just parse
            return etree.parse(self.input).getroot()

    def __str__(self):
        return self.tree.__str__()

    def __repr__(self):
        return self.tree.__repr__()

    def is_annotated(self):
        if self.tree.find('.//annotation', namespaces=self.tree.nsmap) is None:
            return False
        return True

    def make_graph(self):
        if not self.is_annotated():
            raise ValueError('Cannot make graph from this model because it is '
                             'not annotated')
        annotation_element = self.tree.find('.//annotation', namespaces=self.tree.nsmap)
        rdf_root = annotation_element[0]
        rdf_str = etree.tostring(rdf_root)
        g = Graph()
        rdf = g.parse(data=rdf_str, format="xml")
        return rdf


class ReaderWithLibSBML:

    def __init__(self, input):
        self.input = input
        self._doc = self._read_sbml()

    def _read_sbml(self):
        reader = libsbml.SBMLReader()
        # if input is xml string
        if self.input.startswith('<?xml'):
            return reader.readSBMLFromString(self.input)
        else:
            return reader.readSBMLFromFile(self.input)

    def get_annotation(self):
        pass

    def is_annotated(self):
        print('')
        print(self._doc.getAnnotation())
        print(self._doc.getAnnotationString())
        print(self._doc.isSetAnnotation())
        for i in sorted(dir(self._doc)):
            print(i)

        print('')
        for i in sorted(dir(libsbml)):
            print(i)

