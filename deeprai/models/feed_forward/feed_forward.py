from deeprai.engine.base_layer import WeightVals, Optimizer, ActivationList, ActivationDerivativeList, LossString, \
    OptimizerString, NeuronVals, DropoutList, l1PenaltyList, l2PenaltyList, LayerVals
import deeprai.engine.build_model as builder
from deeprai.engine.cython.dense_train_loop import train as train
from deeprai.engine.cython.dense_operations import forward_propagate
from deeprai.tools.graphing import neural_net_metrics
import numpy as np

class FeedForward:
    def __init__(self):
        self.spawn = builder.Build()
        self.graph_engine = neural_net_metrics.MetricsGraphingEngine()
        self.use_bias = True
        self.opt_name = "momentum"

    def add_dense(self, neurons, activation='sigmoid', dropout=0, l1_penalty=0, l2_penalty=0):
        self.spawn.create_dense(neurons, activation, dropout, l1_penalty, l2_penalty, self.use_bias)

    def config(self, optimizer='momentum', loss='mean square error', use_bias=True):
        self.opt_name = optimizer
        LossString[0] = loss
        self.use_bias = use_bias

    def train_model(self, train_inputs, train_targets, test_inputs, test_targets, batch_size=36, epochs=500,
                    learning_rate=0.1, momentum=0.6, verbose=True):
        # MomentEstimateVals.moment_estimate_1 = np.zeros((len(WeightVals.Weights), len(WeightVals.Weights[0])))
        # MomentEstimateVals.moment_estimate_2 = np.zeros((len(WeightVals.Weights), len(WeightVals.Weights[0])))
        train(inputs=train_inputs, targets=train_targets, test_inputs=test_inputs, test_targets=test_targets,
              epochs=epochs, learning_rate=learning_rate, momentum=momentum,
              activation_list=ActivationList, activation_derv_list=ActivationDerivativeList, loss_function=LossString,
              verbose=verbose, batch_size=batch_size, dropout_rate=DropoutList, l1_penalty=l1PenaltyList,
              l2_penalty=l2PenaltyList, optimizer_name=self.opt_name, use_bias=self.use_bias)

    def run(self, inputs):
        inputs = np.array(inputs)
        if len(inputs.shape) == 2:
            results = []
            for input_row in inputs:
                result = forward_propagate(input_row, ActivationList, NeuronVals.Neurons, WeightVals.Weights,
                                           DropoutList, training_mode=False)
                results.append(result)
            return np.array(results)
        else:
            return forward_propagate(inputs, ActivationList, NeuronVals.Neurons, WeightVals.Weights, DropoutList,
                                     training_mode=False)

    def specs(self):  # 19
        loss_table = {"categorical cross entropy": "Cross entropy",
                      "mean square error": "MSE",
                      "mean absolute error": "MAE"}
        parameters = sum([LayerVals.Layers[i] * LayerVals.Layers[i + 1] for i in range(len(LayerVals.Layers) - 1)])
        layer_model = 'x'.join(str(i) for i in LayerVals.Layers)

        print(f"""  
    .---------------.------------------.-----------------.------------------.
    |      Key      |       Val        |       Key       |       Val        |
    :---------------+------------------+-----------------+------------------:
    | Model         | Feed Forward     | Optimizer       | Gradient Descent |
    :---------------+------------------+-----------------+------------------:
    | Parameters    | {parameters}{" " * (17 - len(str(parameters)))}| Layer Model     | {layer_model}{" "*(17-len(layer_model))}|
    :---------------+------------------+-----------------+------------------:
    | Loss Function | {loss_table[LossString[0]]}{" " * (17 - len(loss_table[LossString[0]]))}| DeeprAI Version | 0.0.16 BETA      |
    '---------------'------------------'-----------------'------------------'
        """)

    def graph(self, metric="cost"):
        if metric == "cost":
            self.graph_engine.graph_cost()
        elif metric == "acc" or metric == "accuracy":
            self.graph_engine.graph_accuracy()
        elif metric == "error" or metric == "relative error":
            self.graph_engine.graph_rel_error()
        else:
            print(f"Invalid metric: {metric}")


    #auto compleate

    def tanh(self):
        return "tanh"

    def relu(self):
        return "relu"

    def leaky_relu(self):
        return "leaky relu"

    def sigmoid(self):
        return "sigmoid"

    def linear(self):
        return "linear"

    def softmax(self):
        return "softmax"

    def gradient_descent(self):
        return "gradient descent"

    def mean_square_error(self):
        return "mean square error"

    def categorical_cross_entropy(self):
        return "categorical cross entropy"

    def mean_absolute_error(self):
        return "mean absolute error"

    def momentum(self):
        return "momentum"

    def rmsprop(self):
        return "rmsprop"

    def adagrad(self):
        return "adagrad"

    def adam(self):
        return "adam"

