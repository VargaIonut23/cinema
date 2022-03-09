from Domain.clientcard import ClientCard
from Domain.movie import Movie
from Domain.reservation import Reservation
from Repository.repository_json import RepositoryJson


def test_movie_repository():
    repo = RepositoryJson('test_movies.json')
    repo.create(Movie('1', 'Nume', 1923, 120, 'da', 0))
    assert len(repo.read()) == 1
    repo.update(Movie('1', 'Prenume', 1921, 100, 'da', 0))
    assert repo.read('1').nameMovie == 'Prenume'
    repo.delete('1')
    assert len(repo.read()) == 0


def test_clientcard_repository():
    repo = RepositoryJson('test_clientcard.json')
    repo.create(ClientCard('1',
                           'Varga',
                           'Ionut',
                           '1234567891011',
                           '12.12.2012',
                           '12.12.2021',
                           100))
    assert len(repo.read()) == 1
    repo.update(ClientCard('1',
                           'Ionescu',
                           'Vasile',
                           '1234567891011',
                           '12.12.2012',
                           '12.12.2021',
                           90))
    assert repo.read('1').Nume == 'Ionescu'
    repo.delete('1')
    assert len(repo.read()) == 0


def test_reservation_repository():
    repo = RepositoryJson('test_reservation.json')
    repo.create(Reservation('1', '1', '1', '12.12.2021', '12:12:12'))
    assert len(repo.read()) == 1
    repo.update(Reservation('1', '1', '1',  '10.10.2010', '12:12:12'))
    assert repo.read('1').data == '10.10.2010'
    repo.delete('1')
    assert len(repo.read()) == 0


def test_all_repository():
    test_movie_repository()
    test_clientcard_repository()
    test_reservation_repository()
