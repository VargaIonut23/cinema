from Domain.clientcard import ClientCard
from Domain.clientcard_error import ClientCardError


class ClientCardValidator:
    def valideaza(self, client_card: ClientCard):
        errors = []
        if client_card.Nume.isalpha() is False:
            errors.append("Prenumele nu poate contine cifre.")
        if client_card.Prenume.isalpha() is False:
            errors.append("Numele nu poate contine cifre.")
        if client_card.CNP.isdigit() is False:
            errors.append("CNP-ul nu poate contine litere.")
        if client_card.DataNasterii is None:
            errors.append("Data de nastere introdusa nu este valida!")
        if client_card.DataInregistrarii is None:
            errors.append("Data si ora efectuarii tranzactiei nu sunt valide!")
        if len(client_card.CNP) < 13:
            errors.append("CNP-ul nu are 13 cifre!")
        if client_card.DataNasterii[2] != '.':
            errors.append('Data nasterii introdusa'
                          ' este incorecta')
        if client_card.DataNasterii[5] != '.':
            errors.append('Data nasterii introdusa'
                          ' este incorecta')
        if client_card.DataInregistrarii[2] != '.':
            errors.append('Data inregistrarii introdusa'
                          ' este incorecta')
        if client_card.DataInregistrarii[5] != '.':
            errors.append('Data inregistrarii introdusa'
                          ' este incorecta')
        if len(errors) > 0:
            raise ClientCardError(errors)
