"""

8. Criar um programa em Python que solicite três números ao usuário, utilize estruturas condicionais para determinar o maior entre eles e apresente o resultado.

"""

numero_1,numero_2,numero_3 = input("Insira os três números separados por uma virgula:\n").split(",")
numero_1 =float(numero_1)
numero_2 = float(numero_2)
numero_3 = float(numero_3)


maior = 0
if numero_1 == numero_2 == numero_3:
    print("Todos os números são iguais.")
elif numero_1 == numero_2 and numero_1>numero_3:
    print(f"{numero_1} e {numero_2} são iguais e maiores que {numero_3}")
    print(f"Os maiores numeros são: {numero_1} e {numero_2}")
elif numero_1 == numero_2 and numero_1<numero_3:
    maior = numero_3
    print(f"{numero_1} e {numero_2} são iguais e menores que {numero_3}")
    print (f"O maior numero entre os tres é: {maior}")    
    #
elif numero_2 == numero_3 and numero_2>numero_1:
    print(f"{numero_2} e {numero_3} são iguais e maiores que {numero_1}")
    print(f"Os maiores numeros são: {numero_2} e {numero_3}")
elif numero_2 == numero_3 and numero_2<numero_1:
    maior = numero_1
    print(f"{numero_2} e {numero_3} são iguais e menores que {numero_1}")
    print (f"O maior numero entre os tres é: {maior}")
    #
elif numero_1 == numero_3 and numero_1>numero_2:
    print(f"{numero_1} e {numero_3} são iguais e maiores que {numero_2}")
    print(f"Os maiores numeros são: {numero_1} e {numero_3}")
elif numero_1 == numero_3 and numero_1 < numero_2:
    maior = numero_2
    print(f"{numero_1} e {numero_3} são iguais e menores que {numero_2}")
    print (f"O maior numero entre os tres é: {maior}")
    #
    
else:
    if numero_1 > numero_2 and numero_1 > numero_3:
        maior = numero_1
    elif numero_2 > numero_1 and numero_2 > numero_3:
        maior = numero_2
    else:
        maior = numero_3
    print(f"O maior numero entre os tres é: {maior}")