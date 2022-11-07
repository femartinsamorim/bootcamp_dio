class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("Plim plim")
        
    def parar(self):
        print("Parando bicicleta ...")
        print("bicicleta parada!")
    
    def correr(self):
        print("Vrummm....")
        
    def get_cor(self):      # Usado o get para não dar erro devido a declaração de "cor" acima
        return self.cor
    
    #def __str__(self):
    #    return f"bicliceta: Cor={self.cor}, Modelo={self.modelo}, Ano={self.ano}, Valor={self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
        
#b1 = bicicleta("vermelha","caloi",2022,600)
#b1.buzinar()
#b1.correr()
#b1.parar()
#print (b1.cor,b1.modelo,b1.ano,b1.valor)

b2 = bicicleta("verde","bmx",200,2500)
#bicicleta.buzinar(b2)
#b2.parar()
#print(b2.get_cor())
#print(b2.cor)
print(b2)


