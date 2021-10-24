# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1, nota2, nota3, nota4 = input('Digite as quatro notas separadas por espaço: ').split()
nota1 = int(nota1)
nota2 = int(nota2)
nota3 = int(nota3)
nota4 = int(nota4)
print('A média foi:', (nota1 + nota2 + nota3 + nota4) / 4)
