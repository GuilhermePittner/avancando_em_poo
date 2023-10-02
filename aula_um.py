class Filme:

    def __init__(self, nome: str, ano: int, duracao: float) -> None:
        self.nome = nome
        self.ano = ano
        self.duracao = duracao


class Serie:

    def __init__(self, nome: str, ano: int, temporadas: int) -> None:
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


filme_um = Filme('Coraline', 2009, 107)
print(filme_um.nome)


serie_um = Serie('Young Sheldon', 2017, 6)
print(serie_um.temporadas)
