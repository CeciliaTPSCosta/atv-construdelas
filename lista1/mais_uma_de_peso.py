# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

# engolindo o orgulho, farei esta questão como ela é, mas não queria.

h_m = input('Digite h se você é homem e m se você é mulher')
altura = float(input('Qual a sua altura?'))
if h_m == 'm':
    print(f'Seu peso ideal é: {(62.1 * altura) - 44.7}')
else:
    print(f'Seu peso ideal é: {(72.7 * altura) - 58}')
