import os
from rdflib import Graph
from lxml import etree
from io import StringIO





class Reader:

    def __init__(self, input):
        self.input = input

        # if input is a file, read into string
        # if not self.input.startswith('<?xml'):
        #     with open(self.input) as f:
        #         self.input = f.read()

        # if resulting string is utf8, convert to ascii
        # self.input = self.input.encode('ascii')
        self.xml = self._read_xml()

    def _read_xml(self):
        if self.input.startswith('<?xml'):
            return etree.fromstring(self.input)
        else:
            return etree.parse(self.input)

    def __str__(self):
        return self.xml.__str__()

    def __repr__(self):
        return self.xml.__repr__()



















