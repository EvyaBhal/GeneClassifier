
import argparse
from utils.FASTA_parser import FastaParser
from models.GeneClassifier import GeneClassifier

if __name__ == '__main__':
    """
    main function
    """
    # Parse input args
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--training_set', dest='training_folder', type=str, help="Path to training folder")
    arg_parser.add_argument('--test_folder', dest='test_folder', type=str, help="Path to testing folder")
    arg_parser.add_argument("--model_order", dest='model_order', type=int, help="Order of IMM models to use")
    args = arg_parser.parse_args()

    training_folder = args.training_folder
    testing_folder = args.test_folder
    model_order = args.model_order

    # Create Gene Classifier with given arguments
    training_set_dict = FastaParser.get_train_labels_dict(training_folder)
    gs = GeneClassifier(training_set_dict, model_order)
    gs.train()


    test_group = FastaParser.get_train_labels_dict(testing_folder)
    correct_perdiciton = 0
    errors = 0
    for label, file in test_group.values():
        test_sequences = FastaParser.get_sequences_from_file(file)
        for seq in test_sequences:
            predicted_groups = gs.predict(seq)
            max_prob = 0
            for key, val in predicted_groups:
                print(f"Probability of seq to be in label {key} is {val}")
                if val > max_prob:
                    max_prob = val
                    max_prob_label = key

            print(f"Model perdicted sequence is in label {max_prob_label}, true label is {label}")
            if label == max_prob_label:
                correct_perdiciton += 1
            else:
                errors += 1

    overall_evaluations = correct_perdiciton + errors
    print(f"overall evaluated {overall_evaluations} sequences")
    print(f"Accuracy: {correct_perdiciton/overall_evaluations}")
