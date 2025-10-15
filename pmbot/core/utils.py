from typing import Any
from os import getenv


def assert_getenv(key: str) -> str:
    """
    Returns value from environment by key

    :raises
    - `AssertionError` if key was not founded
    """
    value = getenv(key, None)
    assert value, f"'{key}' is not defined in environment"
    return value


__all__ = ("assert_getenv",)
