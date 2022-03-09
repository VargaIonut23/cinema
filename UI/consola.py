
from Service.clientcardService import ClientCardService
from Service.movieService import MovieService
from Service.randommovie import unique_strings, inProgram, unique_number
from Service.reservationService import ReservationService
from Service.undoredoservice import Undoredoservice


class Consola:
    def __init__(self,
                 movieService: MovieService,
                 clientcardService: ClientCardService,
                 reservationService: ReservationService,
                 undoredoservice: Undoredoservice):
        self.__movieService = movieService
        self.__clientcardService = clientcardService
        self.__reservationService = reservationService
        self.__undoredoservice = undoredoservice

    def runMenu(self):
        while True:
            print("1. CRUD film")
            print("2. CRUD card client")
            print("3. CRUD rezervari")
            print("4. Căutare full text")
            print("u. Undo")
            print("r. Redo")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.runCRUDMoviesMenu()
            elif optiune == "2":
                self.runCRUDCardClientMenu()
            elif optiune == "3":
                self.runCRUDReservationMenu()
            elif optiune == "4":
                self.runFULLTEXT()
            elif optiune == "u":
                self.__undoredoservice.undo()
            elif optiune == "r":
                self.__undoredoservice.redo()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runCRUDMoviesMenu(self):
        while True:
            print("1. Adauga film")
            print("2. Sterge film")
            print("3. Modifica film")
            print("4. Afișarea filmelor ordonate "
                  "descrescător după numărul de rezervări.")
            print("rd. Genereaza un film random")
            print("a. Afiseaza toate filmele")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAddMovie()
            elif optiune == "2":
                self.uiDeleteMovie()
            elif optiune == "3":
                self.uiModifyMovie()
            elif optiune == "4":
                self.uiOrdonareMovie()
            elif optiune == "rd":
                self.uirandom()
            elif optiune == "a":
                self.showAllMovies()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAddMovie(self):
        try:
            idMovie = input("Dati id-ul filmului: ")
            name = input("Dati numele filmului: ")
            year = int(input("Dati anul filmului: "))
            ticketPrice = float(input("Dati pretul biletului: "))
            inProgram = input("Precizati daca filmul este in program: ")

            self.__movieService.add_movie(idMovie,
                                          name,
                                          year,
                                          ticketPrice,
                                          inProgram)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiDeleteMovie(self):
        try:
            idMovie = input("Dati id-ul filmului de sters: ")
            self.__movieService.delete_movie(idMovie)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModifyMovie(self):
        try:
            idMovie = input("Dati id-ul filmului de modificat: ")
            name = input("Dati numele filmului de modificat: ")
            year = int(input("Dati anul filmului de modificat: "))
            ticketprice = int(input("Dati pretul biletului de modificat: "))
            inProgram = input("Precizati daca filmul de "
                              "modificat este in program: ")
            self.__movieService.update_movie(idMovie,
                                             name,
                                             year,
                                             ticketprice,
                                             inProgram)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllMovies(self):
        for movie in self.__movieService.show_all_movies():
            print(movie)

    def runCRUDCardClientMenu(self):
        while True:
            print("1. Adauga card")
            print("2. Sterge card")
            print("3. Modifica card")
            print("4. Afișarea cardurilor client ordonate"
                  " descrescător după numărul de puncte de pe card.")
            print("5. Incrementarea cu o valoare dată a punctelor de"
                  " pe toate cardurile a căror zi de naștere se află"
                  " într-un interval dat.")
            print("a. Afiseaza toate cardurile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAddClientCard()
            elif optiune == "2":
                self.uiDeleteClientCard()
            elif optiune == "3":
                self.uiModifyClientCard()
            elif optiune == "4":
                self.uiOrdonareCardClient()
            elif optiune == "5":
                self.uiIncrementarePuncte()
            elif optiune == "a":
                self.showAllClientCards()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAddClientCard(self):
        try:
            idClientCard = input("Dati id-ul cardului: ")
            Nume = input("Dati numele celui care detine cardul: ")
            Prenume = input("Dati prenumele celui care detine cardul: ")
            CNP = input("Dati CNP ul celui care detine cardul: ")
            DataNasterii = input("Dati data nasterii "
                                 "persoanei care detine cardul (dd.mm.yyyy): ")
            DataInregistrarii = input("Dati data inregistrarii (dd.dd.yyyy): ")
            PuncteAcumulate = int(input("Dati numarul de puncte acumulate: "))

            self.__clientcardService.add_clientcard(idClientCard,
                                                    Nume,
                                                    Prenume,
                                                    CNP,
                                                    DataNasterii,
                                                    DataInregistrarii,
                                                    PuncteAcumulate)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiDeleteClientCard(self):
        try:
            idClientCard = input("Dati id-ul cardului de sters: ")
            self.__clientcardService.delete_clientcard(idClientCard)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModifyClientCard(self):
        try:
            idClientCard = input("Dati id-ul cardului de modificat: ")
            Nume = input("Dati numele celui care detine cardul de modificat: ")
            Prenume = input("Dati prenumele celui "
                            "care detine cardul de modificat: ")
            CNP = input("Dati CNP ul celui care detine cardul de modificat: ")
            DataNasterii = input("Dati data nasterii persoanei care "
                                 "detine cardul (d.mm.yyyy) de modificat: ")
            DataInregistrarii = input("Dati data inregistrarii "
                                      "(dd.mm.yyyy) de modificat: ")
            PuncteAcumulate = int(input("Dati numarul "
                                        "de puncte acumulate de modificat: "))

            self.__clientcardService.update_clientcard(idClientCard,
                                                       Nume,
                                                       Prenume,
                                                       CNP,
                                                       DataNasterii,
                                                       DataInregistrarii,
                                                       PuncteAcumulate)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllClientCards(self):
        for clientcard in self.__clientcardService.show_all_clientcards():
            print(clientcard)

    def runCRUDReservationMenu(self):
        while True:
            print("1. Adauga rezervare")
            print("2. Sterge rezervare")
            print("3. Modifica rezervare")
            print("4. Ștergerea tuturor rezervărilor "
                  "dintr-un anumit interval de zile.")
            print("5. Afișarea tuturor rezervărilor "
                  "dintr-un interval de ore dat, "
                  "indiferent de zi.")
            print("a. Afiseaza toate rezervare")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaRezervare()
            elif optiune == "2":
                self.uiStergeRezervare()
            elif optiune == "3":
                self.uiModificaRezervare()
            elif optiune == "4":
                self.uiStergeRezervareZile()
            elif optiune == "5":
                self.uiAfisareRezervareOre()
            elif optiune == "a":
                self.showAllRezervari()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaRezervare(self):
        try:
            idReservation = input("Dati id-ul rezervarii: ")
            idMovie = input("Dati id-ul filmului: ")
            idClientCard = input("Dati id-ul cardului: ")
            data = input("Dati data (dd.mm.yyyy): ")
            ora = input("Dati ora (hh:mm:ss): ")

            self.__reservationService.add_reservation(
                    idReservation,
                    idMovie,
                    idClientCard,
                    data,
                    ora)

        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeRezervare(self):
        try:
            idRezervare = input("Dati id-ul rezervarii de sters: ")

            self.__reservationService.delete_reservation(idRezervare)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaRezervare(self):
        try:
            idReservation = input("Dati id-ul rezervarii de modificat: ")
            idMovie = input("Dati id-ul filmului de modificat: ")
            idClientCard = input("Dati id-ul cardului de modificat: ")
            data = input("Dati data (dd.mm.yyyy) de modificat: ")
            ora = input("Dati ora de modificat (hh:mm:ss): ")

            self.__reservationService.update_reservation(
                idReservation,
                idMovie,
                idClientCard,
                data,
                ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllRezervari(self):
        for reservation in self.__reservationService.show_all_reservations():
            print(reservation)

    def uirandom(self):
        try:
            n = int(input("Dati un numar natural: "))
            for i in range(0, n):
                list1 = unique_strings(4, 2)
                list2 = []
                for x in list1:
                    list2.append(x)
                self.__movieService.add_movie(list2[0],
                                              list2[1],
                                              unique_number(),
                                              unique_number(),
                                              inProgram())
        except ValueError as ve:
            print(ve)

    def uiOrdonareCardClient(self):
        newlist = self.__clientcardService.OrdonareClientCards()
        for list in newlist:
            print(list)

    def uiStergeRezervareZile(self):
        data1 = input("Dati o data (dd.mm.yyyy): ")
        data2 = input("Dati o data (dd.mm.yyyy): ")
        self.__reservationService.\
            StergeRezervareZile(data1,
                                data2,
                                self.__reservationService.
                                reservation_repository.
                                read(),
                                [])

    def uiAfisareRezervareOre(self):
        ora1 = input("Dati o ora (hh:mm:ss): ")
        ora2 = input("Dati o ora (hh:mm:ss): ")
        newlist = self.__reservationService.AfisareRezervareOre(ora1,
                                                                ora2)
        for list in newlist:
            print(list)

    def uiIncrementarePuncte(self):
        date1 = input("Dati o data (dd.mm.yyyy): ")
        date2 = input("Dati o data (dd.mm.yyyy): ")
        try:
            puncte = int(input("Dati numarul de puncte care sa fie adaugat: "))
        except ValueError as ve:
            print(ve)
            return
        self.__clientcardService.adaugarepuncte(puncte, date1, date2)

    def uiOrdonareMovie(self):
        newlist = self.__movieService.OrdonareMovie()
        for list in newlist:
            print(list)

    def runFULLTEXT(self):
        '''
        cauta in toate filmele si cardurile client segventa data de utilizator
        '''
        search_this = input("Cautati in lista de filme si clienti: ")
        result = []
        result = self.__movieService.FullText(search_this)
        if len(result) > 0:
            for x in result:
                print(x)
        else:
            print("Nu s-a gasit nimic :( ")
