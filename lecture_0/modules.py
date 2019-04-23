import json
from typing import Any


def to_json(entity: Any) -> str:
    """Converts object to JSON string.

    Parameters
    ----------
    entity
        Object to be converted.

    Returns
    -------
    str
        JSON formatted data.

    """

    return json.dumps(entity)
