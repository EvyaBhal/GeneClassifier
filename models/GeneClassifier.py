"""
GeneClassifier
Need to allocate IMM for each genome we have
training is the crucial part:
need to train each IMM to tell probability for given sequnce to belong to the label
perdiction algorithm is simple:
1. get a sequence
2. get probability for each IMM ( each IMM is a different genome)
3. take max probability as the classification of the gene.

TODO:
1. need to define a correlnce bar - if max prob is below bar - than gene doesnt belong to any of known classes
2. need to maybe consider different probability bars for classifying to different genomes


"""
import Bio
from typing import Dict
from models.interpolated_mm import IMM
# read the file and generate a sequence out of it


class GeneClassifier(object):

    def __init__(self, labels: Dict[int, str], order: int = 3):

        self.order = order
        self.models = [IMM(order=self.order, label=label, file=path_to_file) for label, path_to_file in labels.items()]

    def predict(self, context) -> int:
        """

        :param context: sequence to
        :return:
        """
        for model in self.models:
            model.prepare_model()




if __name__ == "__main__":
    """
    Main funciton.
    Logic:
    need to created a dict from the training sets: (label, path to file) - done with fasta parser
    1. function gets' specific file path and returns container of all sequences in file.
    2. function gets path to folder, create a dict of {label: path to file} for each file in directory
    """


