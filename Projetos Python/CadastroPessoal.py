#definindo as variáveis
galera = list()
pessoa = dict()
soma = media = 0

#importando a biblioteca time para utilizar a função sleep
import time

print(' Cadastro Pessoal ') 
time.sleep(1)

while True: #Definindo o nome da pessoa
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))  

    while True: #Validação do sexo
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper() [0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')


    while True: #Validação do idade
        try:
            pessoa['idade'] = int(input('Idade: '))
            if pessoa['idade'] < 0:
                print('ERRO! Idade não pode ser negativa. Digite novamente.')
            else:
                break
            print('ERRO! Idade não pode ser negativa. Digite novamente.')
        except ValueError:
            print('ERRO! Por favor, digite apenas números para a idade.')

    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True: #Validação da resposta para continuar ou não
        resp = str(input('Quer continuar? [S/N] ')).upper() [0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N! ')
    if resp == 'N':
        break
    
#Resultados
print('-=' * 30) 
print(f'Ao todo foram {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f' A média de idade é de {media:5.2f}. ')
print(f'As mulheres cadastradas foram', end='')

for p in galera: #Iterando sobre a lista de pessoas
    if p['sexo'] == 'F':
        print(f' {p["nome"] }' , end='')
print()
#Lista de pessoas que estão acima da média da idade
print('Lista de pessoas que estão acima da média da idade:')
for p in galera:
    if p ['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('<< ENCERRADO >>')