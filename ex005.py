lista_ferramentas=['chaves de apertos', 'soquetes', 'torquímetro', 'alicate','chave de fenda','martelo','ferramenta de cortes']
chave_loop=True
for i in range(len(lista_ferramentas)):
    print(f' {i+1}..{lista_ferramentas[i]}')# primeira ação motra usuario o estoque atual
while(chave_loop==True):
  def alterar(remover_item):# função que remove as ferramentas em estoque...
    if remover_item!='':
      if(remover_item!=str(remover_item)):
        num=remover_item-1
        lista_ferramentas.pop(num)# remove pela posição no array 0,1,2... 
      else:
        lista_ferramentas.remove(remover_item)# remove pelo nome da ferramenta em estoque martelo
      
    for i in range(len(lista_ferramentas)):
          print(f' {i+1}..{lista_ferramentas[i]}')# mostra o estoque sbtraindo ferramenta selecinada
   
  def adicinar(adicinar_novo):
    if( adicinar_novo!='' ):
      lista_ferramentas.append(adicinar_novo)
    for i in range(len(lista_ferramentas)):
          print(f' {i+1}..{lista_ferramentas[i]}')# mostra o estoque com adição nova ferramenta
  try:
   modifica=int(input(' I).Quer modificar o estoque? \n1.sim: \n2.não:\n..'))# aqui vc modifica o estoque ou sai  do programa
   if(modifica<0 or modifica>2):
    raise Exception('  Oops!! número invalido... Tente novamente....') #se apão for diferente 1 ou 2 aparece essa mensagem
   elif(modifica==1): 
    remover_adicinar=int(input(" II).Quer remover um item no estoque  ou adicinar no estoque? \n 1.Remover: \n 2.Adicinar:\n.. "))
    if(remover_adicinar<0 or remover_adicinar>2):
     raise Exception('  Oops!! número invalido... Tente novamente....')
    elif(remover_adicinar==1):
      numero_nome=int(input(' III).Opções de remoção: \n 1.número: \n 2.nome: \n..'))
      if(numero_nome<0 or numero_nome>2):
        raise Exception('  Oops!! número invalido... Tente novamente....')
      elif(numero_nome==1):
        remover_item=int(input(' §-Número da ferramenta que quer remover : \n..')) #remove pela posição array
      else:
        remover_item=str(input(' §-Nome da ferramenta que quer remover : \n..'))# remove pelo item no
      alterar(remover_item)
    else:
      adicinar_novo=str(input(' §-Qual novo ferramenta sera adicinada ao estoque: \n..'))
      adicinar(adicinar_novo)
   else:
    print(' ===>Estoque em dia!!<===')
    chave_loop=False 
  except:
    print('  Oops!! número invalido... Tente novamente....')
  
