from typing import Any
from structlog.typing import EventDict as EventDictionary


def mijdauya2j3h7lg3d8hcl6qkk(
    logger: Any, log_type_name: str, event_dict: EventDictionary
) -> EventDictionary:
    event_dict["level"] = log_type_name

    return event_dict
