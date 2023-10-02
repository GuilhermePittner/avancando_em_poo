class Programa:
    def __init__(self, nome: str, ano: int) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes


    def like_content(self):
        self.__likes += 1

    
    @property
    def nome(self):
        return self.__nome
    

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    
class Filme(Programa):

    def __init__(self, nome: str, ano: int, duracao: int) -> None:
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):

    def __init__(self, nome: str, ano: int, temporadas: int) -> None:
        super().__init__(nome, ano)
        self.temporadas = temporadas


pg_um = Programa('ratinho', 1998)
print(pg_um.ano)

filme_um = Filme('coraline', 2009, 107)
print(filme_um.nome)
print(filme_um.duracao)
