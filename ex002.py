chave=True
while(chave==True):
  print("Coloque seus dados para caucular sua idade...") # entrada do usuario
  try: # exceção isso me garante que codigo não vai ´para se usuario digita numero no campo ano
    nome=str(input("Digitar seu nome completo:"))
    ano=int(input ("Digote se ano nascimento:"))
    if(ano >=1922 and ano<= 2023):
      anoNasc=2023-ano
      print(" "+nome)
      print(" Sua idade "+str(anoNasc))
    elif(ano==0 or nome ==0):
      print(" Acaba de sair do app...")
      chave=False
    elif(ano<1922 and ano>2023):
      print(" "+nome)
      print(" Facha etária não computada... tente outro")
  except Exception as e:
   print(" Nao digitar lestras nesse campo...")
   print(e)# para saber qual foi erro digitado pelo usuario