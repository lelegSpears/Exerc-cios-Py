

def pegar_dados():
    while True:
        try:
            print("\n-- Cálculo IMC --")
            peso = float(input("Digite seu peso: "))
            altura = float(input("Digite sua altura: "))

            if altura <= 0:
                print("Altura deve ser maior que zero.")
                continue

            return peso, altura

        except ValueError:
            print("Entrada inválida! Digite apenas números.")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    print(f"\nSeu IMC é {imc:.2f}", end=", ")
    if imc < 18.5:
        print("você está abaixo do peso.")
    elif imc <= 24.9:
        print("você está no peso normal.")
    elif imc <= 29.9:
        print("você está com Sobrepeso.")
    elif imc <= 34.9:
        print("você está com Obesidade Grau 1.")
    elif imc <= 39.9:
        print("você está com Obesidade Grau 2.")
    else:
        print("você está com Obesidade Grau 3.")

def deseja_continuar():
    while True:
        resposta = input("\nDeseja continuar? Digite S(im) ou N(ão): ").lower()
        if resposta in ["n", "não", "nao"]:
            print("Encerrando...")
            return False
        elif resposta in ["s", "sim"]:
            return True
        else:
            print("Digite uma resposta válida (S ou N).")

# --- Programa principal ---
while True:
    peso, altura = pegar_dados()
    imc = calcular_imc(peso, altura)
    classificar_imc(imc)

    if not deseja_continuar():
        break
