class Veiculo:
    def __init__(self, cor, placa, quantidade_rodas,):
        self.cor = cor
        self.placa = placa
        self.quantidade_rodas = quantidade_rodas
    
    def ligar_motor(self):
        print("Ligando o motor...")
        
    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass
    
class Carro(Veiculo):
    pass
        
class Caminhao(Veiculo):
    def __init__(self, cor, placa, quantidade_rodas, carregado):
        super().__init__(cor, placa, quantidade_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}, estou carregado")
              
    
#moto = Motocicleta("preto","abc-1234",2)
#print(moto)
#moto.ligar_motor()

#carro = Carro("branco","erf-5475",4)
#moto.ligar_motor()

caminhao = Caminhao("azul","cts-5865",4, True)
#moto.ligar_motor()
caminhao.esta_carregado()
caminhao.ligar_motor()
print(caminhao)
#carro.esta_carregado()