from agent import Agent, Decision
import copy


class Game:

    def __init__(self, agent_1 : Agent, agent_2 : Agent, rounds : int, verbosity : int = 2) -> None:
        self.rounds     = rounds
        self.agent_1    = None
        self.agent_2    = None
        self.__verbos   = verbosity

        self.__play(agent_1, agent_2)
        

    def __play(self, agent_1 : Agent, agent_2 : Agent) -> None:

        agent_1.wipe()
        agent_2.wipe()

        agent_1.test_decision_function()
        agent_2.test_decision_function()

        hist_1      = []
        hist_2      = []
        scores_1    = []
        scores_2    = []

        d1  = None
        d2  = None
        sc1 = 0
        sc2 = 0

        for _ in range(self.rounds):
            hist_1      = agent_1.my_history
            hist_2      = agent_2.my_history
            scores_1    = agent_1.my_scores
            scores_2    = agent_2.my_scores

            d1 = agent_1.get_decision(hist_1, hist_2, scores_1, scores_2)
            d2 = agent_2.get_decision(hist_2, hist_1, scores_2, scores_1)

            if d1 == Decision.COOPORATE      and d2 == Decision.COOPORATE:
                sc1 = 3
                sc2 = 3
            if d1 == Decision.DONT_COOPORATE and d2 == Decision.COOPORATE:
                sc1 = 5
                sc2 = 0
            if d1 == Decision.COOPORATE      and d2 == Decision.DONT_COOPORATE:
                sc1 = 0
                sc2 = 5
            if d1 == Decision.DONT_COOPORATE and d2 == Decision.DONT_COOPORATE:
                sc1 = 1
                sc2 = 1
            
            agent_1.update(d1.value, sc1)
            agent_2.update(d2.value, sc2)

        self.agent_1    = copy.copy(agent_1)
        self.agent_2    = copy.copy(agent_2)

        if self.__verbos >= 1:
            print("\nWe welcome our competing agents:")
            name1, _  = agent_1.introduce_yourself()
            name2, _  = agent_2.introduce_yourself()

            tsc1 = agent_1.total_score
            tsc2 = agent_2.total_score

            if tsc1 == tsc2:
                print("It's a draw!")
            if tsc1 > tsc2:
                print(f"The winner is \033[94m{name1}\033[0m with {tsc1} points! This beats \033[94m{name2}\033[0m with {tsc2} points.")
            if tsc2 > tsc1:
                print(f"The winner is \033[94m{name2}\033[0m with {tsc2} points! This beats \033[94m{name1}\033[0m with {tsc1} points.")

    def show(self) -> None:
        name1   = self.agent_1.name         # type: str
        name2   = self.agent_2.name         # type: str
        hist1   = self.agent_1.my_history
        hist2   = self.agent_2.my_history
        sc1     = self.agent_1.my_scores
        sc2     = self.agent_2.my_scores
        d       = "|"

        print("\033[1m" + "Round".center(8) + d + name1.center(15) + d + name2.center(15) + d + "Advantage".center(15) + d + "Score".center(10) + "\033[0m")

        prstr = ""
        for i in range(len(hist1)):
            prstr = f"{i}".center(8) + d
            if hist1[i]:    prstr = prstr + f"\033[32mCOOP\033[0m".center(24) + d
            else:           prstr = prstr + f"\033[31mDON'T COOP\033[0m".center(24) + d
            
            if hist2[i]:    prstr = prstr + f"\033[32mCOOP\033[0m".center(24) + d
            else:           prstr = prstr + f"\033[31mDON'T COOP\033[0m".center(24) + d

            if sc1[i] == sc2[i]:  prstr = prstr + "-".center(15) + d
            if sc1[i] > sc2[i]:   prstr = prstr + name1.center(15) + d
            if sc1[i] < sc2[i]:   prstr = prstr + name2.center(15) + d

            prstr = prstr + f"{sum(sc1[0:i+1])}".rjust(4) + "-" + f"{sum(sc2[0:i+1])}"

            print(prstr)



    def evaluate(self):
        #TODO: Return interesting metrics for further analysis
        pass






if __name__ == "__main__":

    from random_agent import RandomAgent
    from naive_agent import NaiveAgent

    num_rounds = 10
    A = RandomAgent()
    B = NaiveAgent()

    G = Game(A, B, num_rounds)
    G.show()
    

    pass