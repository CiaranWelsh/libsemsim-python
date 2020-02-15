import os
from rdflib import Graph
from lxml import etree
from io import StringIO





class Reader:

    def __init__(self, input):
        self.input = input
        self.tree = self._read_xml()
        self.root = self.tree.getroot()

    def _read_xml(self):
        """
        Read input into :py:class:`lxml._ElementTree`
        :return:
        """
        if self.input.startswith('<?xml'):
            try:
                # this sometimes works but not if unicode characters present in xml
                return etree.fromstring(self.input)
            except ValueError as e:
                # when unicode characters are present, reading directly from file works,
                # so create a temporary file, read from it and then delete. Note a good solution,
                # but its a workaround for now.
                # todo: find a way to overcome the unicode problem without reading/writing to file
                if str(e) == 'Unicode strings with encoding declaration are not supported.' \
                                ' Please use bytes input or XML fragments without declaration.':
                    temp_fname = os.path.join(os.path.dirname(__file__), 'temp.xml')
                    with open(temp_fname, 'wb') as f:
                        f.write(self.input.encode('utf-8'))
                    assert os.path.isfile(temp_fname)
                    tree = etree.parse(temp_fname)
                    os.remove(temp_fname)
                    return tree
                raise

        else:
            return etree.parse(self.input)

    def __str__(self):
        return self.tree.__str__()

    def __repr__(self):
        return self.tree.__repr__()

    def to_string(self):
        return etree.tostring(self.tree, pretty_print=True)

    def _get_rdf_element(self):
        print(self.to_string())

        # print(self.root.find('sbml'))
        # print(str(self.root))
        # print(self.root.findall('//annotation'))
        # print(self.root.xpath('//annotation'))



















