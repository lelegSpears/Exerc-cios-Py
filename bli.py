#Atividade 2 - M2   Software básico
#Leandro Soares Lazari 1°C - E.S.
#Pedro Rafael da Silva 1°B - S.I.

import os  # Biblioteca para comandos do sistema (limpar tela)

# == Dados iniciais ==
mensal_SE = 0  # mensalidade ES
mensal_CC = 0  # mensalidade CC
Period_M_ES = Period_N_ES = Period_M_CC = Period_N_CC = 0  # períodos (não usados ainda)

# Professores pré-cadastrados
Professores = {
    101: {"nome": "João Silva", "senha": "senha123", "horario_aula": "19:00 - 22:00",
          "dias_semana": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]},
    102: {"nome": "Maria Oliveira", "senha": "senha456", "horario_aula": "10:00 - 13:00",
          "dias_semana": ["Segunda", "Terça", "Quinta", "Sexta"]}
}

Alunos = {}  # dicionário para cadastro dinâmico de alunos
funcionarios = {}  # não usado, mas mantido conforme original

# == Utilitários ==
def Limpador():
    os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela conforme o SO

def pausa():
    pausa = input('Digite qualquer coisa para continuar:')

# == Exibição de menus e telas ==
def exibir_menu_principal():
    print("\n\t\033[36m-- Universidade de Pahiro --\033[0m\n")
    print("Menus:")
    print("1 - Portais")
    print("2 - Cursos")
    print("3 - Suporte")
    print("0 - Sair")

def exibir_menu_login():
    print("\n\033[32mOpções de Login:\033[0m\n")
    print("1 - Portal do Aluno")
    print("2 - Portal do Docente")
    print("3 - Gestão de pessoas")
    print("4 - Voltar")
    print("0 - Sair")

def exibir_menu_professor():
    print("\n\033[34m-- Menu do Professor --\033[0m")
    print("1 - Lançar falta para um aluno")
    print("2 - Ver lista de alunos")
    print("0 - Sair")

def exibir_menu_rh():
    print("\nMenu RH:")
    print("1 - Cadastrar ou editar usuários")
    print("0 - Voltar")

def exibir_menu_cursos():
    print("\n\t\033[36m-- Cursos --\033[0m\n")
    print("1 - Engenharia de Software")
    print("2 - Ciência da Computação")
    print("3 - Voltar")
    print("0 - Sair")

def exibir_info_curso_ES():
    print("\n\033[36m== Engenharia de Software ==\033[0m\n")
    print("Mensalidade: R$ 900")
    print("Períodos: Matutino 10:00 - 13:00 | Noturno 19:00 - 22:00")
    print("1 - Inscrição")
    print("2 - Voltar")
    print("0 - Sair")

def exibir_info_curso_CC():
    print("\n\033[36m== Ciência da Computação ==\033[0m\n")
    print("Mensalidade: R$ 960")
    print("Períodos: Matutino 10:00 - 13:00 | Noturno 19:00 - 22:00")
    print("1 - Inscrição")
    print("2 - Voltar")
    print("0 - Sair")

def exibir_info_suporte():
    print("\n\t\033[36m-- Contato do Suporte --\033[0m\n")
    print("Atendimento integrado: 11 9XXX-XXXX")
    print("Financeiro: 11 9XXX-XXXX")
    print("Secretaria: 11 9XXX-XXXX")
    print("0 - Sair")
    pausa()

def exibir_dados_aluno(rgm, aluno):
    print("\n Login bem‑sucedido!")
    print(f"🔍 Dados do Aluno RGM {rgm}:")
    print(f"Nome: {aluno['nome']}")
    print(f"Curso: {aluno.get('curso', 'Não informado')}")
    print(f"Mensalidade: {aluno.get('mensalidade', 'Não informada')}")
    print(f"Horário de Aula: {aluno.get('horario_aula', 'Não informado')}")
    print(f"Dias da Semana: {', '.join(aluno.get('dias_semana', []))}")

