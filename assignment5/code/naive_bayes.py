from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction


@dataclass
class NaiveBayes:
    """
    The last criteria in the list of criterias given, is the outcome, so we don't need to calculate the probabilities for it. The last criteria needs to be on the form "Yes" or "No"."""
    criterias: list[str]
    probabilites: dict[str, dict[str, dict[str, Fraction]]]

    def __init__(self, criterias: list[str]) -> None:
        self.criterias = criterias
        probabilites = {}
        for criteria in criterias[:-1]:
            probabilites[criteria] = defaultdict(lambda: {"Yes": 0, "No": 0})
        probabilites[criterias[-1]] = {"Yes": 0, "No": 0}
        self.probabilites = probabilites

    def train(self, data: list[list[str]]) -> None:
        """
        Train the model with the given data, i.e. calculate the probabilities for each criteria.
        """
        # Find the number of times each criteria has a specific value
        for line in data:
            assert len(line) == len(self.criterias), "Invalid data"
            self.probabilites[self.criterias[-1]][line[-1]] += 1
            for criteria, value in zip(self.criterias[:-1], line[:-1]):
                self.probabilites[criteria][value][line[-1]] += 1

        # Turn the number of times into probabilities
        for criteria in self.criterias[:-1]:
            for value in self.probabilites[criteria]:
                self.probabilites[criteria][value]["Yes"] = Fraction(
                    self.probabilites[criteria][value]["Yes"], self.probabilites[self.criterias[-1]]["Yes"])
                self.probabilites[criteria][value]["No"] = Fraction(
                    self.probabilites[criteria][value]["No"], self.probabilites[self.criterias[-1]]["No"])
        self.probabilites[self.criterias[-1]]["Yes"] = Fraction(
            self.probabilites[self.criterias[-1]]["Yes"], len(data))
        self.probabilites[self.criterias[-1]]["No"] = Fraction(
            self.probabilites[self.criterias[-1]]["No"], len(data))

    def predict(self, **kwargs) -> str:
        """ Predict the outcome for the given criteria. """
        yes = self.probabilites[self.criterias[-1]]["Yes"]
        no = self.probabilites[self.criterias[-1]]["No"]
        for criteria in self.criterias[:-1]:
            try:
                yes *= self.probabilites[criteria][kwargs[criteria]]["Yes"]
                no *= self.probabilites[criteria][kwargs[criteria]]["No"]
            except KeyError:
                print(f"No value for {criteria} given")
                return "Wrong input"
        print(f"Yes: {yes}, No: {no}")
        return "Yes" if yes > no else "No"
