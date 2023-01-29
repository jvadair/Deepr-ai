from deeprai.engine.cython import activation as act
class LeakyRelu:
    def leaky_relu(self, neuron):
        return act.sigmoid(neuron)

    def sigmoid_derivative(self, sigmoid):
        return act.sigmoid_derivative(sigmoid)


