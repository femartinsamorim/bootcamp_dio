class Passaro:
    def voar(self):
        print("voando....")

class Pardal(Passaro):
	def voar(self):
		super().voar()

class Avestruz(Passaro):
	def voar(self):
			print("Avestruz não voa")
   
class Aviao(Passaro):           # Exemplo ruim do uso de herança para "ganhar" o método voar 
    def voar(self):
            print("Avião está decolando...")

def plano_de_voo(obj):
    obj.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())