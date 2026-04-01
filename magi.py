# Função para exibir as informações detalhadas do Sistema MAGI
def exibir_informacoes(sistema):
    sistemas_magi = {
        "Balthasar": {
            "Descrição": "Balthasar é o sistema MAGI responsável pela lógica e raciocínio. Ele representa a sabedoria e é a unidade mais calculista.",
            "Função": "Análise estratégica e raciocínio lógico. Ele é o principal responsável pelas decisões que envolvem a sobrevivência da NERV.",
            "Frase": "'A lógica deve prevalecer, a emoção é um risco.'"
        },
        "Caspar": {
            "Descrição": "Caspar é a unidade do Sistema MAGI que lida com as emoções humanas. Representa a emoção e a intuição.",
            "Função": "A análise emocional e comportamental dos seres humanos, incluindo os pilotos de EVA e membros da NERV.",
            "Frase": "'Em momentos de crise, as emoções não podem ser ignoradas.'"
        },
        "Melchior": {
            "Descrição": "Melchior é o sistema MAGI dedicado à memória humana e à preservação de dados. Ele representa o entendimento.",
            "Função": "Armazenamento e recuperação de informações cruciais para o funcionamento da NERV e do mundo em geral.",
            "Frase": "'Sem memória, a humanidade não teria futuro.'"
        }
    }

    if sistema in sistemas_magi:
        info = sistemas_magi[sistema]
        print(f"\nInformações sobre {sistema}:")
        print(f"Descrição: {info['Descrição']}")
        print(f"Função: {info['Função']}")
        print(f"Frase famosa: {info['Frase']}")
    else:
        print("Sistema não encontrado!")

# Função principal para interação com o usuário
def main():
    print("Bem-vindo ao explorador do Sistema MAGI de Evangelion!")
    print("Aqui você pode aprender sobre os 3 sistemas do MAGI que ajudam a controlar a NERV.\n")

    sistemas = ["Balthasar", "Caspar", "Melchior"]

    while True:
        print("\nSistemas disponíveis:")
        for idx, sistema in enumerate(sistemas, 1):
            print(f"{idx}. {sistema}")

        try:
            escolha = int(input("\nDigite o número do sistema (1-3) ou 0 para sair: "))
        except ValueError:
            print("Escolha inválida! Digite um número de 1 a 3.")
            continue

        if escolha == 0:
            print("Saindo do programa. Até logo!")
            break
        elif 1 <= escolha <= 3:
            exibir_informacoes(sistemas[escolha - 1])
        else:
            print("Escolha inválida! Digite um número entre 1 e 3.")

if __name__ == "__main__":
    main()