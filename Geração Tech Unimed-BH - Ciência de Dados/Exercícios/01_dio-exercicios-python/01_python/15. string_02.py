nome = "Felipe"
idade = 29
profissao = "Desenvolvedor"
linguagem = "Python"
saldo = 45.4350000

dados = {"nome": "Guilherme","idade":20,}

print("Nome: %s idade: %d Faço: %s Serei: %s" % (nome,idade,linguagem,profissao))

print("Nome: {} idade: {} Faço: {} Serei: {}" .format(nome,idade,linguagem,profissao))
print("Nome: {3} idade: {1} Faço: {0} Serei: {2} Ja disse meu nome? {3}" .format(linguagem,idade,profissao,nome))
print("Nome: {name} idade: {age}".format(name=nome,age=idade))
print("Nome: {nome} idade: {idade}".format(**dados))

print (f"Nome: {nome} e Profissão de {profissao}")

print (f"Nome: {nome} e Profissão de {profissao} seu saldo é de: {saldo}")
print (f"Nome: {nome} e Profissão de {profissao} seu saldo é de: {saldo:10.2f}")
print (f"Nome: {nome} e Profissão de {profissao} seu saldo é de: {saldo:.1f}")