def exibir_dados_professor(id_prof, prof):
    print("\n Login bem‑sucedido!")
    print(f"🔍 Dados do Professor ID {id_prof}:")
    print(f"Nome: {prof['nome']}")
    print(f"Curso que leciona: {prof.get('curso', 'Não informado')}")
    print(f"Salário: {prof.get('salario', 'Não informado')}")
    print(f"Horário de Aula: {prof.get('horario_aula', 'Não informano')}")
    print(f"Dias da Semana: {', '.join(prof.get('dias_semana', []))}")

def exibir_lista_alunos():
    print("\n\033[33m-- Alunos Cadastrados --\033[0m")
    for rgm, aluno in Alunos.items():
        faltas = aluno.get("faltas", 0)
        curso = aluno.get("curso", "N/I")
        print(f"RGM: {rgm} | Nome: {aluno['nome']} | Curso: {curso} | Faltas: {faltas}")

# == Lógica dos menus e funcionalidades ==
def Menu_princ(): 
    selecao_menu()  # entra no loop de seleção

def selecao_menu():
    while True:
        exibir_menu_principal()  # Mostra o menu a cada ciclo
        try:
            opcao = int(input("Escolha uma Opção: "))  # lê a opção
            if opcao == 1:
                menu_login()
            elif opcao == 2:
                menu_cursos()
            elif opcao == 3:
                exibir_info_suporte()
            elif opcao == 0:
                exit("\nEncerrando...")  # encerra
            else:
                print("Digite apenas 1, 2, 3 ou 0.")  # inválido
        except ValueError:
            print("Opção inválida.")  # erro entrada

def menu_cursos():
    while True:
        exibir_menu_cursos()  # Mostra as opções de cursos
        try:
            escolha = int(input("Escolha uma opção: "))  # Lê a escolha do usuário
            if escolha == 1:
                info_curso_ES()  # Vai para o menu do curso de ES
            elif escolha == 2:
                info_curso_CC()  # Vai para o menu do curso de CC
            elif escolha == 3:
                exibir_menu_principal
                break  # Volta ao menu principal
            elif escolha == 0:
                exit("Encerrando...")  # Encerra o programa
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")

def info_curso_ES():
    while True:
        exibir_info_curso_ES()  # Exibe informações do curso de ES
        try:
            escolha = int(input("Escolha uma opção: "))  # Lê escolha
            if escolha == 1:
                print("📝 Iniciando inscrição para Engenharia de Software...\n")
                # Aqui você pode chamar uma função de inscrição
            elif escolha == 2:
                break  # Volta ao menu de cursos
            elif escolha == 0:
                exit("Encerrando...")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")

def info_curso_CC():
    while True:
        exibir_info_curso_CC()  # Exibe informações do curso de CC
        try:
            escolha = int(input("Escolha uma opção: "))
            if escolha == 1:
                print("📝 Iniciando inscrição para Ciência da Computação...\n")
                # Aqui também pode ir uma função de inscrição
            elif escolha == 2:
                break  # Volta ao menu de cursos
            elif escolha == 0:
                exit("Encerrando...")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")

def menu_login():
    exibir_menu_login()
    while True:
        try:
            opcao = int(input("Escolha uma Opção: "))
            if opcao == 1:
                aluno_login()
                break
            elif opcao == 2:
                professor_login()
                break
            elif opcao == 3:
                RH()
                break
            elif opcao == 4:
                selecao_menu()
                break
            elif opcao == 0:
                exit("Encerrando...")
            else:
                print("Digite apenas 1 a 4 ou 0.")
        except ValueError:
            print("Opção inválida.")

def aluno_login():
    print("\n\033[42m- Login do Aluno -\033[0m")
    try:
        RGM = int(input("RGM: "))  # RGM
        senha = input("Senha: ")   # senha
        aluno = Alunos.get(RGM)
        if aluno and aluno["senha"] == senha: #verificação
            exibir_dados_aluno(RGM, aluno)
        else:
            print(" RGM ou senha incorretos.")
    except ValueError:
        print(" Entrada inválida. RGM deve ser numérico.")

