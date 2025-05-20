# Programa para apenas aceitar nome com letra A

while (True):                                                       # Loop indefinido
 
 print('\n-- Digite um nome com "A" de primeira letra --')          # Título

 try:                                                               # "Try" Para aplicar "Except ValueError".
 
  caracteres = str(input("Digite algo: "))                          # Entrada

  if (caracteres[0].upper() == "A"):                                # "if len(variavel)"" Para verificar comprimento da variavel.
     print(f'\nO nome é "{caracteres}".')                           # "variavel[:3]" Para pegar os 4 primeiros caracteres (0 conta como o primeiro caracter).
     exit("Encerrando...")                                          # "exit" Para sair.

  else:                                                             # "else" Para avisar que esta curto caso "if" seja falso.
     print('Por favor, o primeiro caracter deve ser "A".') 

 except ValueError:                                                 # "ValueError" Para caso tenha erro de valor.
   print("Escreva um nome.")