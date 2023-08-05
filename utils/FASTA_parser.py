from Bio import SeqIO
import pandas as pd


class FastaParser:

    @staticmethod
    def get_train_labels_dict(labels_path, remove_prefix=True):
        """Transform training labels file to dict.

        :param labels_path: path to training labels (.txt file).
        :param remove_prefix: if True, removes prefix from paths.
        :return: dict of labels and their matching FASTA files.
        """
        df = pd.read_csv(labels_path, sep='\t', header=None, index_col=0)
        df[1] = df[1].str.replace('centroids/', '') if remove_prefix else df[1]
        return df.to_dict()[1]

    @staticmethod
    def get_sequences_from_file(file_path):
        """Extract sequences from given FASTA file.

        :param file_path: path to FASTA file path containing sequences.
        :return: list of all sequences in file.
        """
        return [sequence.seq for sequence in SeqIO.parse(file_path, "fasta")]
