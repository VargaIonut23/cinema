from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Reservation(Entity):
    idMovie: str
    idClientCard: str
    data: str
    ora: str
