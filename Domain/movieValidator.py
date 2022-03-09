from Domain.movie import Movie
from Domain.movie_error import MovieError


class MovieValidator:
    def valideaza(self, movie: Movie):
        erori = []
        if movie.year < 0:
            erori.append('Anul introdus trebuie sa fie un numar pozitiv')
        if movie.ticketPrice < 0:
            erori.append('Pretul biletului trebuie sa fie un numar pozitiv ')
        if movie.inProgram not in ['da', 'nu']:
            erori.append("Filmul poate fi 'da' "
                         "daca mai este in program "
                         "sau 'nu' in rest!")
        if len(erori) > 0:
            raise MovieError(erori)
