"""Keeps track of the networks values"""
import build_model
class Layer:
    def __init__(self):
        self.Layers = None

    def initialize(self, layers):
        self.Layers = layers

    def pop(self):
        self.Layers = []


class Kernel:
    def __init__(self):
        self.Kernels = None

    def initialize(self):
        self.Kernels = []

    def pop(self):
        self.Kernels = []


class Bias:
    def __init__(self):
        self.Biases = None

    def initialize(self, bias):
        self.Biases = bias

    def pop(self):
        self.Biases = []



class Weight:
    def __init__(self):
        self.Weights = None

    def initialize(self, weight):
        self.Weights = weight

    def pop(self):
        self.Weights = []

class Neuron:
    def __init__(self):
        self.Neurons = None

    def initialize(self, neurons):
        self.Neurons = neurons

    def pop(self):
        self.Neurons = []

class Derivative:
    def __init__(self):
        self.Derivatives = None

    def initialize(self, derivatives):
        self.Derivatives = derivatives

    def pop(self):
        self.Derivatives = []



#GLOBAL NETWORK VALUES
Biases = Bias()
Weight = Weight()
Kernels = Kernel()
Layers = Layer()
Neurons = Neuron()

