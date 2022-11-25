import matplotlib.pyplot as plt
from neuron import Neuron

def draw_data(fig, ax, data):
    ax.scatter(
        [test[0][0] for test in data], 
        [test[0][1] for test in data], 
        c=["black" if test[1] else "white" for test in data],
        edgecolors="black"
        )
    

def draw_neuron(fig, ax, neuron):

    func =  lambda x : -(neuron.weights[0] * x + neuron.bias)/neuron.weights[1]
    arrow = plt.arrow(0, 0, neuron.weights[0], neuron.weights[1], head_width=0.1, head_length=0.1, fc='k', ec='k')
    
    if neuron.weights[1] > 0:
        offset = 100
    else:
        offset = -100

    func2 = lambda x : -(neuron.weights[0] * x + neuron.bias)/neuron.weights[1] + offset
    
    ax.add_patch(arrow)
    ax.fill_between([-2, 2], [func(-2), func(2)], [func2(-2), func2(2)], color="black", alpha=0.2)
    ax.plot([-2,2], [func(-2), func(2)], color="black")