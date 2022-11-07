class cachorro:
    def __init__(self,nome,cor,acordado=True):
        print("Inicilizando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo a instãncia da classe.")
    
    def falar(self):
        print("Auau")
        
def criar_cachorro():
    c = cachorro("Caramelo","Caramelo",False)
    print(c.nome)
        
c = cachorro("Caramelo", "amarelo/caramelo")
c.falar()

print("TESTE")

del c

print("TESTE")
print("TESTE")
print("TESTE")

criar_cachorro()