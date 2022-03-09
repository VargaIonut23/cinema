from Domain.clientcard import ClientCard
from Domain.movie import Movie
from Domain.reservation import Reservation


def test_movie():
    movie = Movie('1', 'Nume', 1923, 120, 'da', 0)
    assert movie.entity_id == '1'
    assert movie.nameMovie == 'Nume'
    assert movie.year == 1923
    assert movie.ticketPrice == 120
    assert movie.inProgram == 'da'
    movie.year = 2001
    movie.nameMovie = 'Titanic'
    assert movie.nameMovie == 'Titanic'
    assert movie.year == 2001


def test_clientcard():
    clientcard = ClientCard('1',
                            'Varga',
                            'Ionut',
                            '1234567891011',
                            '12.12.2012',
                            '12.12.2021',
                            100)
    assert clientcard.entity_id == '1'
    assert clientcard.Nume == 'Varga'
    assert clientcard.Prenume == 'Ionut'
    assert clientcard.CNP == '1234567891011'
    assert clientcard.DataNasterii == '12.12.2012'
    assert clientcard.DataInregistrarii == '12.12.2021'
    assert clientcard.PuncteAcumulate == 100


def test_reservation():
    reservation = Reservation('1', '1', '1', '12.12.2021', '12:12:12')
    assert reservation.entity_id == '1'
    assert reservation.idClientCard == '1'
    assert reservation.idMovie == '1'
    assert reservation.data == '12.12.2021'
    assert reservation.ora == '12:12:12'


def test_domain():
    test_movie()
    test_clientcard()
    test_reservation()
