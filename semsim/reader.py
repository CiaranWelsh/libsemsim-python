from .graph import Graph
from lxml import etree



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
            return etree.fromstring(self.input.encode('utf-8'), parser=utf8_parser)
        else:
            # if input is a filename, we can just parse
            return etree.parse(self.input)

    def __str__(self):
        return self.tree.__str__()

    def __repr__(self):
        return self.tree.__repr__()

    def _get_rdf_element(self):
        #todo handle situation where model is not annotated
        annotation_element = self.tree.find('.//annotation', namespaces=self.tree.nsmap)
        return annotation_element[0]

    def make_graph(self):
        rdf = self._get_rdf_element()
        rdf_str = etree.tostring(rdf)
        g = Graph()
        rdf = g.parse(data=rdf_str, format="xml")
        return rdf



