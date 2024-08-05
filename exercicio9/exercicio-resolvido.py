# Desafio 2 - Exercicio 9
# Contadores de pares e ímpares
cont_pares = 0
cont_impares = 0

while True:
    try:
        # Solicitando um número ao usuário
        numero = int(input("Digite um número positivo (ou 0 para encerrar): "))
        
        # Verificando se o número é zero para encerrar o loop
        if numero == 0:
            break
        
        # Validando se o número é positivo
        if numero < 0:
            print("Por favor, insira apenas números positivos.")
            continue
        
        # Verificando se o número é par ou ímpar e atualizando os contadores
        if numero % 2 == 0:
            cont_pares += 1
        else:
            cont_impares += 1
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

# Apresentando a quantidade de números pares e ímpares
print(f"Quantidade de números pares inseridos: {cont_pares}")
print(f"Quantidade de números ímpares inseridos: {cont_impares}")