def professor_login():
    print("\n\033[42m- Login do Professor -\033[0m")
    try:
        id_prof = int(input("ID: "))
        senha = input("Senha: ")
        prof = Professores.get(id_prof)
        if prof and prof["senha"] == senha:
            exibir_dados_professor(id_prof, prof)
            while True:
                exibir_menu_professor()
                opcao = input("Escolha uma opção: ")
                if opcao == "1":
                    if not Alunos:
                        print("Nenhum aluno cadastrado.")
                        continue
                    try:
                        rgm = int(input("Digite o RGM do aluno: "))
                        aluno = Alunos.get(rgm)
                        if aluno:
                            aluno["faltas"] = aluno.get("faltas", 0) + 1
                            print(f" Falta lançada para {aluno['nome']}. Total: {aluno['faltas']}")
                        else:
                            print(" Aluno não encontrado.")
                    except ValueError:
                        print("RGM inválido.")
                elif opcao == "2":
                    if Alunos:
                        exibir_lista_alunos()
                    else:
                        print("Nenhum aluno cadastrado.")
                elif opcao == "0":
                    print("Saindo do portal do professor.")
                    break
                else:
                    print("Opção inválida.")
        else:
            print(" ID ou senha incorretos.")
    except ValueError:
        print(" Entrada inválida. ID deve ser numérico.")

def RH():
    print("\n\033[91m-Login RH-\033[0m")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == "RH" and senha == "1234":
        print("✅ Login efetuado com sucesso!")
        while True:
            exibir_menu_rh()
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                cadastrar_ou_editar()
            elif opcao == "0":
                print("Voltando ao menu principal...\n")
                break
            else:
                print(" Opção inválida.")
    else:
        print(" Acesso negado.")

def cadastrar_ou_editar():
    while True:
        print("\nVocê deseja cadastrar ou editar dados de:")
        print("1 - Aluno")
        print("2 - Professor")
        print("0 - Voltar")
        try:
            escolha = int(input("Escolha uma opção: "))
            if escolha == 1:
                registro, tipo, id_label = Alunos, "Aluno", "RGM"
            elif escolha == 2:
                registro, tipo, id_label = Professores, "Professor", "ID"
            elif escolha == 0:
                print("Retornando ao menu RH...\n")
                break
            else:
                print(" Opção inválida.")
                continue
            identificador = int(input(f"Digite o {id_label} do {tipo} (ou 0 para voltar): "))
            if identificador == 0:
                print("Voltando...\n")
                continue
            if identificador in registro:
                opc = input(f"{tipo} com {id_label} {identificador} já existe. Editar? (s/n): ").lower()
                if opc != 's':
                    continue
            nome = input("Nome: ")
            senha = input("Senha: ")
            horario = input("Horário de aula (ex: 08:00 - 12:00): ")
            dias = input("Dias da semana (ex: Segunda,Terça): ").split(',')
            curso = input("Curso (ex: Engenharia de Software): ")
            if tipo == "Aluno":
                mensalidade = input("Mensalidade (ex: 850.00): ")
                registro[identificador] = {
                    "nome": nome, "senha": senha, "horario_aula": horario,
                    "dias_semana": [d.strip().capitalize() for d in dias],
                    "curso": curso, "mensalidade": f"R$ {mensalidade}", "faltas": 0
                }
            else:
                salario = input("Salário (ex: 3500.00): ")
                registro[identificador] = {
                    "nome": nome, "senha": senha, "horario_aula": horario,
                    "dias_semana": [d.strip().capitalize() for d in dias],
                    "curso": curso, "salario": f"R$ {salario}"
                }
            print(f"\n✅ {tipo} com {id_label} {identificador} salvo com sucesso!\n")
        except ValueError:
            print(" Entrada inválida. Use apenas números onde solicitado.")

Menu_princ()