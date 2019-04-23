import json
from typing import Any


def to_json(entity: Any) -> str:
    return json.dumps(entity)
