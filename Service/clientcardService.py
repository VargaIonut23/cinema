from datetime import date
from typing import Optional, List

from Domain.addoperation import Addoperation
from Domain.clientcard import ClientCard
from Domain.clientcardValidator import ClientCardValidator
from Domain.deleteoperation import Deleteoperation
from Domain.incrementarepuncteoperation import Incrementarepuncteoperation
from Domain.modifyoperations import Modifyoperation
from Repository.repository import Repository
from Service.reservationService import ReservationService
from Service.sort import sort
from Service.undoredoservice import Undoredoservice


class ClientCardService:
    def __init__(self,
                 clientcard_repository: Repository,
                 clientcard_validator: ClientCardValidator,
                 reservation_repository: Repository,
                 reservationService: ReservationService,
                 undoredoservice: Undoredoservice):
        self.clientcard_repository = clientcard_repository
        self.clientcard_validator = clientcard_validator
        self.reservation_repository = reservation_repository
        self.__reservationService = reservationService
        self.undoredoservice = undoredoservice

    def add_clientcard(self,
                       idClientCard: str,
                       Nume: str,
                       Prenume: str,
                       CNP: str,
                       DataNasterii: str,
                       DataInregistrarii: str,
                       PuncteAcumulate: int):

        '''
        :param idClientCard: id ul clientcardului
        :param Nume: numele clientcardului
        :param Prenume: prenumele clientcardului
        :param CNP: cnp ul clientcardului
        :param DataNasterii: data nasterii clientcardului
        :param DataInregistrarii: data inregistrarii clientcardului
        :param PuncteAcumulate: punctele acumulate clientcardului
        adauga clientcardul cu noile date
        '''

        clientcard = ClientCard(idClientCard,
                                Nume,
                                Prenume,
                                CNP,
                                DataNasterii,
                                DataInregistrarii,
                                PuncteAcumulate)
        self.clientcard_validator.valideaza(clientcard)
        self.clientcard_repository.create(clientcard)
        self.undoredoservice.adaugaOperatie(
            Addoperation(self.clientcard_repository, clientcard))

    def update_clientcard(self,
                          idClientCard: str,
                          Nume: str,
                          Prenume: str,
                          CNP: str,
                          DataNasterii: str,
                          DataInregistrarii: str,
                          PuncteAcumulate: int):
        '''
        :param idClientCard: id ul clientcardului de modificat
        :param Nume: numele clientcardului de modificat
        :param Prenume: prenumele clientcardului de modificat
        :param CNP: cnp ul clientcardului de modificat
        :param DataNasterii: data nasterii clientcardului de modificat
        :param DataInregistrarii: data inregistrarii
        clientcardului de modificat
        :param PuncteAcumulate: punctele acumulate clientcardului de modificat
        modifica clientcardul cu id ul dat cu noile date
        '''
        oldclientcard = self.clientcard_repository.read(idClientCard)
        clientcard = ClientCard(idClientCard,
                                Nume,
                                Prenume,
                                CNP,
                                DataNasterii,
                                DataInregistrarii,
                                PuncteAcumulate)
        self.clientcard_validator.valideaza(clientcard)
        self.clientcard_repository.update(clientcard)
        self.undoredoservice.adaugaOperatie(
            Modifyoperation(self.clientcard_repository,
                            clientcard,
                            oldclientcard))

    def delete_clientcard(self, clientcard_id):
        '''
        :param clientcard_id: id ul clientcardului de sters
        sterge clientcardul cu id ul dat
        '''
        self.undoredoservice.adaugaOperatie(
            Deleteoperation(self.clientcard_repository,
                            self.clientcard_repository.read(clientcard_id)))
        for r in self.reservation_repository.read():
            if r.idClientCard == clientcard_id:
                self.__reservationService.delete_reservation(r.entity_id)
        self.clientcard_repository.delete(clientcard_id)

    def show_all_clientcards(self) -> List[ClientCard]:
        '''
        :return: lista cu toate clientcardurile
        '''
        return self.clientcard_repository.read()

    def show_clientcard(self, clientcard_id) -> Optional[ClientCard]:
        '''
        :param clientcard_id: id ul clientcardului de returnat
        :return: clientcardul cu id ul dat
        '''
        return self.clientcard_repository.read(clientcard_id)

    def convertationstringdate(self,
                               date_time_str,
                               date_time_comp1,
                               date_time_comp2) -> bool:
        '''

        :param date_time_str: data care va fi comparata cu celelalte doua
        :param date_time_comp1: prima data introdusa de utilizator
        :param date_time_comp2: a doua data introdusa de utilizator
        :return: 1 daca data se afla intre
         cele doua date introduse de utilizator
        si 0 in rest
        '''
        date_time_str_obj_test = date_time_str.split('.')
        dd = int(date_time_str_obj_test[0])
        mm = int(date_time_str_obj_test[1])
        yyyy = int(date_time_str_obj_test[2])
        datec = date(yyyy, mm, dd)
        date_time_comp1_test = date_time_comp1.split('.')
        dd = int(date_time_comp1_test[0])
        mm = int(date_time_comp1_test[1])
        yyyy = int(date_time_comp1_test[2])
        d1 = date(yyyy, mm, dd)
        date_time_comp2_test = date_time_comp2.split('.')
        dd = int(date_time_comp2_test[0])
        mm = int(date_time_comp2_test[1])
        yyyy = int(date_time_comp2_test[2])
        d2 = date(yyyy, mm, dd)

        if (datec > d1 and datec < d2) or (datec < d1 and datec > d2):
            return True
        return False

    def adaugarepuncte(self, puncte, date1, date2):
        '''
        :param puncte: numarul de puncte introdus de utilizator
        :param date1: prima data introdusa de utilizator
        :param date2: a doua data introdusa de utilizator
        va adauga puncte cardului client daca data nasterii se afla
        intre cele doua date scrise de utilizator
        '''
        lista = []
        lista1 = list(filter(lambda card:
                             ClientCardService.convertationstringdate(
                                self,
                                card.DataNasterii,
                                date1,
                                date2),
                             self.clientcard_repository.read()))
        for card in lista1:
            card.PuncteAcumulate += puncte
            self.clientcard_repository.update(card)
            lista.append(card)

        self.undoredoservice.adaugaOperatie(
            Incrementarepuncteoperation(self.clientcard_repository,
                                        lista,
                                        puncte))

    def OrdonareClientCards(self):
        lista1 = []
        lista = list(map(lambda x: x, self.clientcard_repository.read()))
        for x in lista:
            lista1.append(x.PuncteAcumulate)
        newlist = sort(lista, lista1, True)
        return newlist
