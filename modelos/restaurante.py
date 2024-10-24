from modelos.avaliacao import avaliacao # type: ignore

class restaurante:
    # lista que armazena todos os restaurantes cadastrados
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() # nome do restaurante, formato com a primeira letra maiuscula
        self._categoria = categoria.upper() # categoria do restaurante, formatada em letras maiuscula
        self._ativo = False # estado inicial do restaurante, definido como inativo
        self._avaliacao = [] # listas que armazena as avaliações do restaurante
        restaurante.restaurantes.append(self) # adiciona o restaurante à lista global de restaurantes

    def __str__(self):
        # retorna um representação textual do restaurante, mostrando nome e categoria
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        # exibe a lista de todos os restaurantes cadastrados
        print(" ")
        print(f"{'nome do restaurante'.ljust(25)} | {'categoria'.just(25)} | {'avaliação'.ljust(25)} | {'status'}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media.avaliacoes).ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        #retorna um simbolo visual representando se o restaurante está ativo ou inativo
        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
        # alterna o estado do restaurante entre ativo e inativo
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        # adiciona uma nova avliação ao restaurante, desde que a nota esteja entre 0 e 10
        if 0 <= nota <=10:
            avaliacao = avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        else:
            print("a nota deve estar entre 0 e 10.")
        
    @property
    def media_avaliacoes(self):
        # calcula e retorna a média das avaliações do restaurante
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(some_das_notas / quantidade_de_notas, 1) # type: ignore
        return media
