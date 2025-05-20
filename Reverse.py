# Programa que deixa palavra ou texto de tras para frente

while (True):
 print('\n-- Digite uma frase para invertela --')                                # Título

 while True:
     try:                                                                        # "Try" Para aplicar "Except ValueError".
     
      palavra = str(input("Escreva uma palavra/texto: "))                        # Entrada
  
      if not palavra.isalpha():
       print('\nPor favor, digite apenas letras.')
      else:
       print(f'\nAo contrario se escreve "{palavra[::-1]}"')                     # "variavel[::-1]"" Inverte a variavel.
       break                                                                     # Sai do loop se a entrada for válida.

     except ValueError:
       print("erro")


 while True:                                                                     # Looping Indefinido - (Início) Continuar
        Resposta = input("Deseja continuar? Digite S(im) ou N(ão): ").lower()    #Entrada

        if Resposta in ["n", "não", "nao"]:
            exit("\nEncerrando...") 

        elif Resposta in ["s", "sim"]:
            print("\nContinuando...")
            break                                                                # Sai do loop se a entrada for válida.
                                                                   
        else:
            print("Digite uma resposta válida.")                                 # Looping Indefinido - (Final) Continuar & Looping Indefinido 1 - (Final) Pesos(Principal)