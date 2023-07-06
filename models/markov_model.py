class MarkovModel(object):
    """
    This is a class representation of a Markov Model of order N
    order should be given as input to the model.
    Since we are using each markov model only to get the probabilities, we do not need evaluation at this point.
    @TODO: check with Itay about this implementation. maybe we need additions?
    """
    def __init__(self, order):
        """
        Class constructor
        :param order: the order of the markov model
        """
        self.order = order
        self.transitions = {}

    def train(self, training_data):
        """
        train the model
        :param training_data:
        """
        for sequence in training_data:
            self._train_sequence(sequence)

    def _train_sequence(self, sequence):
        context = tuple(sequence[:self.order])
        for i in range(self.order, len(sequence)):
            current_state = sequence[i]
            if context not in self.transitions:
                self.transitions[context] = {}
            if current_state not in self.transitions[context]:
                self.transitions[context][current_state] = 0
            self.transitions[context][current_state] += 1
            context = context[1:] + (current_state,)

    def predict(self, context) -> dict:
        """

        :param context:
        :return:
        """
        next_state_counts = self.transitions.get(tuple(context[-self.order:]), {})
        total_count = sum(next_state_counts.values())
        probabilities = {state: count / total_count for state, count in next_state_counts.items()}
        return probabilities