import numpy as np


class Data:
    train_label = []  # label of each file in training data
    test_label = []   # label of each file in test data
    p_class = []  # the possibility of each label
    # the jth value: log(P(Y = y_j)
    # + \sum\limit_i log(P(X = x_i| Y = y_j))
    posterior = []
    word_count_conditioned = []  # value at (i, j) Count(X = x_i, Y = y_j)
    total_words_each_class = []
    p_word_conditioned = []
    label_number = 20
    train_file_number = 11269
    test_file_number = 7505
    vocabulary_size = 61188
    dirichlet_para = 1. / vocabulary_size
    output_confusion_matrix = False
    count_word_frequency = False
    gauge = False
    find_best_words = False
    gauge_start = -5  # starting gauging at 10^{gauge_start}
    gauge_end = 0  # end gauging at 10^{gauge_end}
    gauge_number = 50  # number of sample point

    @staticmethod
    def possibility_of_word():
        """
        Calculate conditioned possibilities of each word given the label.
        This method divides the occurrences of each word
        by the total number of words given the label.
        Additive smoothing is used here.
        :return: a matrix. The ith row of the matrix represents the possibility of
        each word conditioned on the ith label.
        """
        denominator_part = Data.dirichlet_para * Data.vocabulary_size
        p_word_conditioned = np.zeros([Data.label_number, Data.vocabulary_size])
        # Additive smoothing
        for i in range(Data.label_number):
            p_word_conditioned[i] = \
                (Data.word_count_conditioned[i] + Data.dirichlet_para) / \
                (Data.total_words_each_class[i] + denominator_part)
        return p_word_conditioned

    @staticmethod
    def possibility_of_each_class():
        """
        Calculate possibility of each class with MLE, which is simply dividing the
        frequency of each class by the total number of objects.

        :return: an array which contains possibility of each class
        """

        label_count = np.zeros(Data.label_number, dtype=int)
        # count occurrences of each label
        for label in Data.train_label:
            label_count[label - 1] += 1
        return label_count / float(Data.train_file_number)

    @staticmethod
    def count_each_word():
        """
        Calculate the frequency of each word given a certain class.
        If count_word_frequency is true, also count the total frequency
        of each word among all files.
        :return: the conditioned frequency of each word
        """
        Data.word_count_conditioned = np.zeros([Data.label_number, Data.vocabulary_size], dtype=int)
        train_data_file = open("data/train.data", 'r')
        word_frequency = np.zeros(Data.vocabulary_size, dtype=int)
        # Count occurrences of each word with certain labels
        for line in train_data_file:
            data = map(int, line.strip().split(' '))
            if data:
                word_frequency[data[1] - 1] += 1
                Data.word_count_conditioned[Data.train_label[data[0] - 1] - 1]\
                    [data[1] - 1] += data[2]
        train_data_file.close()
        Data.total_words_each_class = np.sum(Data.word_count_conditioned, axis=1)
        if Data.count_word_frequency:
            f = open('word_frequency', 'w')
            for x in word_frequency:
                print >> f, x
            f.close()

    def __init__(self):
        # input labels of train data
        train_label_file = open("data/train.label", 'r')
        Data.train_label = np.zeros(Data.train_file_number, dtype=int)
        index = 0
        for line in train_label_file:
            label = line.strip()
            if label != "":
                Data.train_label[index] = label
                index += 1
        train_label_file.close()

        # input labels of test data
        test_label_file = open("data/test.label", 'r')
        Data.test_label = np.zeros(Data.test_file_number, dtype=int)
        index = 0
        for line in test_label_file:
            label = line.strip()
            if label != "":
                Data.test_label[index] = label
                index += 1
        test_label_file.close()

        # calculate possibility of each class with MLE
        Data.p_class = Data.possibility_of_each_class()
        # initialize value of posterior
        Data.posterior = np.log(Data.p_class)
        # count conditioned frequency of each word
        Data.count_each_word()
        # calculate conditioned possibility of each word
        Data.p_word_conditioned = Data.possibility_of_word()
