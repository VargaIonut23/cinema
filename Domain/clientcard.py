from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class ClientCard(Entity):
    Nume: str
    Prenume: str
    CNP: str
    DataNasterii: str
    DataInregistrarii: str
    PuncteAcumulate: int
