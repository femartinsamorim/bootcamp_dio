# POSITIONAL ONLY

#def criar_carro(modelo,ano,placa,/,marca,motor,combustivel): 
#	print (modelo,ano,placa,marca,motor,combustivel)

#criar_carro("Palio",1999,"ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")
#criar_carro("Palio",1999,"ABC-1234","Fiat","1.0","Gasolina")
#criar_carro(modelo="Palio",ano=1999,placa="ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")

# KEYWORD ONLY

#def criar_carro(*,modelo,ano,placa,marca,motor,combustivel): 
#	print (modelo,ano,placa,marca,motor,combustivel)
 
#criar_carro(modelo="Palio",ano=1999,placa="ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")
#criar_carro("Palio",1999,"ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")

# KEYWORD E POSITIONAL ONLY

#def criar_carro(modelo,ano,placa,/,*,marca,motor,combustivel):
def criar_carro(modelo,ano,placa,/,marca,*,motor,combustivel): 
	print (modelo,ano,placa,marca,motor,combustivel)
 
#criar_carro("Palio",1999,"ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")
#criar_carro(modelo="Palio",ano=1999,placa="ABC-1234",marca="Fiat",motor="1.0",combustivel="Gasolina")
criar_carro("Palio",1999,"ABC-1234","Fiat",motor="1.0",combustivel="Gasolina")