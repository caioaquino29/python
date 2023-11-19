def fatorial(numero):
    if(numero==0): # essa codição que funcão recursiva deve atigir para sair 
        return 1 # quando fatorial(0) vai retorna valor 1
    else:
        return numero*fatorial(numero-1) # função recurciva ela mesma chama si mesma por exemplo o fatorial(3)  faz pilha de chamada mais ou menos assim  (3*(2*(1*(1)))) 
    
chave_loop=True
print("Digite número saber seu fatorial:")
while(chave_loop==True):
    try:
     numero=int(input())
     if(numero<0):
        print('Oops!!... Número negativo não permitido...')
     else:
        print(f'Resultado: {fatorial(numero)}')
        chave_loop=False
    except:
       print('Oops!!... Letras ou outro caractere que não seja número inteiro não fucina...')    
