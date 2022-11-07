from email.errors import NonASCIILocalPartDefect


class Pessoa:
    def __init__(self,nome,ano_nasc):
        self._nome = nome
        self._ano_nasc = ano_nasc
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nasc
    
    def get_nome(self): 
        return self._nome
    
    def get_idade(self):
        return 2022 - self._ano_nasc
    
pessoa = Pessoa("Felipe", 1993)
print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade}")
print(f"Nome: {pessoa.get_nome()}\nIdade: {pessoa.get_idade()}") # O Método com get "def" também funciona, mas não é muito utilizado em Python, pois usaremos mais nele o property