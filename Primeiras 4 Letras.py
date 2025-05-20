# Programa para mostrar os primeiros 4 Caracteres.

while (True):                                                       # Loop indefinido
 
 print("\n-- Digite e veja os primeiros 4 caracteres --")           # Título

 caracteres = int(input("Digite algo: "))                                # Entrada

 try:                                                               # "Try" Para aplicar "Except ValueError".

   if len(caracteres) > 4:                                          # "if len(variavel)"" Para verificar comprimento da variavel.
     print(f'\nOs primeiros 4 caracteres são "{caracteres[:4]}".')  # "variavel[:3]" Para pegar os 4 primeiros caracteres.
     exit("Encerrando...")                                          # "exit" Para sair.

   else:                                                            # "else" Para avisar que esta curto caso "if" seja falso.
     print("Por favor, digite pelomenos 4 caracteres.") 

 except ValueError:                                                 # "ValueError" Para caso tenha erro de valor.
   print("Ocorreu um erro.")


