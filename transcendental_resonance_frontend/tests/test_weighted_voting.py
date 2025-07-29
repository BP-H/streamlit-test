# STRICTLY A SOCIAL MEDIA PLATFORM
# Intellectual Property & Artistic Inspiration
# Legal & Ethical Safeguards
from validators.strategies.voting_consensus_engine import (
    aggregate_validator_votes,
    VotingMethod,
)


def test_token_weight_affects_result():
    votes = [
        {"validator_id": "a", "decision": "yes", "confidence": 1, "token_amount": 5},
        {"validator_id": "b", "decision": "no", "confidence": 1, "token_amount": 1},
        {"validator_id": "c", "decision": "yes", "confidence": 1, "token_amount": 1},
    ]
    reputations = {"a": 1.0, "b": 1.0, "c": 1.0}
    res = aggregate_validator_votes(
        votes, reputations=reputations, method=VotingMethod.MAJORITY_RULE
    )
    assert res["consensus_decision"] == "yes"


def test_weight_defaults_to_one():
    votes = [
        {"validator_id": "a", "decision": "yes", "confidence": 1},
        {"validator_id": "b", "decision": "no", "confidence": 1},
    ]
    reputations = {"a": 1.0, "b": 1.0}
    res = aggregate_validator_votes(
        votes, reputations=reputations, method=VotingMethod.MAJORITY_RULE
    )
    assert res["consensus_decision"] == "no_consensus"
