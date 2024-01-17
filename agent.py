from abc import ABC, abstractmethod
from typing import List, final
import random
from enum import Enum

class Decision(Enum):
    COOPORATE       = 1
    DONT_COOPORATE  = 0

class Agent(ABC):

    name    = None  
    descr   = None

    def __init__(self) -> None:
        self.my_history  = []
        self.my_scores   = []
        self.total_score = 0
        super().__init__()

    def __init_subclass__(cls) -> None:
        
        # Check if necessary attributes are present
        if not hasattr(cls, 'name'):
            raise NotImplementedError('Attribute "name" not implemented')
        if not hasattr(cls, 'descr'):
            raise NotImplementedError('Attribute "descr" not implemented')
        
        # Check correct type of attributes
        if not type(cls.name) == str:
            raise TypeError(f'Attribute "name" has wrong type: {type(cls.name)} -> Should be of type str')
        if not type(cls.descr) == str:
            raise TypeError(f'Attribute "descr" has wrong type: {type(cls.descr)} -> Should be of type str')
        
        # Check if value of attributes is valid
        if not (len(cls.name) > 0 and len(cls.name) <= 30):
            raise ValueError(f'Attribute "name" has invalid length: {len(cls.name)} -> Should be between 1 and 30 characters')
        if not (len(cls.descr) > 3 and len(cls.descr) <= 300):
            raise ValueError(f'Attribute "descr" has invalid length: {len(cls.descr)} -> Should be between 4 and 300 characters')
        
        return super().__init_subclass__()

    @classmethod
    @final
    def test_decision_function(cls) -> bool: 
        # Check decision function 
        if not type(cls.what_is_your_decision([], [], [], [])) == Decision:
            raise TypeError(f'Decision function returns invalid value. -> Should return a Decision Enum')
        if not type(cls.what_is_your_decision([1], [1], [3], [3])) == Decision:
            raise TypeError(f'Decision function returns invalid value. -> Should return a Decision Enum')
        if not type(cls.what_is_your_decision([1, 0], [1, 1], [3, 0], [3, 5])) == Decision:
            raise TypeError(f'Decision function returns invalid value. -> Should return a Decision Enum')
        
        return True

    @classmethod
    @final
    def introduce_yourself(cls, talk : bool = True) -> tuple[str, str]:
        intro_list  = ["Hi, I am", "It's me", "Call me", "My name is", "The name is", "I respond to", "I'm known as"]

        if talk:
            print(f"{random.choice(intro_list)}\033[94m {cls.name}\033[0m. ({cls.descr})")
        
        return cls.name, cls.descr
    
    @classmethod
    @final
    def get_decision(cls, my_history : List[int], rival_history : List[int], my_score : int, rival_score : int) -> Decision:
        return cls.what_is_your_decision(my_history, rival_history, my_score, rival_score)
    
    @classmethod
    @final
    def get_test_decision(cls, my_history : List[int], rival_history : List[int]) -> Decision:
        my_score    = []
        rival_score = []
        
        if not len(my_history) == len(rival_history):
            raise ValueError(f'History lists are not the same length -> Should be the same length') 

        for i in range(len(my_history)):
            d1 = my_history[i]
            d2 = rival_history[i]
            if     d1 and     d2:
                sc1 = 3
                sc2 = 3
            if not d1 and     d2:
                sc1 = 5
                sc2 = 0
            if     d1 and not d2:
                sc1 = 0
                sc2 = 5
            if not d1 and not d2:
                sc1 = 1
                sc2 = 1

            my_score.append(sc1)
            rival_score.append(sc2)

        return cls.what_is_your_decision(my_history, rival_history, my_score, rival_score)
       
    @final
    def update(self, new_decision : int, new_score) -> None:
        self.my_history.append(new_decision)
        self.my_scores.append(new_score)
        self.total_score = sum(self.my_scores)

    @final
    def wipe(self) -> None:
        self.my_history  = []
        self.my_scores   = []
        self.total_score = 0

    @staticmethod
    @abstractmethod
    def what_is_your_decision(my_history : List[int], rival_history : List[int], my_score : int, rival_score : int) -> Decision:
        pass
 


if __name__ == "__main__":

    from random_agent import RandomAgent
    from naive_agent import NaiveAgent
    
    RA = RandomAgent()
    RA.introduce_yourself()

    NA = NaiveAgent()
    NA.introduce_yourself()


    my_history      = [1, 1, 0, 0]
    rival_history   = [1, 0, 1, 0]
    test_decision   = NA.get_test_decision(my_history, rival_history)

    pass 







