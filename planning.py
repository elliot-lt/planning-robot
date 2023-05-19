from enum import Enum  # https://docs.python.org/3/library/enum.html
from typing import Callable
from dataclasses import dataclass

@dataclass
class Application:
    is_brownfield: bool = False
    num_dwellings: int = 0
    is_mayors_pet_project: bool = False

class Decision(Enum):
    APPROVE = 1
    REJECT = 2
    NO_DECISION = 3

Rule = Callable[[Application], Decision]

def compose(*rules: Rule) -> Rule:
    def composed(app) -> Decision:
        for rule in rules:
            decision = rule(app)
            if decision != Decision.NO_DECISION:
                return decision
        return Decision.NO_DECISION
        
    return composed
