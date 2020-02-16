import rdflib


class Graph(rdflib.Graph):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
