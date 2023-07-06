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
from models.interpolated_mm import IMM
# read the file and generate a sequence out of it


class GeneClassifier(object):

    def __init__(self, num_labels):

        self.models = [IMM() for i in num_labels]

