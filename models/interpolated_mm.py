from models.markov_model import MarkovModel
from utils.globals import RC_FAILED, RC_SUCCESS


class IMM(object):
    """
    Class representation of the Interpolated Markov Model
    """
    def __init__(self, order, label, file):
        """
        Class constructor
        :param order: max order of MM members
        :param label: weight for each order
        :param file: path to FASTA file containing sequences, all with the same label/
        """
        self.orders = order  # List of Markov model orders
        self.weights = []  # List of corresponding weights
        self.models = [MarkovModel(i) for i in range(1, order+1, 1)]
        self.label = label
        self.file = file


    def prepare_model(self,) -> int:
        """
        prepare the model by reading the data from the FASTA file and training the model over all the data.
        :return: RC_SUCCESS or RC_FAILED
        flow:
        read FASTA file TODO: need fasta parser lib from Arbel
        prepare the data according to model format
        train the model ( use self.train over the extracted data)
        """
        #tragining_set = fasta_parser.get_data(file)
        self.train(training_data=training_set)

        return RC_SUCCESS

    def train(self, training_data):
        for model in self.models:
            model.train(training_data)

    def predict(self, context):
        probabilities = []
        for model in self.models:
            probabilities.append(model.predict(context))
        interpolated_probability = sum(p * w for p, w in zip(probabilities, self.weights))
        return interpolated_probability

    def evaluate_success_rate(self, test_data):
        correct_predictions = 0
        total_predictions = 0
        for sequence in test_data:
            for i in range(self.orders[-1], len(sequence)):
                context = sequence[i - self.orders[-1]:i]
                actual_next_state = sequence[i]
                predicted_probability = self.predict(context)
                predicted_next_state = max(predicted_probability, key=predicted_probability.get)
                if predicted_next_state == actual_next_state:
                    correct_predictions += 1
                total_predictions += 1
        success_rate = correct_predictions / total_predictions
        return success_rate

    def evaluate_error_rate(self, test_data):
        return 1 - self.evaluate_success_rate(test_data)