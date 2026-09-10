# Exibir mensagem de boas-vindas.
print('Bem vindo ao Sistema do Daniel Lisboa Gonçalves')

# Verificar valor_base e idade do cliente.
valor_base = float(input('Informe o valor base do plano: R$'))
idade = int(input('Informe a idade do cliente: '))

# Aplicar porcentagem conforme a idade do cliente.
if (idade >= 0 and idade < 19):
   porcentagem = 100 / 100 # Simplificando 1.00
elif (idade >= 19 and idade < 29):
   porcentagem = 150 / 100 # Simplificando 1.50
elif (idade >= 29 and idade < 39):
   porcentagem = 225 / 100 # Simplificando 2.25
elif (idade >= 39 and idade < 49):
   porcentagem = 240 / 100 # Simplificando 2.40
elif (idade >= 49 and idade < 59):
   porcentagem = 350 / 100 # Simplificando 3.50
else:
   porcentagem = 600 / 100 # Simplificando 6.00

# Calcula valor mensal do plano
valor_mensal = valor_base * porcentagem

# Exibir mensagem do valor mensal do plano.
print(f'O valor mensal do plano é de: R${valor_mensal:.2f}')