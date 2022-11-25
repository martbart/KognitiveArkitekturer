"""Creates a neuron and trains it to learn the OR function"""

import matplotlib.pyplot as plt
from draw import draw_data, draw_neuron
from generate_tests import generate_tests_from_csv, generate_tests_or
from neuron import Neuron


def main():
    """Main function"""
    neuron = Neuron()
    print("Before learning:", neuron)
    inputs, targets = generate_tests_from_csv(
        "assignment4/data/assign4data.csv", transform=True)
    inputs, targets = generate_tests_or(100)

    fig, ax = plt.subplots()
    ax.set_ylim(-2, 2)
    ax.set_xlim(-2, 2)
    ax.set_aspect("equal")
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()
    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()
    ax.spines['bottom'].set_position('zero')

    draw_data(fig, ax, [[inputs[i], targets[i]] for i in range(len(inputs))])
    neuron.fit(inputs, targets)

    print("After learning:", neuron)

    draw_neuron(fig, ax, neuron)

    correct = 0
    for inpt, target in zip(inputs, targets):
        guess = neuron.feed_forward(inpt)
        if guess == target:
            correct += 1
    print(f"Correct: {correct/len(inputs):.2%}")

    plt.savefig("assignment4/figures/assignment4.png")


if __name__ == "__main__":
    main()
