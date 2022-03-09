from datetime import date, time
from typing import List, Optional

from Domain.addoperation import Addoperation
from Domain.deletealloperation import Deletealloperation
from Domain.deleteoperation import Deleteoperation
from Domain.modifyoperations import Modifyoperation
from Domain.reservation import Reservation
from Domain.reservationValidator import ReservationValidator
from Repository.repository import Repository
from Service.undoredoservice import Undoredoservice


class ReservationService:

    def __init__(self,
                 reservation_repository: Repository,
                 reservation_validator: ReservationValidator,
                 movie_repository: Repository,
                 clientcard_repository: Repository,
                 undoredoservice: Undoredoservice):
        self.clientcard_repository = clientcard_repository
        self.movie_repository = movie_repository
        self.reservation_repository = reservation_repository
        self.reservation_validator = reservation_validator
        self.undoredoservice = undoredoservice

    def add_reservation(self,
                        idReservation: str,
                        idMovie: str,
                        idClientCard: str,
                        data: str,
                        ora: str):
        '''
        :param idReservation: id ul rezervarii
        :param idMovie: id ul filmului rezervarii
        :param idClientCard:  id ul ClientCardului
         rezervarii
        :param data: data rezervarii
        :param ora: ora rezervarii
        adauga o noua rezervare cu atributele date
        '''
        movie = self.movie_repository.read(idMovie)
        if movie is None:
            raise ValueError('Nu exista filmul cu id-ul dat in lista de filme')
        clientcard = self.clientcard_repository.read(idClientCard)
        if clientcard is None:
            raise ValueError('Nu exista un clientcard'
                             ' cu id-ul dat in lista de filme')

        reservation = Reservation(idReservation,
                                  idMovie,
                                  idClientCard,
                                  data,
                                  ora)
        self.reservation_validator.validator(reservation)
        self.reservation_repository.create(reservation)

        clientcard.PuncteAcumulate += movie.ticketPrice // 10
        self.clientcard_repository.update(clientcard)

        movie.nrReservation += 1
        self.movie_repository.update(movie)
        self.undoredoservice.adaugaOperatie(
            Addoperation(self.reservation_repository, reservation))

    def update_reservation(self,
                           idReservation: str,
                           idMovie: str,
                           idClientCard: str,
                           data: str,
                           ora: str):
        '''
        :param idReservation: id ul rezervarii de modificat
        :param idMovie: id ul filmului rezervarii de modificat
        :param idClientCard: id ul ClientCardului
         rezervarii de modificat
        :param data: data rezervarii de modificat
        :param ora: ora rezervarii de modificat
        modifica rezervarea cu id ul dat cu noile atribute
        '''
        oldreservation = self.reservation_repository.read(idReservation)
        idmovie = self.reservation_repository.read(idReservation).idMovie
        movie = self.movie_repository.read(idmovie)
        movie.nrReservation -= 1
        self.movie_repository.update(movie)
        reservation = Reservation(idReservation,
                                  idMovie,
                                  idClientCard,
                                  data,
                                  ora)
        self.reservation_validator.validator(reservation)
        self.undoredoservice.adaugaOperatie(
            Modifyoperation(self.movie_repository,
                            reservation,
                            oldreservation))
        self.reservation_repository.update(reservation)
        movie = self.movie_repository.read(idMovie)
        movie.nrReservation += 1
        self.movie_repository.update(movie)

    def delete_reservation(self, reservation_id: str):
        '''
        :param reservation_id: id ul rezervarii de sters
        sterge rezervarea cu id ul dat
        '''
        self.undoredoservice.adaugaOperatie(
            Deleteoperation(self.reservation_repository,
                            self.reservation_repository.read(reservation_id)))
        idmovie = self.reservation_repository.read(reservation_id).idMovie
        movie = self.movie_repository.read(idmovie)
        movie.nrReservation -= 1
        self.movie_repository.update(movie)
        self.reservation_repository.delete(reservation_id)

    def show_all_reservations(self) -> List[Reservation]:
        '''
        :return: lista cu toate rezervarile
        '''
        return self.reservation_repository.read()

    def show_reservation(self, reservation_id: str) -> Optional[Reservation]:
        '''
        :param reservation_id: id ul rezervarii de gasit
        :return: rezervarea cu id ul dat
        '''
        return self.reservation_repository.read(reservation_id)

    def convertationstringdate(self,
                               date_time_str,
                               date_time_comp1,
                               date_time_comp2) -> bool:
        '''

                :param date_time_str: data care
                va fi comparata cu celelalte doua
                :param date_time_comp1: prima data introdusa de utilizator
                :param date_time_comp2: a doua data introdusa de utilizator
                :return: 1 daca data se afla
                intre celle doua date introduse de utilizator
                si 0 in rest
                '''
        date_time_str_obj_test = date_time_str.split('.')
        dd = int(date_time_str_obj_test[0])
        mm = int(date_time_str_obj_test[1])
        yyyy = int(date_time_str_obj_test[2])
        date_time_str_obj = date(yyyy, mm, dd)
        date_time_comp1_test = date_time_comp1.split('.')
        dd = int(date_time_comp1_test[0])
        mm = int(date_time_comp1_test[1])
        yyyy = int(date_time_comp1_test[2])
        date_time_comp1_obj = date(yyyy, mm, dd)
        date_time_comp2_test = date_time_comp2.split('.')
        dd = int(date_time_comp2_test[0])
        mm = int(date_time_comp2_test[1])
        yyyy = int(date_time_comp2_test[2])
        date_time_comp2_obj = date(yyyy, mm, dd)
        if (date_time_str_obj > date_time_comp1_obj and
            date_time_str_obj < date_time_comp2_obj)\
                or (date_time_str_obj < date_time_comp1_obj and
                    date_time_str_obj > date_time_comp2_obj):
            return True
        return False

    def convertationstringtime(self,
                               hour_str,
                               hour_comp1_str,
                               hour_comp2_str) -> bool:
        '''
        :param hour_str: ora care va fi comparata cu celelalte doua
        :param hour_comp1_str: prima ora introdusa de utilizator
        :param hour_comp2_str: a doua ora introdusa de utilizator
        :return: 1 daca ora se afla intre cele
        doua date introduse de utilizator si 0 in rest
        '''
        hour_str_test = hour_str.split(':')
        hh = int(hour_str_test[0])
        mm = int(hour_str_test[1])
        ss = int(hour_str_test[2])
        hour = time(hh, mm, ss)
        hour_comp1_str_test = hour_comp1_str.split(':')
        hh = int(hour_comp1_str_test[0])
        mm = int(hour_comp1_str_test[1])
        ss = int(hour_comp1_str_test[2])
        h1 = time(hh, mm, ss)
        hour_comp2_str_test = hour_comp2_str.split(':')
        hh = int(hour_comp2_str_test[0])
        mm = int(hour_comp2_str_test[1])
        ss = int(hour_comp2_str_test[2])
        h2 = time(hh, mm, ss)
        if (hour > h1 and hour < h2) or (hour < h1 and hour > h2):
            return True
        return False

    def StergeRezervareZile(self, data1, data2, lista: list, reservations):
        '''
        :param data1: prima data introdusa de utilizator
        :param data2: a doua data introdusa de utilizator
        sterge rezervarile facute in intevalul celor doua dati
        '''

        '''lista = list((filter(lambda x: self.convertationstringdate(x.data,
                                                                   data1,
                                                                   data2),
                             self.show_all_reservations())))
        for x in lista:
            reservations.append(x)
            self.reservation_repository.delete(x.entity_id)'''
        if lista == []:
            return 0
        if self.convertationstringdate(lista[0].data, data1, data2):
            reservations.append(lista[0])
            self.undoredoservice.adaugaOperatie(
                Deletealloperation(self.reservation_repository,
                                   reservations))
            self.reservation_repository.delete(lista[0].entity_id)
        return self.StergeRezervareZile(data1,
                                        data2,
                                        list(lista[1:]),
                                        reservations)

    def AfisareRezervareOre(self, ora1, ora2):
        newlist = []
        [newlist.append(self.show_reservation(x.entity_id))
         for x in self.show_all_reservations()
         if self.convertationstringtime(x.ora, ora1, ora2)]
        if len(newlist) == 0:
            newlist.append('Nu exista o rezervare intre orele date')
        return newlist
