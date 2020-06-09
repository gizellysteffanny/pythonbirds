class Pessoa:

    def __init__(self,*filhos, nome=None, idade=21):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    joe = Pessoa(nome='Joe')
    p = Pessoa(joe, nome='John')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)

    for filho in p.filhos:
        print(filho.nome)
