
from dataclasses import dataclass
from typing import Callable
from .solutions import ini3_solution, ini4_solution, ini5_solution, ini6_solution

@dataclass
class Problem:
    '''Class for writing testable solutions to Rosalind problems.'''
    solution: Callable
    sample_dataset: str
    sample_out: str

    def __post_init__(self):
        self.sample_dataset = self.sample_dataset.splitlines(True)

    def test(self):
        output = self.solution(self.sample_dataset)
        try:
            assert self.sample_out == output
            print('The solution is correct!')
        except:
            print('The soultion is not correct!\n') 
            print(f'{output}\n')
            print('!=\n')
            print(f'{self.sample_out}')


ini3 = Problem(
    solution=ini3_solution,
    sample_dataset="""HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102""",
    sample_out="""Humpty Dumpty"""
    )

ini4 = Problem(
    solution=ini4_solution,
    sample_dataset="""100 200""",
    sample_out="""7500"""
    )

ini5 = Problem(
    solution=ini5_solution,
    sample_dataset="""Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat""",
    sample_out="""Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat"""
    )

ini6 = Problem(
    solution=ini6_solution,
    sample_dataset="""We tried list and we tried dicts also we tried Zen""",
    sample_out="""and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1"""
    )
