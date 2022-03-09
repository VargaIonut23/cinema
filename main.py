from AllTest.testall import test_all
from Domain.clientcardValidator import ClientCardValidator
from Domain.movieValidator import MovieValidator
from Domain.reservationValidator import ReservationValidator
from Repository.repository_json import RepositoryJson
from Service.clientcardService import ClientCardService
from Service.movieService import MovieService
from Service.reservationService import ReservationService
from Service.undoredoservice import Undoredoservice
from UI.consola import Consola


def main():
    test_all()
    undoredoservice = Undoredoservice()
    reservation_repository = RepositoryJson('reservation.json')
    reservation_validator = ReservationValidator()

    clientcard_repository = RepositoryJson('clientcards.json')
    clientcard_validator = ClientCardValidator()

    movie_repository = RepositoryJson('movies.json')
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

    console = Consola(movie_service,
                      clientcard_service,
                      reservation_service,
                      undoredoservice)
    console.runMenu()


if __name__ == '__main__':
    main()
