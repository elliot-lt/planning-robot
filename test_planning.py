import planning

from planning import Decision

def only_brownfield(app: planning.Application) -> Decision:
    if not app.is_brownfield:
        return Decision.REJECT
    return Decision.NO_DECISION

positive_properties: planning.Rule = lambda app: Decision.NO_DECISION if app.num_dwellings > 0 else Decision.REJECT
approve_mayors_projects: planning.Rule = lambda app: Decision.APPROVE if app.is_mayors_pet_project else Decision.NO_DECISION
reject_all: planning.Rule = lambda app: Decision.REJECT
approve_all: planning.Rule = lambda app: Decision.APPROVE

def test_compose_single_rule():
    engine = planning.compose(only_brownfield)
    assert engine(planning.Application(is_brownfield=False)) is Decision.REJECT

def test_compose_multi_rules():
    engine = planning.compose(only_brownfield, positive_properties)
    assert engine(planning.Application(is_brownfield=True, num_dwellings = 0)) is Decision.REJECT

def test_compose_passing():
    engine = planning.compose(only_brownfield, approve_all)
    assert engine(planning.Application(is_brownfield=True)) is Decision.APPROVE


def test_early_approve():
    engine = planning.compose(approve_mayors_projects, reject_all)
    assert engine(planning.Application(is_mayors_pet_project=True)) is Decision.APPROVE