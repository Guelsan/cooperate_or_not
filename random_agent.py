from typing import List
from agent import Agent, Decision

import random

class RandomAgent(Agent):

    name    = "Rando"
    descr   = "Does random shit"


    def what_is_your_decision(my_history : List[int], rival_history : List[int], my_scores : List[int], rival_scores : List[int]) -> Decision:
        """ Choses decisions at random, with equal probability. """

        random_choice = random.choice([Decision.COOPORATE, Decision.DONT_COOPORATE])
        return random_choice
    




if __name__ == "__main__":

    # This is how the compliance of your agent is tested
    A = RandomAgent()
    A.introduce_yourself()
    A.test_decision_function()

    # This is how you can get a decision from your agent in a custom test scenario
    my_history      = [1, 1, 0, 0]
    rival_history   = [1, 0, 1, 0]
    test_decision   = A.get_test_decision(my_history, rival_history)

    # This is how you can run a test game
    from naive_agent import NaiveAgent
    from game import Game

    num_rounds = 10
    B = NaiveAgent()
    G = Game(A, B, num_rounds)
    G.show()

    pass