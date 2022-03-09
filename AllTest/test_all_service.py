from Domain.addoperation import Addoperation
from Domain.clientcardValidator import ClientCardValidator
from Domain.deletealloperation import Deletealloperation
from Domain.deleteoperation import Deleteoperation
from Domain.incrementarepuncteoperation import Incrementarepuncteoperation
from Domain.modifyoperations import Modifyoperation
from Domain.movieValidator import MovieValidator
from Domain.reservationValidator import ReservationValidator
from Repository.repository_json import RepositoryJson
from Service.clientcardService import ClientCardService
from Service.movieService import MovieService
from Service.reservationService import ReservationService
from Service.undoredoservice import Undoredoservice


def test_movie_service():
    undoredoservice = Undoredoservice()
    reservation_repository = RepositoryJson('test_reservation.json')
    reservation_validator = ReservationValidator()

    clientcard_repository = RepositoryJson('test_clientcard.json')
    clientcard_validator = ClientCardValidator()

    movie_repository = RepositoryJson('test_movies.json')
    movie_validator = MovieValidator()
    reservation_service = ReservationService(reservation_repository,
                                             reservation_validator,
                                             movie_repository,
                                             clientcard_repository,
                                             undoredoservice)
    clientcard_service = ClientCardService(clientcard_repository,
                                           clientcard_validator,
                                           reservation_repository,
                                           reservation_service,
                                           undoredoservice)
    movie_service = MovieService(movie_repository,
                                 movie_validator,
                                 reservation_repository,
                                 reservation_service,
                                 clientcard_service,
                                 undoredoservice)
    movie_service.add_movie('1', 'Nume', 1923, 120, 'da')
    assert len(movie_service.show_all_movies()) == 1
    movie_service.update_movie('1', 'Prenume', 2000, 120, 'da')
    assert len(movie_service.show_all_movies()) == 1
    movie_service.delete_movie('1')
    assert len(movie_service.show_all_movies()) == 0


def test_cardclient_service():
    undoredoservice = Undoredoservice()
    reservation_repository = RepositoryJson('test_reservation.json')
    reservation_validator = ReservationValidator()

    clientcard_repository = RepositoryJson('test_clientcard.json')
    clientcard_validator = ClientCardValidator()
    movie_repository = RepositoryJson('test_movies.json')
    reservation_service = ReservationService(reservation_repository,
                                             reservation_validator,
                                             movie_repository,
                                             clientcard_repository,
                                             undoredoservice)
    clientcard_service = ClientCardService(clientcard_repository,
                                           clientcard_validator,
                                           reservation_repository,
                                           reservation_service,
                                           undoredoservice)
    clientcard_service.add_clientcard('1',
                                      'Varga',
                                      'Ionut',
                                      '1234567891011',
                                      '12.12.2012',
                                      '12.12.2021',
                                      100)
    assert len(clientcard_service.show_all_clientcards()) == 1
    clientcard_service.update_clientcard('1',
                                         'Varga',
                                         'Ionut',
                                         '1234567891011',
                                         '12.12.2012',
                                         '12.12.2021',
                                         200)
    assert len(clientcard_service.show_all_clientcards()) == 1
    clientcard_service.delete_clientcard('1')
    assert len(clientcard_service.show_all_clientcards()) == 0


def test_reservation_service():
    undoredoservice = Undoredoservice()
    reservation_repository = RepositoryJson('test_reservation.json')
    reservation_validator = ReservationValidator()

    clientcard_repository = RepositoryJson('test_clientcard.json')
    clientcard_validator = ClientCardValidator()

    movie_repository = RepositoryJson('test_movies.json')
    movie_validator = MovieValidator()
    reservation_service = ReservationService(reservation_repository,
                                             reservation_validator,
                                             movie_repository,
                                             clientcard_repository,
                                             undoredoservice)
    clientcard_service = ClientCardService(clientcard_repository,
                                           clientcard_validator,
                                           reservation_repository,
                                           reservation_service,
                                           undoredoservice)
    movie_service = MovieService(movie_repository,
                                 movie_validator,
                                 reservation_repository,
                                 reservation_service,
                                 clientcard_service,
                                 undoredoservice)
    clientcard_service.add_clientcard('1',
                                      'Varga',
                                      'Ionut',
                                      '1234567891011',
                                      '12.12.2012',
                                      '12.12.2021',
                                      100)
    movie_service.add_movie('1', 'Nume', 1923, 120, 'da')
    reservation_service.add_reservation('1',
                                        '1',
                                        '1',
                                        '12.12.2021',
                                        '12:12:12')
    assert len(reservation_service.show_all_reservations()) == 1
    reservation_service.update_reservation('1',
                                           '1',
                                           '1',
                                           '12.12.2021',
                                           '12:12:12')
    assert len(reservation_service.show_all_reservations()) == 1
    reservation_service.delete_reservation('1')
    assert len(reservation_service.show_all_reservations()) == 0
    movie_service.delete_movie('1')
    clientcard_service.delete_clientcard('1')


