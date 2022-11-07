MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a carteira")
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a carteira")
    
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a carteira")
else:
    print("Ainda não pode tirar a carteira")
    
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a carteira")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas téoricas")
else:
    print("Ainda não pode tirar a carteira")