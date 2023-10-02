class Filme:

    def __init__(self, nome: str, ano: int, duracao: float) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
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


class Serie:

    def __init__(self, nome: str, ano: int, temporadas: int) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
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



filme_um = Filme('Coraline', 2009, 107)
print(filme_um.nome)


serie_um = Serie('Young Sheldon', 2017, 6)
print(serie_um.temporadas)
