
  print('====================================')
  print('     SISTEMA DE FUNCIONÁRIOS        ')
  print('====================================')

  # 1. Agora usamos uma LISTA para armazenar vários dicionários
  funcionarios = []

  def exibir_menu():
      print('\n' + '='*20)
      print(' ======== MENU ========== ')
      print('='*20)
      print('1 - Cadastrar Funcionário')
      print('2 - Listar Todos')
      print('3 - Alterar Dados')
      print('4 - Excluir Funcionário')
      print('5 - Sair')
      print('='*20)

  while True:
      exibir_menu()
      opcao = input('Escolha uma opção: ')

      if opcao == '1':
          # Cadastro: cria um dicionário e adiciona na lista
          print("\n--- Cadastro de Novo Funcionário ---")
          nome = input('Digite o nome: ')
          idade = int(input('Digite a idade: '))
          cargo = input('Digite o cargo: ')
          salario = float(input('Digite o salário: '))

          novo_funcionario = {
              'nome': nome,
              'idade': idade,
              'cargo': cargo,
              'salario': salario,
          }
          funcionarios.append(novo_funcionario)
          print('Funcionário cadastrado com sucesso!')

      elif opcao == '2':
          # Listagem: percorre a lista de funcionários
          print('\n==== LISTA DE FUNCIONÁRIOS =======')
          if not funcionarios:
              print('Nenhum funcionário cadastrado.')
          else:
              for i, func in enumerate(funcionarios):
                  print(f"ID: {i} | Nome: {func['nome']} | Cargo: {func['cargo']} | Salário: R${func['salario']:.2f}")
          print('=================================')

      elif opcao == '3':
          # Alteração: busca pelo ID (índice da lista)
          if not funcionarios:
              print('Não há funcionários para alterar.')
              continue

          # Primeiro mostramos a lista para o usuário saber qual ID escolher
          for i, func in enumerate(funcionarios):
              print(f"{i} - {func['nome']}")

          try:
              indice = int(input('\nDigite o ID do funcionário que deseja alterar: '))

              print('1 - Alterar Cargo')
              print('2 - Alterar Salário')
              sub_opcao = input('O que deseja alterar? ')

              if sub_opcao == '1':
                  novo_cargo = input('Digite o novo cargo: ')
                  funcionarios[indice]['cargo'] = novo_cargo
                  print('Cargo atualizado!')
              elif sub_opcao == '2':
                  novo_salario = float(input('Digite o novo salário: '))
                  funcionarios[indice]['salario'] = novo_salario
                  print('Salário atualizado!')
              else:
                  print('Opção inválida.')
          except (ValueError, IndexError):
              print('Erro: ID inválido ou valor incorreto.')

      elif opcao == '4':
          # Exclusão: remove o item da lista via índice
          if not funcionarios:
              print('Não há funcionários para excluir.')
              continue

          for i, func in enumerate(funcionarios):
              print(f"{i} - {func['nome']}")

          try:
              indice = int(input('\nDigite o ID do funcionário que deseja excluir: '))
              removido = funcionarios.pop(indice)
              print(f"Funcionário {removido['nome']} removido com sucesso!")
          except (ValueError, IndexError):
              print('Erro: ID inválido.')

      elif opcao == '5':
          print('Sistema encerrado. Até logo!')
          break

      else:
          print('Opção inválida! Tente novamente.')
