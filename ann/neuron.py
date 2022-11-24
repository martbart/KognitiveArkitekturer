from typing import List
from dataclasses import dataclass

@dataclass(repr=True)
class Neuron:
    """Neuron class, hardlimit activation function."""
    weights: List[float]
    bias: float

    def __init__(self, dimension: int =2) -> None:
        """Initialize neuron with weitghts and bias of 0."""
        self.weights = [0 for _ in range(dimension)]
        self.bias = 0
    
    def feed_forward(self, inputs: List[float]) -> int:
        """Feed forward inputs to neuron."""
        if len(inputs) != len(self.weights):
            raise Exception("Input dimension must be equal to weight dimension.")
        total = 0
        for i in range(len(self.weights)):
            total += self.weights[i] * inputs[i]
        return 1 if total + self.bias >= 0 else 0

    def learn(self, inputs: List[float], target: int) -> None:
        """Learn from inputs and target."""
        guess = self.feed_forward(inputs)
        error = target - guess
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i]
        self.bias += error

    def fit(self, inputs: List[List[float]], targets: List[int]) -> None:
        """Learn from inputs and targets."""
        if not len(inputs) == len(targets):
            raise Exception("Input and target must have same length.")
        old_weights = self.weights.copy()
        converged = False
        iterations = 0
        while not converged and iterations < 100:
            iterations += 1
            for i in range(len(inputs)):
                self.learn(inputs[i], targets[i])
            converged = self.weights == old_weights
            old_weights = self.weights.copy()
        print(f"Converged after {iterations} iterations.")