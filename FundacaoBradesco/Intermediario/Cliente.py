class Cliente:
    def __init__(self, n, t): #init é o metodo construtor da classe em python; Todo método Python tem self como primeiro parâmetro.
        self._nome = n #atributos
        self._telefone = t

    def get_nome(self):
        return self._nome
    
    def set_nome(self, nome):
        self._nome = nome