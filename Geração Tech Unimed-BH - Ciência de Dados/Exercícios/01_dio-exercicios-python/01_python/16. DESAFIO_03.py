valores = input().split() 
tempo_gasto = int(valores[0])
velocidade_media = int(valores[1])
litros = velocidade_media / 12
litros_necessarios = tempo_gasto * litros
print(f"{litros_necessarios:1.3f}")
