chave=bool(True)

while(chave==True):
 def tabuada(n):
  if(n<0 or n>100):
    raise Exception('Não use numero negativo ou valor muito alto ...') #é limitador de valor para não usar valor alto de mais nem negativo pois foge da aplicação...
  else:
   for i in range(11):
    res=n*i
    print(n,"x",i,'=',res) #se usa return não fucio 
 
 try:
  n=int(input("Digite numero para sua tabuada:"))
  tabuada(n)
 except Exception as erro: # Usando uma exceção par detectar quando usuario preeche com letra campo que deveria conter numero
    print(erro)
    print('ERRo!!!!!')
     # chama minha função assim consigo colocar qual que numero de tabuada... 
    
 