def test_cerinte_service():
    undoredoservice = Undoredoservice()
    reservation_repository = RepositoryJson('test_reservation.json')
    reservation_validator = ReservationValidator()
    clientcard_repository = RepositoryJson('test_clientcard.json')
    clientcard_validator = ClientCardValidator()
    movie_repository = RepositoryJson('test_movies.json')
    movie_validator = MovieValidator()
    reservation_service = ReservationService(reservation_repository,
                                             reservation_validator,
                                             movie_repository,
                                             clientcard_repository,
                                             undoredoservice)
    clientcard_service = ClientCardService(clientcard_repository,
                                           clientcard_validator,
                                           reservation_repository,
                                           reservation_service,
                                           undoredoservice)
    movie_service = MovieService(movie_repository,
                                 movie_validator,
                                 reservation_repository,
                                 reservation_service,
                                 clientcard_service,
                                 undoredoservice)
    clientcard_service.add_clientcard('1',
                                      'Varga',
                                      'Ionut',
                                      '1234567891011',
                                      '12.12.2012',
                                      '12.12.2021',
                                      100)
    movie_service.add_movie('1', 'Nume', 1923, 0, 'da')
    reservation_service.add_reservation('1',
                                        '1',
                                        '1',
                                        '12.12.2021',
                                        '12:12:12')
    '''Incrementarea cu o valoare dată'''
    assert clientcard_service.show_clientcard('1').PuncteAcumulate == 100
    clientcard_service.adaugarepuncte(100, '10.12.2011', '13.12.2015')
    assert clientcard_service.show_clientcard('1').PuncteAcumulate == 200
    '''Ștergerea tuturor rezervărilor
    dintr-un anumit interval de zile'''
    assert len(reservation_service.show_all_reservations()) == 1
    reservation_service.StergeRezervareZile('10.12.2021',
                                            '13.12.2021',
                                            reservation_service.
                                            reservation_repository.read(),
                                            [])
    assert len(reservation_service.show_all_reservations()) == 0
    reservation_service.add_reservation('1',
                                        '1',
                                        '1',
                                        '12.12.2021',
                                        '12:12:12')
    '''Afișarea filmelor ordonate
    descrescător după numărul de rezervări'''
    movie_service.add_movie('2', 'Nume', 1923, 0, 'da')
    list = []
    list = movie_service.OrdonareMovie()
    assert (list[0].entity_id) == '1'
    assert (list[1].entity_id) == '2'
    movie_service.delete_movie('2')
    '''Afisarea cardurilor client ordonate
    descrescator dupa numarul de puncte'''
    clientcard_service.add_clientcard('2',
                                      'Varga',
                                      'Ionut',
                                      '1234567891011',
                                      '12.12.2012',
                                      '12.12.2021',
                                      100)
    list = []
    list = clientcard_service.OrdonareClientCards()
    assert (list[0].entity_id) == '1'
    assert (list[1].entity_id) == '2'
    clientcard_service.delete_clientcard('2')
    '''Afișarea tuturor rezervărilor dintr-un
        interval de ore dat, indiferent de zi'''
    reservation_service.add_reservation('2',
                                        '1',
                                        '1',
                                        '12.12.2021',
                                        '12:12:12')
    list = []
    list = reservation_service.AfisareRezervareOre('10:10:10', '13:13:13')
    assert (list[0].entity_id) == '1'
    assert (list[1].entity_id) == '2'
    reservation_service.delete_reservation('2')
    'full text'
    list = []
    list = movie_service.FullText('1')
    assert (list[0].nameMovie) == 'Nume'
    assert (list[1].Nume) == 'Varga'

    movie_service.delete_movie('1')
    clientcard_service.delete_clientcard('1')


