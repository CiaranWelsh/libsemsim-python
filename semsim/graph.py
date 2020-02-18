import rdflib


class Graph(rdflib.Graph):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_sbml(self, sbml, replace=True, filename=None):
        """
        Write annotation to sbml.

        Args:
            sbml (str): file or string
            replace (bool): if model is already annotated, replace it
            filename (str): path to save to. If None, return string. default=None.

        Returns:

        """

    def to_cellml(self):
        """

        Returns:

        """
