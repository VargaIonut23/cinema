from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Movie(Entity):
    nameMovie: str
    year: int
    ticketPrice: float
    inProgram: str
    nrReservation: int