def test_undo_redo_service():
    undoredoservice = Undoredoservice()
    reservation_repository = RepositoryJson('test_reservation.json')
    reservation_validator = ReservationValidator()
    clientcard_repository = RepositoryJson('test_clientcard.json')
    clientcard_validator = ClientCardValidator()
    movie_repository = RepositoryJson('test_movies.json')
    movie_validator = MovieValidator()
    reservation_service = ReservationService(reservation_repository,
                                             reservation_validator,
                                             movie_repository,
                                             clientcard_repository,
                                             undoredoservice)
    clientcard_service = ClientCardService(clientcard_repository,
                                           clientcard_validator,
                                           reservation_repository,
                                           reservation_service,
                                           undoredoservice)
    movie_service = MovieService(movie_repository,
                                 movie_validator,
                                 reservation_repository,
                                 reservation_service,
                                 clientcard_service,
                                 undoredoservice)
    '''MOVIE'''
    '''adaugare'''
    movie_service.add_movie('1', 'Nume', 1923, 0, 'da')
    assert len(movie_repository.read()) == 1
    undoredoservice.adaugaOperatie(Addoperation(movie_repository,
                                                movie_repository.read("1")))
    undoredoservice.undo()
    assert len(movie_repository.read()) == 0
    undoredoservice.redo()
    assert len(movie_repository.read()) == 1
    '''stergere'''
    undoredoservice.adaugaOperatie(Deleteoperation(movie_repository,
                                                   movie_repository.read("1")))
    movie_service.delete_movie("1")
    assert len(movie_repository.read()) == 0
    undoredoservice.undo()
    assert len(movie_repository.read()) == 1
    undoredoservice.redo()
    assert len(movie_repository.read()) == 0
    '''modificare'''
    movie_service.add_movie('1', 'Nume', 1923, 0, 'da')
    movie = movie_repository.read("1")
    movie_service.update_movie('1', 'Ionut', 2021, 0, 'nu')
    undoredoservice.adaugaOperatie(Modifyoperation(movie_repository,
                                                   movie_repository.read('1'),
                                                   movie))
    assert movie_repository.read('1').nameMovie == 'Ionut'
    assert movie_repository.read('1').year == 2021
    assert movie_repository.read('1').ticketPrice == 0
    assert movie_repository.read('1').inProgram == 'nu'
    undoredoservice.undo()
    assert movie_repository.read('1').nameMovie == 'Nume'
    assert movie_repository.read('1').year == 1923
    assert movie_repository.read('1').ticketPrice == 0
    assert movie_repository.read('1').inProgram == 'da'
    undoredoservice.redo()
    assert movie_repository.read('1').nameMovie == 'Ionut'
    assert movie_repository.read('1').year == 2021
    assert movie_repository.read('1').ticketPrice == 0
    assert movie_repository.read('1').inProgram == 'nu'
    '''CLIENTCARD'''
    '''adaugare'''
    clientcard_service.add_clientcard('1',
                                      'Varga',
                                      'Ionut',
                                      '1234567891011',
                                      '12.12.2012',
                                      '12.12.2021',
                                      0)
    assert len(clientcard_repository.read()) == 1
    undoredoservice.adaugaOperatie(
        Addoperation(clientcard_repository,
                     clientcard_repository.read('1')))
    undoredoservice.undo()
    assert len(clientcard_repository.read()) == 0
    undoredoservice.redo()
    assert len(clientcard_repository.read()) == 1
    '''stergere'''
    undoredoservice.adaugaOperatie(
        Deleteoperation(clientcard_repository,
                        clientcard_repository.read('1')))
    assert len(clientcard_repository.read()) == 1
    clientcard_service.delete_clientcard('1')
    assert len(clientcard_repository.read()) == 0
    undoredoservice.undo()
    assert len(clientcard_repository.read()) == 1
    undoredoservice.redo()
    assert len(clientcard_repository.read()) == 0
    '''modificare'''
    clientcard_service.add_clientcard('1',
                                      'Varga',
                                      'Ionut',
                                      '1234567891011',
                                      '12.12.2012',
                                      '12.12.2021',
                                      0)
    clientcard = clientcard_repository.read('1')
    clientcard_service.update_clientcard('1',
                                         'Horvat',
                                         'Denis',
                                         '1234567891012',
                                         '12.12.1212',
                                         '12.12.1212',
                                         0)
    undoredoservice.adaugaOperatie(
        Modifyoperation(clientcard_repository,
                        clientcard_repository.read('1'),
                        clientcard))
    assert clientcard_repository.read('1').Nume == 'Horvat'
    assert clientcard_repository.read('1').Prenume == 'Denis'
    assert clientcard_repository.read('1').CNP == '1234567891012'
    assert clientcard_repository.read('1').DataNasterii == '12.12.1212'
    assert clientcard_repository.read('1').DataInregistrarii == '12.12.1212'
    assert clientcard_repository.read('1').PuncteAcumulate == 0
    undoredoservice.undo()
    assert clientcard_repository.read('1').Nume == 'Varga'
    assert clientcard_repository.read('1').Prenume == 'Ionut'
    assert clientcard_repository.read('1').CNP == '1234567891011'
    assert clientcard_repository.read('1').DataNasterii == '12.12.2012'
    assert clientcard_repository.read('1').DataInregistrarii == '12.12.2021'
    assert clientcard_repository.read('1').PuncteAcumulate == 0
    undoredoservice.redo()
    assert clientcard_repository.read('1').Nume == 'Horvat'
    assert clientcard_repository.read('1').Prenume == 'Denis'
    assert clientcard_repository.read('1').CNP == '1234567891012'
    assert clientcard_repository.read('1').DataNasterii == '12.12.1212'
    assert clientcard_repository.read('1').DataInregistrarii == '12.12.1212'
    assert clientcard_repository.read('1').PuncteAcumulate == 0
    '''incrementare puncte'''
    assert clientcard_repository.read('1').PuncteAcumulate == 0
    undoredoservice.adaugaOperatie(
        Incrementarepuncteoperation(clientcard_repository,
                                    clientcard_repository.read('1'),
                                    7))
    clientcard_service.adaugarepuncte(7, '11.11.1111', '13.12.1212')
    assert clientcard_repository.read('1').PuncteAcumulate == 7
    undoredoservice.undo()
    assert clientcard_repository.read('1').PuncteAcumulate == 0
    undoredoservice.redo()
    assert clientcard_repository.read('1').PuncteAcumulate == 7
    '''REZERVARE'''
    '''adaugare'''
    reservation_service.add_reservation('1',
                                        '1',
                                        '1',
                                        '12.12.2021',
                                        '12:12:12')
    assert len(reservation_repository.read()) == 1
    undoredoservice.adaugaOperatie(
        Addoperation(reservation_repository,
                     reservation_repository.read('1')))
    undoredoservice.undo()
    assert len(reservation_repository.read()) == 0
    undoredoservice.redo()
    assert len(reservation_repository.read()) == 1
    '''stergere'''
    undoredoservice.adaugaOperatie(
        Deleteoperation(reservation_repository,
                        reservation_repository.read('1')))
    assert len(reservation_repository.read()) == 1
    reservation_service.delete_reservation('1')
    assert len(reservation_repository.read()) == 0
    undoredoservice.undo()
    assert len(reservation_repository.read()) == 1
    undoredoservice.redo()
    assert len(reservation_repository.read()) == 0
    '''modificare'''
    reservation_service.add_reservation('1',
                                        '1',
                                        '1',
                                        '12.12.2021',
                                        '12:12:12')
    reservation = reservation_repository.read('1')
    reservation_service.update_reservation('1',
                                           '1',
                                           '1',
                                           '23.12.1000',
                                           '14:14:14')
    undoredoservice.adaugaOperatie(
        Modifyoperation(reservation_repository,
                        reservation_repository.read('1'),
                        reservation))
    assert reservation_repository.read('1').idMovie == '1'
    assert reservation_repository.read('1').idClientCard == '1'
    assert reservation_repository.read('1').data == '23.12.1000'
    assert reservation_repository.read('1').ora == '14:14:14'
    undoredoservice.undo()
    assert reservation_repository.read('1').idMovie == '1'
    assert reservation_repository.read('1').idClientCard == '1'
    assert reservation_repository.read('1').data == '12.12.2021'
    assert reservation_repository.read('1').ora == '12:12:12'
    undoredoservice.redo()
    assert reservation_repository.read('1').idMovie == '1'
    assert reservation_repository.read('1').idClientCard == '1'
    assert reservation_repository.read('1').data == '23.12.1000'
    assert reservation_repository.read('1').ora == '14:14:14'
    '''Ștergerea tuturor rezervărilor dintr-un anumit interval de zile'''
    reservation_service.add_reservation('2',
                                        '1',
                                        '1',
                                        '12.12.1000',
                                        '12:12:12')
    assert len(reservation_repository.read()) == 2
    undoredoservice.adaugaOperatie(
        Deletealloperation(reservation_repository,
                           reservation_repository.read('1')))
    reservation_service.StergeRezervareZile('11.11.1000',
                                            '13.12.1000',
                                            reservation_repository.read(),
                                            [])
    assert len(reservation_repository.read()) == 1
    assert reservation_repository.read('2') is None
    assert reservation_repository.read('1') is not None
    undoredoservice.undo()
    assert len(reservation_repository.read()) == 2
    assert reservation_repository.read('2') is not None
    assert reservation_repository.read('1') is not None
    undoredoservice.redo()
    assert len(reservation_repository.read()) == 1
    assert reservation_repository.read('2') is None
    assert reservation_repository.read('1') is not None
    movie_service.delete_movie('1')
    clientcard_service.delete_clientcard('1')


def test_All_Service():
    test_movie_service()
    test_cardclient_service()
    test_reservation_service()
    test_cerinte_service()
    test_undo_redo_service()
