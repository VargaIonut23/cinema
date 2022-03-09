from dataclasses import dataclass
from typing import List


@dataclass
class MovieError(Exception):
    error_message: List[str]

    def __str__(self):
        return f"MovieError: {self.error_message}"
