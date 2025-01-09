# Programa de Cadastro de Pessoa e Criação de Conta de Acesso (Reescrito)

def cadastrar_usuario():
    print("\n=== Cadastro de Usuário ===")
    usuario = {
        "nome": input("Nome: "),
        "cpf": input("CPF: "),
        "idade": int(input("Idade: ")),
        "endereco": input("Endereço: "),
        "telefone": input("Telefone: ")
    }
    print("\nUsuário cadastrado com sucesso!")
    return usuario


def criar_conta_acesso():
    print("\n=== Criação de Conta de Acesso ===")
    while True:
        login = input("Login: ")
        senha = input("Senha: ")
        if senha == input("Confirme a senha: "):
            print("Conta de acesso criada com sucesso!")
            return {"login": login, "senha": senha}
        print("As senhas não coincidem. Tente novamente.")


def exibir_dados(usuario, conta):
    print("\n=== Dados do Usuário ===")
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")

    print("\n=== Conta de Acesso ===")
    print(f"Login: {conta['login']}")


def main():
    usuario = cadastrar_usuario()
    conta = criar_conta_acesso()
    exibir_dados(usuario, conta)


if __name__ == "__main__":
    main()
