from dataclasses import dataclass
from typing import List


@dataclass
class ReservationError(Exception):
    error_message: List[str]

    def __str__(self):
        return f"ReservationError: {self.error_message}"
