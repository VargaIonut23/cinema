from Domain.reservation import Reservation
from Domain.reservation_error import ReservationError


class ReservationValidator:
    def validator(self, reservation: Reservation):
        erori = []
        if reservation.entity_id <= '0':
            erori.append('id ul rezervarii '
                         ' trebuie sa fie cel putin 0!')
        if reservation.data[2] != '.':
            erori.append('Data introdusa'
                         ' este incorecta')
        if reservation.data[5] != '.':
            erori.append('Data introdusa'
                         ' este incorecta')
        if reservation.ora[2] != ':':
            erori.append('Ora introdusa'
                         ' este incorecta')
        if reservation.ora[5] != ':':
            erori.append('Ora introdusa'
                         ' este incorecta')
        if len(erori) > 0:
            raise ReservationError(erori)
