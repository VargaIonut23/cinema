from typing import List, Optional

from Domain.addoperation import Addoperation
from Domain.deleteall import Deletealloperation
from Domain.deleteoperation import Deleteoperation
from Domain.modifyoperations import Modifyoperation
from Domain.movie import Movie
from Domain.movieValidator import MovieValidator
from Repository.repository import Repository
from Service.clientcardService import ClientCardService
from Service.reservationService import ReservationService
from Service.sort import sort
from Service.undoredoservice import Undoredoservice


class MovieService:

    def __init__(self, movie_repository: Repository,
                 movie_validator: MovieValidator,
                 reservation_repository: Repository,
                 reservationService: ReservationService,
                 clientcardService: ClientCardService,
                 undoredoservice: Undoredoservice):
        self.reservation_repository = reservation_repository
        self.movie_repository = movie_repository
        self.movie_validator = movie_validator
        self.__reservationService = reservationService
        self.clientcardService = clientcardService
        self.undoredoservice = undoredoservice

    def add_movie(self,
                  entity_id: str,
                  nameMovie: str,
                  year: int,
                  ticketPrice: float,
                  inProgram: str):
        '''
        :param entity_id: id ul filmului
        :param nameMovie: numele filmului
        :param year: anul filmului
        :param ticketPrice: pretul filmului
        :param inProgram: daca filmul este in program
        adauga un nou film cu atributele date
        '''
        movie = Movie(entity_id, nameMovie, year, ticketPrice, inProgram, 0)
        self.movie_validator.valideaza(movie)
        self.movie_repository.create(movie)
        self.undoredoservice.adaugaOperatie(
            Addoperation(self.movie_repository, movie))

    def update_movie(self,
                     entity_id: str,
                     nameMovie: str,
                     year: int,
                     ticketPrice: float,
                     inProgram: str):
        '''
        :param entity_id: id ul filmului de modificat
        :param nameMovie: numele filmului de modificat
        :param year: anul filmului de modificat
        :param ticketPrice: pretul filmului de modificat
        :param inProgram: daca filmul este in program
        modifica filmul cu id ul dat cu noile date
        '''
        oldmovie = self.movie_repository.read(entity_id)
        nrreservation = self.movie_repository.read(entity_id)
        movie = Movie(entity_id,
                      nameMovie,
                      year,
                      ticketPrice,
                      inProgram,
                      nrreservation.nrReservation)
        self.movie_validator.valideaza(movie)
        self.undoredoservice.adaugaOperatie(
            Modifyoperation(self.movie_repository, movie, oldmovie))
        self.movie_repository.update(movie)

    def delete_movie(self, entity_id: str):
        '''
        :param entity_id: id ul filmului de sters
        sterge filmul cu id ul dat
        '''
        reservation = []
        for r in self.reservation_repository.read():
            if r.idMovie == entity_id:
                reservation.append(r)
        if reservation:
            self.undoredoservice.adaugaOperatie(
                Deletealloperation(self.movie_repository,
                                   self.reservation_repository,
                                   self.movie_repository.read(entity_id),
                                   reservation))
            self.movie_repository.delete(entity_id)
            for r in reservation:
                self.reservation_repository.delete(r.entity_id)
        else:
            self.undoredoservice.adaugaOperatie(
                Deleteoperation(self.movie_repository,
                                self.movie_repository.read(entity_id)))
            self.movie_repository.delete(entity_id)

    def show_all_movies(self) -> List[Movie]:
        '''
        :return: returneza o lista cu toate
        filmele
        '''
        return self.movie_repository.read()

    def show_movie(self, entity_id: str) -> Optional[Movie]:
        '''
        :param entity_id: id ul filmului de returnat
        :return: returneza filmul cu id ul dat
        '''
        return self.movie_repository.read(entity_id)

    def OrdonareMovie(self) -> List[Movie]:
        '''
        :return: Lista cu filmele existente in ordine descrescatoare dupa nr
        de rezervari
        '''
        lista1 = []
        lista = list(map(lambda x: x, self.movie_repository.read()))
        for x in lista:
            lista1.append(x.nrReservation)
        newlist = sort(lista, lista1, True)
        return newlist

    def FullText(self, search_this):
        result = []
        movie_repo = self.show_all_movies()
        cards_repo = self.clientcardService.show_all_clientcards()
        for movie in movie_repo:
            if search_this in movie.nameMovie or \
                    search_this in str(movie.year) or \
                    search_this in str(movie.ticketPrice) or \
                    search_this in movie.inProgram or \
                    search_this in str(movie.nrReservation):
                result.append(movie)
        for card in cards_repo:
            if search_this in card.Nume or \
                    search_this in card.Prenume or \
                    search_this in card.CNP or \
                    search_this in str(card.PuncteAcumulate) or \
                    search_this in card.DataInregistrarii or \
                    search_this in card.DataNasterii:
                result.append(card)
        return result
