class Pessoa:
    olhos = 2

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

    p.sobrenome = 'Jack'
    print(p.sobrenome)
    del joe.filhos
    print(joe.__dict__)
    print(p.__dict__)
    p.olhos = 1
    del p.olhos
    print(Pessoa.olhos)
    print(joe.olhos)
    print(p.olhos)