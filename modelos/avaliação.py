class avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente #nome do cliente que fez a avaliação
        self._nota = nota # nota dada pelo cliente
    
    # metodo para converter o objeto avaliação em um dicionario para salvar JSON
    def __dict__(self):
        return {
            'cliente': self._cliente,
            'nota': self._nota
        }
    