from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass 
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando...")
        print("TV Ligada!")
    def desligar(self):
        print("Desligando...")
        print("TV Desligada!")
    
    @property
    def marca(self):
        return "LG"

class ControleAr(ControleRemoto):
    def ligar(self):
        print("Ligando...")
        print("Ar Ligado!")
    def desligar(self):
        print("Desligando...")
        print("Ar Desligado!")
        
    @property
    def marca(self):
        return "SAMSUNG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleAr()
controle.ligar()
controle.desligar()  
print(controle.marca)