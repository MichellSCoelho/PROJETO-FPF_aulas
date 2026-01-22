DIARIA = 130
DIARIA = 130
hospedes = []
#FUNÇÕES

def cadastrarHospede():
    nome = input('Nome do hóspede: ')
    idade = int(input('Idade: '))
    documento = input('Tem documento? (sim/não): ').lower()
    dinheiro = float(input('Quanto pode gastar (R$): '))
    dias = int(input('Quantos dias pretende ficar: '))

    hospede = {
        'nome': nome,
        'idade': idade,
        'documento': documento,
        'dinheiro': dinheiro,
        'dias': dias,
        'hospedado': False
    }

    hospedes.append(hospede)
    print("\n Hóspede cadastrado com sucesso!\n")


def listarHospedes():
    if len(hospedes) == 0:
        print("\n Nenhum hóspede cadastrado.\n")
        return

    print("\n LISTA DE HÓSPEDES\n")
    for i, h in enumerate(hospedes, start=1):
        print(f"{i} - Nome: {h['nome']}")
        print(f"   Idade: {h['idade']}")
        print(f"   Documento: {h['documento']}")
        print(f"   Dias: {h['dias']}")
        print(f"   Hospedado: {'Sim' if h['hospedado'] else 'Não'}")
        print("-" * 30)


def verificarElegibilidade():
    listarHospedes()

    if len(hospedes) == 0:
        return

    indice = int(input("\nSelecione o número do hóspede: ")) - 1

    if indice < 0 or indice >= len(hospedes):
        print("\n Hóspede inválido!\n")
        return

    hospede = hospedes[indice]
    custo_total = hospede["dias"] * DIARIA

    print(f"\n Custo total da hospedagem: R$ {custo_total:.2f}")

    if hospede["idade"] < 18:
        print(" Não aprovado!(menor de idade).")
    elif hospede["documento"] != "sim":
        print(" Não aprovado!(indigente).")
    elif hospede["dinheiro"] < custo_total:
        print(" Liso (Você é pobre).")
    else:
        hospede["hospedado"] = True
        print(" Check-in realizado com sucesso!")


def deletarHospede():
    listarHospedes()

    if len(hospedes) == 0:
        return

    indice = int(input('\nDigite o número do hóspede a deletar:')) - 1

    if 0 <= indice < len(hospedes):
        hospedes.pop(indice)
        print('\n Hóspede removido com sucesso!\n')
    else:
        print('\n Hóspede inválido!\n')


# ---------- PROGRAMA PRINCIPAL ----------

while True:
    print('===== HOTEL GRUPO 04 =====')
    print('1 - Cadastrar novo hóspede')
    print('2 - Verificar elegibilidade / Check-in')
    print('3 - Deletar hóspede')
    print('4 - Listar hóspedes')
    print('5 - Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == "1":
        cadastrarHospede()
    elif opcao == "2":
        verificarElegibilidade()
    elif opcao == "3":
        deletarHospede()
    elif opcao == "4":
        listarHospedes()
    elif opcao == "5":
        print("\n Bye!...")
        break