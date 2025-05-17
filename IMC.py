# Atividade 1 - M2 (Aula Segunda-Feira)
# Leandro Soares Lazari 1°C
# Programa Cálculo de IMC                                                    - Comentário                                 

while (True):                                                                # Looping Indefinido 1 - (Início) Pesos (Principal)
 while True:                                                                    # Looping Indefinido 2 - (Início) Float ou ValueError
        try:
           print("\n--Cálculo IMC--")                                                   # Titulo
           peso = float(input("Digite seu peso: "))  #Entrada
           altura = altura = float(input("Digite sua altura: ")) #Entrada
           if altura <= 0:
             print("Altura deve ser maior que zero.")
             continue
           break                                                               # Sai do loop 2 se a entrada for válida
                                                                
        except ValueError:
            print("Entrada inválida! Digite apenas números.")        # Looping Indefinido 2 - (Final) Float ou ValueError

 imc = peso / (altura ** 2)
            
 if imc < 18.5:                                                           # Desvio Condicional Composto Encadeado - (início)        
  print(f"\nSeu IMC é {imc:2f}, você está abaixo do peso.")   

 elif imc <= 24.9:
  print(f"\nSeu IMC é {imc:2f}, você está No peso normal.")

 elif imc <= 29.9:
  print(f"\nSeu IMC é {imc:2f}, você está com Sobrepeso.")

 elif imc <= 34.9:
  print(f"\nSeu IMC é {imc:2f}, você está com Obesidade Grau 1.")

 elif imc <= 39.9:
  print(f"\nSeu IMC é {imc:2f}, você está com Obesidade Grau 2.")

 else:
  print(f"\nSeu IMC é {imc:2f}, você está com Obesidade Grau 3.")           # Desvio Condicional Composto Encadeado - (Final)


 while True:                                                                     # Looping Indefinido 3 - (Início) Continuar
        Resposta = input("\nDeseja continuar? Digite S(im) ou N(ão): ").lower()     #Entrada

        if Resposta in ["n", "não", "nao"]:
            exit("\nEncerrando...") 

        elif Resposta in ["s", "sim"]:
            print("\nContinuando...")
            break                                                                # Sai do loop 3 se a entrada for válida
                                                                   
        else:
            print("Digite uma resposta válida.")                              # Looping Indefinido 3 - (Final) Continuar & Looping Indefinido 1 - (Final) Pesos(Principal)
                                                                             