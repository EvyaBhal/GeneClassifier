from models.markov_model import MarkovModel


class IMM(object):
    """
    Class representation of the Interpolated Markov Model
    """
    def __init__(self, orders, weights, label):
        """
        Class constructor
        :param orders: list of orders for the MM
        :param weights: weight for each order
        """
        self.orders = orders  # List of Markov model orders
        self.weights = weights  # List of corresponding weights
        self.models = [MarkovModel(order) for order in orders]
        self.label = label

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