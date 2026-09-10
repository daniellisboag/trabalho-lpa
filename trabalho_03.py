# Mensagem de boas-vindas
print('Bem vindo a Madeireira do Daniel Lisboa Gonçalves')

# Função para escolher o tipo de madeira
def escolha_tipo():
   while True: # inicia o laço de repetição
      print('Entre com o tipo de Madeira desejado')
      print('PIN - Tora de Pinho')
      print('PER - Tora de Peroba')
      print('MOG - Tora de Mogno')
      print('IPE - Tora de Ipê')
      print('IMB - Tora de Imbuia')
      tipoMadeira = input('Tipo escolhido: ') # Pergunta ao usuário o tipo de madeira escolhido
      if tipoMadeira in ('PIN', 'PER', 'MOG', 'IPE', 'IMB'): # Verificação do tipo de madeira escolhido
         # Verifica o tipo de madeira escolhido e retorna o valor por (m³)
         if tipoMadeira == 'PIN':
            return 150.40
         elif tipoMadeira == 'PER':
            return 160.20
         elif tipoMadeira == 'MOG':
            return 190.90
         elif tipoMadeira == 'IPE':
            return 210.10
         elif tipoMadeira == 'IMB':
            return 220.70
      else:
         # Retorna no começo do laço caso o usuário digite um tipo de madeira errado
         print('Escolha inválida, entre com o tipo novamente')
         print('')
         continue

# Função para escolher a quantidade de toras
def qtd_toras():
   while True: # Inicia o laço de repetição
      try: # Estrutura para tratar o tipo de erro (ValueError)
         quantidade = int(input('Entre com a quantidade de toras (m³): ')) # Pergunta ao usuário a quantidade de toras em (m³)
         # Se a quantidade for maior que 2000 retorna para o começo do laço de repetição
         if quantidade > 2000:
            print('')
            print('Não aceitamos pedidos com essa quantidade de toras.')
            print('Por favor, entre com a quantidade novamente.')
            print('')
         else:
            # Encerra o laço de repetição e retorna o valor da quantidade digitada
            return quantidade
      # Tratamento do erro caso digite um valor não numérico
      except ValueError:
         print('')
         print('Só aceitamos valores numéricos. Tente novamente!')
         print('')

# Função para escolher o tipo de transporte
def transporte():
   while True: # Inicia o laço de repetição
      try: # Estrutura para tratar o tipo de erro (ValueError)
         print('Escolha o tipo de transporte:')
         print('1 - Transporte Rodoviário  - R$1000.00')
         print('2 - Transporte Ferroviário - R$2000.00')
         print('3 - Transporte Hidroviário - R$2500.00')
         opcao = int(input('Digite a opção: ')) # Pergunta ao usuário a opção de transporte escolhida
         # Verifica a opção escolhida e retorna o valor do frete
         if opcao in (1, 2, 3):
            if opcao == 1:
               return 1000
            elif opcao == 2:
               return 2000
            elif opcao == 3:
               return 2500
         else:
            # Retorna para o começo do laço de repetição caso o usuário não digite uma das opções disponíveis
            print('')
            print('Escolha uma das opções 1, 2 ou 3')
            print('')
      # Tratamento do erro caso digite um valor não numérico
      except ValueError:
         print('')
         print('Só aceitamos valores numéricos. Tente novamente!')
         print('')

# Chama as funções criadas e armazena o valor que a função retornar
tipoMadeira = escolha_tipo()
qtdToras = qtd_toras()
transporte = transporte()

# Estrutura para verificar se a quantidade de toras tem desconto no valor final
if qtdToras < 100:
   desconto = 0
elif 100 <= qtdToras < 500:
   desconto = (4 / 100)
elif 500 <= qtdToras < 1000:
   desconto = (9 / 100)
elif 1000 <= qtdToras <= 2000:
   desconto = (16 / 100)

# Variável que calcula o valor final com base no tipo, quantidade e transporte escolhido 
total = ((tipoMadeira * qtdToras) * (1 - desconto)) + transporte

# Imprime no console o valor total
print(f'Total: {total:.2f}')