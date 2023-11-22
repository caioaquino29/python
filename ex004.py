while True:
    try:
        x=int(input('Digite um número: '))
        break
    except ValueError:
        print('Oops! Esse número não é valido. Tente novamente... ')

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')        
    
try:
    raise Exception('spam','eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)


    x,y=inst.args
    print('x=',x)
    print('y=',y)    



def soma_recur(lista3):
  if(lista3==0):
    return 0
  else:
    return lista3[0] + soma_recur(lista3.pop())

soma_recur([2,4,6])