from typing import List                             # Mandatory imports
from agent import Agent, Decision

                                                    # More imports that you need

class NaiveAgent(Agent):                            # Have a useful class name, inherit from Agent

    name    = "Naive Nancy"                         # Some agent name
    descr   = "I believe in harmony"                # Short description of your agent

    # This is your Agent-defining decision function. You get access to the game history and scores. A decision is expected from your agent.
    def what_is_your_decision(my_history : List[int], rival_history : List[int], my_scores : List[int], rival_scores : List[int]) -> Decision:
        """ Always decides to cooporate. """        # Put a useful description of your decision logic here
        
        nice_choice = Decision.COOPORATE
        return nice_choice
    




if __name__ == "__main__":

    # This is how the compliance of your agent is tested
    A = NaiveAgent()
    A.introduce_yourself()
    A.test_decision_function()

    # This is how you can get a decision from your agent in a custom test scenario
    my_history      = [1, 1, 0, 0]
    rival_history   = [1, 0, 1, 0]
    test_decision   = A.get_test_decision(my_history, rival_history)

    # This is how you can run a test game
    from random_agent import RandomAgent
    from game import Game

    num_rounds = 10
    B = RandomAgent()
    G = Game(A, B, num_rounds)
    G.show()

    pass