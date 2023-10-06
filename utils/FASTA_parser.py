from Bio import SeqIO
import pandas as pd
import os


class FastaParser:

    @staticmethod
    def get_train_labels_dict(training_path: str):
        """Transform training labels file to dict (label includes path to actual FASTA file).

        :param training_path: path to training data and labels
        :return: dict of labels and their matching FASTA files.
        """
        labels_path = os.path.dirname(training_path)
        full_path = os.path.join(training_path, "centroids")

        df = pd.read_csv(labels_path, sep='\t', header=None, index_col=0)
        df[1] = df[1].str.replace('centroids', full_path)
        return df.to_dict()[1]

    @staticmethod
    def get_sequences_from_file(file_path):
        """Extract sequences from given FASTA file.

        :param file_path: path to FASTA file path containing sequences.
        :return: list of all sequences in file.
        """
        return [sequence.seq for sequence in SeqIO.parse(file_path, "fasta")]
