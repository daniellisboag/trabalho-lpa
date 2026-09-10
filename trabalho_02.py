# Mensagem de boas-vindas
print('------ Bem-vindo a pizzaria do Daniel Lisboa Gonçalves ------')
print('------------------------- Cardápio --------------------------')
print('-' * 61)
print('---|  Tamanho  |  Pizza salgada(PS)  |  Pizza doce(PD)   |---')
print('---|     P     |       R$30.00       |      R$34.00      |---')
print('---|     M     |       R$45.00       |      R$48.00      |---')
print('---|     G     |       R$60.00       |      R$66.00      |---')
print('-' * 61)

# Inicia acumulador
total = 0

# Inicia a estrutura de repetição
while True:
   sabor = input('Entre com o sabor desejado (PS/PD): ') # Pergunta ao usuário o sabor desejado
   if sabor in ('PS', 'PD'):
      tamanho = input('Entre com o tamanho desejado (P/M/G): ') # Pergunta ao usuário o tamanho desejado
      if tamanho in ('P', 'M', 'G'): # Verifica tamanho pedido
         if sabor == 'PD': # Verifica sabor pedido
            if tamanho == 'P':
               total += 34
               print('Você pediu uma Pizza Doce no tamanho P: R$34,00')
               print('')
            elif tamanho == 'M':
               total += 48
               print('Você pediu uma Pizza Doce no tamanho M: R$48,00')
               print('')
            elif tamanho == 'G':
               total += 66
               print('Você pediu uma Pizza Doce no tamanho G: R$66,00')
               print('')
         elif sabor == 'PS':
            if tamanho == 'P':
               total += 30
               print('Você pediu uma Pizza Salgada no tamanho P: R$30,00')
               print('')
            elif tamanho == 'M':
               total += 45
               print('Você pediu uma Pizza Salgada no tamanho M: R$45,00')
               print('')
            elif tamanho == 'G':
               total += 60
               print('Você pediu uma Pizza Salgada no tamanho G: R$60,00')
               print('')
         repetir = input('Deseja mais alguma coisa? (S/N): ') # Pergunta ao usuário se ele deseja mais algo
         if repetir == 'S':
            # Pula o restante do código e volta para o início do laço de repetição
            continue
         if repetir == 'N':
            # Finaliza o pedido e sai do laço de repetição
            print('')
            print(f'O valor total a ser pago: R${total:.2f}')
            break
      else:
         print('Tamanho inválido. Tente novamente') # Mensagem de erro caso o usuário digite tamanho errado
         print('')
   else:
      print('Sabor inválido. Tente novamente') # Mensagem de erro caso o usuário digite sabor errado
      print('')