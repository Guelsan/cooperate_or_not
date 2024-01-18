This is a variation of the prisoner's dilemma as proposed by Merrill Flood and Melvin Dresher.
The goal of this project is to re-do Robert Axelrod's contest, where multiple agents compete against each other. This is all just for fun and serves no serious purpose. Participants can hand in up to 5 agents that will take part in the competition.
The inspiration for this project comes from the Veritasium video: https://www.youtube.com/watch?v=mScpHTIi-kM (If you want to participate, please only watch until 7:15.)

There is extensive research and ressources available for good strategies, but it's more fun to think of something yourself.
If you have already watched the whole video or could not resist reading up on good strategies, no worries, you can still implement your ideas. Just give me notice about this, so I can exclude your agents from the final evaluation. Or hand in strategies of your non-nerdy-friends.

An agent is faced with the decision to _cooporate_ or _not cooperate_. To come to a decision, the agents have access to all previous decisions made by themselves and by their opponent.
- In this implementation, the goal of an agent is to maximize the average score in all games played.
- All agents play against all other agents.
- A game has multiple rounds of decision-making, the number of rounds is on average, but not necessarily exactly, 1000.
- The scores are awarded as follows:

|                          | A cooperates  | A  does not cooperate |
|--------------------------|---------------|-----------------------|
| **B cooperates**         | A: +1,  B: +1 | A: +5,  B: +0         |
| **B does not cooperate** | A: +0,  B: +5 | A: +3,  B: +3         |


To get started, download the files and have a look at the two example agents. "naive_agent.py" and "random_agent.py" can be used as templates. All necessary information is included as comments in "naive_agent.py".
Simply copy one of the example agents and implement your strategies!
Hand in your_agents.py by email or file link.

glhf
