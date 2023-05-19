from typing import Callable, Sequence
from dataclasses import dataclass

@dataclass
class PlanningApplication:
    is_brownfield: bool

Rule = Callable[[PlanningApplication], bool]

def compose(*rules: Rule) -> Rule:
    pass
