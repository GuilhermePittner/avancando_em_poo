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
        self.__nome = nome
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



"""
filme_um = Filme('Coraline', 2009, 107)
print(filme_um.nome)


serie_um = Serie('Young Sheldon', 2017, 6)
print(serie_um.temporadas)
"""

filme_um = Filme('o estranho mundo de jack', 2009, 107)
print(filme_um.nome)
filme_um.nome = 'coraline e o mundo secreto'
print(filme_um.nome)
filme_um.like_content()
filme_um.like_content()
filme_um.like_content()
filme_um.like_content()
print(filme_um.likes)

print('--------------')
serie_um = Serie('two and a half men', 2003, 12)
print(serie_um.nome)
serie_um.nome = 'the walking dead'
print(serie_um.nome)
serie_um.like_content()
print(serie_um.likes)