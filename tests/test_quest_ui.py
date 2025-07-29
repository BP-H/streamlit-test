import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from quest_ui import _quest_progress


def test_quest_progress():
    quest = {
        "milestones": [
            {"progress": 1, "target": 1},
            {"progress": 0, "target": 2},
            {"progress": 2, "target": 2},
        ]
    }
    assert _quest_progress(quest) == 2 / 3


