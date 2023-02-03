import numpy as np
cimport numpy as np
from deeprai.engine.cython import activation as act

#PUBLIC FUNCTIONprint(models.run(x))
cpdef np.ndarray[np.float64_t, ndim=1] forward_propagate(np.ndarray[np.float64_t, ndim=1] inputs, list activation_list, list neurons, list weights):
    """
Parameters:
-----------
inputs : np.ndarray
    Input features to be propagated through the network
activation_list : list
    List of activation functions to be applied to the output of each layer
neurons : list
    List of np.ndarray objects to store the output of each layer
weights : list
    List of weights for each layer

Returns:
-------
np.ndarray
    The final output after forward propagation
"""
    neurons[0]= inputs
    # activation_list -> a list of lambda functions
    cdef np.ndarray[np.float64_t, ndim = 1] layer_outputs
    for layer, weight in enumerate(weights):
        layer_outputs = np.dot(neurons[layer], weight)
        neurons[layer+1] = activation_list[layer](layer_outputs)
    return neurons[-1]

cpdef np.ndarray[np.float64_t, ndim=1] back_propagate(np.ndarray[np.float64_t, ndim=1] loss,  list activation_derv_list, list neurons, list weights, list derv):
    """
Parameters:
-----------
loss : np.ndarray
    Loss to be backpropagated through the network
activation_derv_list : list
    List of derivative functions of the activation functions
neurons : list
    List of np.ndarray objects storing the output of each layer
weights : list
    List of weights for each layer
derv : list
    List of np.ndarray objects to store the gradient of the weights

Returns:
-------
np.ndarray
    The final gradient after backpropagation
"""
    cdef np.ndarray[np.float64_t, ndim = 1] delta
    cdef np.ndarray[np.float64_t, ndim = 2] delta_reshape, current_reshaped
    for layer in reversed(range(len(derv))):
        delta = loss * activation_derv_list[layer](neurons[layer+1])
        delta_reshape = delta.reshape(delta.shape[0], -1).T
        current_reshaped = neurons[layer].reshape(neurons[layer].shape[0], -1)
        derv[layer] = np.dot(current_reshaped, delta_reshape)
        loss = np.dot(delta, weights[layer].T)

#PRIVATE FUNCTION
#note to self, add bies gradent
# cdef np.ndarray[np.float64_t, ndim=1] cython_back_propagate(np.ndarray[np.float64_t, ndim=1] loss,  list activation_derv_list ):
#     cdef np.ndarray[np.float64_t, ndim = 1] delta, delta_reshape, current_reshaped
#     for layer in reversed(range(len(derv))):
#         delta = loss * activation_derv_list[layer](neurons[layer+1])
#         delta_reshape = delta.reshape(delta.shape[0], -1).T
#         current_reshaped = neurons[layer].reshape(neurons[layer].shape[0], -1)
#         derv[layer] = np.dot(current_reshaped, delta_reshape)
#         loss = np.dot(delta, weights[layer].T)
#
#
# cdef np.ndarray[np.float64_t, ndim=1] cython_forward_propagate(np.ndarray[np.float64_t, ndim=1] inputs, list activation_list):
#     neurons[0] = inputs
#     # activation_list -> a list of lambda functions
#     cdef np.ndarray[np.float64_t, ndim = 1] layer_outputs
#     for layer, weight in enumerate(weights):
#         layer_outputs = np.dot(neurons[layer], weight)
#         neurons[layer+1] = activation_list[layer](layer_outputs)
#     return neurons[-1]





