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

from typing import Dict
from threading import Thread
from models.interpolated_mm import IMM


class GeneClassifier(object):

    def __init__(self, labels: Dict[int, str], order: int = 3):

        self.order = order
        self.models = [IMM(order=self.order, label=label, file=path_to_file) for label, path_to_file in labels.items()]

    def predict(self, input_seq) -> dict:
        """

        :param input_seq: sequence to predict if is a part of some label
        :return:
        """
        genom_to_prob_dict = {}
        for model in self.models:
            genom_to_prob_dict[model.label] = model.predict(input_seq)

        return genom_to_prob_dict

    def train(self):
        """
        train the models, each on its own genome
        """
        thread_list = []
        for model in self.models:
            thread_list.append(Thread(target=model.train)) # Work with threads to improve runtimes

        [thread.start() for thread in thread_list]
        [thread.join() for thread in thread_list]





