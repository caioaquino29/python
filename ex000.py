def funcao_calculadora(x,y,operacao):
   if(operacao==1): 
        caculadora=x+y
        return "Resultado: ", caculadora
   elif(operacao==2):
        caculadora=x-y
        return "Resultado:", caculadora
   elif(operacao==3):
       caculadora=x*y
       return "Resultado:", caculadora
   elif(operacao==4):
       caculadora=x/y
       return "Resultado:", caculadora
   else:
       return 0
executar=True
while(executar==True):
     print("Lista de operaçõe: 1.Soma,  2.Subtração, 3.Multiplicação, 4.Divisão, 0.Sair, Digite o número para a operação correspondente")
     operacao=int(input("Digite a operação: "))
     if(operacao<0 or operacao>4):
      print("Essa operação não existe")
     elif(operacao==0):
      print('Você saiu da Caculadora...')
      executar=False
     else:
      x=int(input("Digite um número: "))
      y=int(input("Digite outro número: "))
      result=funcao_calculadora(x,y,operacao)
      print(result)    