lista_contatos = [] # Cria uma lista# Cria uma lista
id_global = 4879048 # Cria uma variável com valor inicial

def cadastrar_contato(id): # Cria uma função com o parâmetro (id)
   global id_global # Define a variável como global dentro da função
   print('-' * 46)
   print('----------- MENU CADASTRAR CONTATO -----------')
   print(f'Id do contato: {id}')
   # Solicita ao usuário os dados do contato
   nome = input('Por favor, entre com o nome do contato: ')
   atividade = input('Por favor, entre com a Atividade do contato: ')
   telefone = int(input('Por favor, entre com o telefone do contato: '))
   # Cria um dicionário com os dados do contato
   informacoes = {
      'id' : id,
      'nome' : nome,
      'atividade' : atividade,
      'telefone' : telefone
   }
   lista_contatos.append(informacoes.copy()) # Faz uma cópia do dicionário para dentro da lista
   id_global += 1 # Incrementa 1 número a mais no id_global para que cada contato tenha seu id próprio
   print('-' * 46)
   print('Contato registrado com sucesso!')

def consultar_contatos(): # Cria a função para consultar os contatos
   print('-' * 46)
   print('----------- MENU CONSULTAR CONTATOS ----------')
   print('Escolha a opção desejada: ')
   print('1 - Consultar Todos os Contatos')
   print('2 - Consultar Contato por id')
   print('3 - Consultar Contato(s) por Atividade')
   print('4 - Retornar')
   opcao = int(input('Escolha uma opção: ')) # Pergunta ao usuário qual opção ele deseja
   print('')
   try: # Estrutura para tratar o tipo de erro (ValueError)
      if opcao in (1, 2, 3, 4): # Verifica se opção escolhida é 1, 2, 3 ou 4
         if opcao == 1: # Se a opção escolhida for 1 executa o seguinte script
            for contato in lista_contatos: # Percorre a lista e mostra todos os contatos registrados
               print('-' * 46)
               print(f'id: {contato["id"]}')
               print(f'nome: {contato["nome"]}')
               print(f'atividade: {contato["atividade"]}')
               print(f'telefone: {contato["telefone"]}')
               print('-' * 46)
         elif opcao == 2: # Se a opção escolhida for 2 executa o seguinte script
            id = int(input('Digite o id do contato: ')) # Pergunta ao usuário o id do contato para buscar a informação
            print('')
            for contato in lista_contatos: # Percorre a lista em busca do id do contato solicitado
               if contato['id'] == id: # Se existir o id do contato na lista irá imprimir os dados
                  print('-' * 46)
                  print(f'id: {contato["id"]}')
                  print(f'nome: {contato["nome"]}')
                  print(f'atividade: {contato["atividade"]}')
                  print(f'telefone: {contato["telefone"]}')
                  print('-' * 46)
                  break
            else:
               print('Id não encontrado. Tente novamente!') # Se não existir o id solicitado irá retornar uma mensagem de erro
         elif opcao == 3: # Se a opção escolhida for 3 executa o seguinte script
            atividade = input('Digite a atividade do(s) contato(s): ') # Pergunta ao usuário a atividade do contato para buscar a informação
            print('')
            atividade_encontrada = False # Variável criada para saber se foi encontrado algum contato
            for contato in lista_contatos: # Percorre a lista em busca da atividade do contato solicitado
               if contato['atividade'] == atividade: # Se existir a atividade do contato na lista irá imprimir os dados
                  print('-' * 46)
                  print(f'id: {contato["id"]}')
                  print(f'nome: {contato["nome"]}')
                  print(f'atividade: {contato["atividade"]}')
                  print(f'telefone: {contato["telefone"]}')
                  print('-' * 46)
                  atividade_encontrada = True # Define a variável como 'True' pois encontrou o contato na lista
            if not atividade_encontrada: # Se não encontrar nenhum contato irá imprimir uma mensagem de contato não encontrado
               print('Atividade não encontrada. Tente novamente!')
         elif opcao == 4: # Se a opção escolhida for 4 retorna para o menu principal
            menu_principal()
      else:
         print('Escolha uma das opções 1, 2, 3 ou 4')
   except ValueError: # Tratamento do erro caso digite um valor não numérico
      print('Só aceitamos valores numéricos. Tente novamente!')

def remover_contato(): # Cria uma função para remover contato da lista
   print('-' * 46)
   print('------------ MENU REMOVER CONTATOS -----------')
   try: # Estrutura para tratar o tipo de erro (ValueError)
      id = int(input('Digite o id do contato a ser removido: '))  # Pergunta ao usuário o id do contato a ser removido
      contato_encontrado = False # Variável criada para saber se foi encontrado algum id
      for contato in lista_contatos: # Percorre a lista em busca da id do contato solicitado
         if contato['id'] == id: # Se existir o id do contato na lista irá remover os dados
            lista_contatos.remove(contato)
            print('Contato removido com sucesso!')
            contato_encontrado = True # Define a variável como 'True' pois encontrou o id na lista
      if not contato_encontrado: # Se não encontrar nenhum id irá imprimir uma mensagem de id não encontrado
         print('Id inválido. Tente novamente!')
         print('')
   except ValueError: # Tratamento do erro caso digite um valor não numérico
      print('Só aceitamos valores numéricos. Tente novamente!')

def menu_principal(): # Cria a função do menu principal
   while True: # Enquanto for verdadeira executará
      print('-' * 46)
      print('--------------- MENU PRINCIPAL ---------------')
      print('Escolha a opção desejada:')
      print('1 - Cadastrar contato')
      print('2 - Consultar contato(s)')
      print('3 - Remover contato')
      print('4 - Sair')
      opcao = int(input('Escolha uma opção: ')) # Pergunta ao usuário qual opção ele deseja
      print('')
      try: # Estrutura para tratar o tipo de erro (ValueError)
         if opcao in (1, 2, 3, 4): # Verifica se opção escolhida é 1, 2, 3 ou 4
            if opcao == 1: # Se for 1 chama a função de cadastrar contato
               cadastrar_contato(id_global)
            elif opcao == 2: # se for 2 chama a função de consultar contatos
               consultar_contatos()
            elif opcao == 3: # Se for 3 chama a função de remover contatos
               remover_contato()
            elif opcao == 4: # Se for 4 encerra o loop
               print('Encerrando programa!')
               break
         else:
            print('Por favor, escolha uma das opções 1, 2, 3 ou 4')
      except ValueError: # Tratamento do erro caso digite um valor não numérico
         print('Só aceitamos valores numéricos. Tente novamente!')

print('Bem vindo a Lista de contatos do Daniel Lisboa') # Mensagem de boas vindas
menu_principal()