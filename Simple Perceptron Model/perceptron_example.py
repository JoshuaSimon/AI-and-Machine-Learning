# Perceptorn classifier for given example data.
# For reference see:
# https://medium.com/@thomascountz/19-line-line-by-line-python-perceptron-b6f113b161f3
# https://towardsdatascience.com/perceptron-learning-algorithm-d5db0deab975

import matplotlib.pyplot as plt
import numpy as np
import unittest 

class Perceptron_Model_Test(unittest.TestCase):
    def test_prediction_1(self):
        x_1 = np.array([6,7,8,9,8,8,9,9])
        x_2 = np.array([1,3,2,0,4,6,2,5])
        x_class = np.array([0,0,0,0,1,1,1,1])

        training_inputs = []
        for x1, x2 in zip(x_1, x_2):
            training_inputs.append(np.array([x1,x2]))

        # Initialize and train the model.
        perceptron = Perceptron(2, 1000)
        perceptron.train(training_inputs, x_class)

        inputs = np.array([7.5, 0.7])
        prediction = perceptron.predict(inputs)
        self.assertEqual(prediction, 0, 'Should be class 0.')

        inputs = np.array([6, 6])
        prediction = perceptron.predict(inputs)
        self.assertEqual(prediction, 1, 'Should be class 1.')

        inputs = np.array([0, 0])
        prediction = perceptron.predict(inputs)
        self.assertEqual(prediction, 0, 'Should be class 0.')

        inputs = np.array([-5.5, -10.7])
        prediction = perceptron.predict(inputs)
        self.assertEqual(prediction, 0, 'Should be class 0.')


class Perceptron:
    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
           
    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
          activation = 1
        else:
          activation = 0            
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.threshold):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)

    def get_weights(self):
        return self.weights


if __name__ == "__main__":
    #unittest.main()

    # Example data.
    x_1 = np.array([6,7,8,9,8,8,9,9])
    x_2 = np.array([1,3,2,0,4,6,2,5])
    x_class = np.array([0,0,0,0,1,1,1,1])

    training_inputs = []
    for x1, x2 in zip(x_1, x_2):
        training_inputs.append(np.array([x1,x2]))

    # Initialize and train the model.
    perceptron = Perceptron(2, 1000)
    perceptron.train(training_inputs, x_class)

    # Calculated final weights and linear separator.
    # Hyperplane for linear separation: w0 + w1 * x1 + w2 * x2 = 0
    # ==> x2 = (-w0 - w1 * x1) / w2
    weights = perceptron.get_weights()
    bias = weights[0]
    weights = weights[1:]
    slope = -weights[0] / weights[1]
    intercept = -bias / weights[1]

    # Plot the data to verify, that the data poinrs
    # are linearly separable.
    plt.plot(x_1[0:4], x_2[0:4], 'o', label='Class 0')
    plt.plot(x_1[4:], x_2[4:], 'o', label='Class 1')
    plt.axline((0, intercept), slope=slope, linestyle='--', color='r', label='Separator')
    plt.xlim(5, 10)
    plt.ylim(-1, 10)
    plt.legend()
    plt.show()