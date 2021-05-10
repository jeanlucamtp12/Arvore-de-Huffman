class No:
    def __init__ (self):
        self.frequencia = None
        self.simbolo = ""
        self.proximo = None
        self.visitado = False
        self.codificado = None
   
class Arvore:
    def __init__ (self):
        self.ptr = None  
        self.arvoreCodificada = ""
        self.arvoreDecodificada = ""
        
class NoArvore:
    def __init__ (self):
        self.frequencia = None
        self.simbolo = None
        self.esquerda = None
        self.direita = None
        self.proximo = None
        self.visitado = False
      
class listaSimples:
    def __init__(self):
        self.primeiro = None
        self.anterior = None
        
'''Procura determinado simbolo na arvore de huffman para encontrar seu valor compprimido'''
def buscaCodificacao(self, simbolo):
    
    aux = self.ptr
    if (aux == None):
        return
    else:
          while (aux.simbolo == None): 

            if (aux.esquerda != None and (aux.esquerda).visitado != True):           
                aux = aux.esquerda   
              
                   
            elif (aux.direita != None and (aux.direita).visitado != True):             
                aux = aux.direita  
                
                
            elif((aux.esquerda != None and (aux.esquerda).visitado == True) and (aux.direita != None and (aux.direita).visitado == True)) :               
                break
         
    aux.visitado = True

    if (aux.simbolo == simbolo):
        x = aux.codificado         
        self.arvoreCodificada = self.arvoreCodificada+str(x)
         
    if((self.ptr).visitado == True):
        return 
    
    buscaCodificacao(self, simbolo)

'''Faz todos os nos da arvore receberem false na variavel visitado'''
def zerarVisitas(self):
    
    aux = self.ptr
    if (aux == None):
        return
    else:
          while (aux.simbolo == None): 
           
            if (aux.esquerda != None and (aux.esquerda).visitado == True):
                aux = aux.esquerda         
                
            elif (aux.direita != None and (aux.direita).visitado == True):
                aux = aux.direita 
                      
            elif((aux.esquerda != None and (aux.esquerda).visitado != True) and (aux.direita != None and (aux.direita).visitado != True)) :                         
                break      
        
    aux.visitado = False
    if((self.ptr).visitado == False and (self.ptr).esquerda.visitado == False and (self.ptr).direita.visitado == False):
        return
    
    zerarVisitas(self)
    
'''Percorre a arvore pelo caminho passado para encontrar cada caractere e formar o texto decodificado'''    
def decodificacao(self, texto):
   
    aux = self.ptr
    if (aux == None):
        return
    else:
               
          j = len(texto)        
          for i in range (j):            
              
              if (texto[i] == '0' and aux.simbolo == None):
                  aux = aux.esquerda
               
              elif(texto[i] == '1' and aux.simbolo == None):
                   aux= aux.direita 
                  
              if(aux.simbolo != None):
                  x =  aux.simbolo                   
                  self.arvoreDecodificada = self.arvoreDecodificada+str(x)  
                  aux = self.ptr
         
'''Busca a codificaçao dos simbolos e os salva em um arquivo'''                      
def codificacao(self, lista, ocorrencias, vocab, valores):
   
    cod = ""
    num = ""
    
    for item in (lista):     
        zerarVisitas(self)  
        buscaCodificacao(self, item)       
      
    t = self.arvoreCodificada
    linha1 = (ocorrencias.items())
    linha1 = str(linha1)
    
    j = len(vocab)
    for i in range(j):     
        letra =  vocab[i]
        numero = valores[i]
        if(letra == '\n'):
            cod = cod+str('π')
            num = num+str(numero) + '-'
            continueç

        cod = cod+str(letra)
        num = num+str(numero) + '-'

    '''Informe o caminho para salvar o arquivo .dvz'''
    with open('/home/jean/Desktop/novo_arquivo.dvz', 'wt') as arquivo:
        arquivo.write(cod)
        arquivo.write(num)
        arquivo.write('\n')
    arquivo.close()
    
    vamos = compactar(t)
    with open('/home/jean/Desktop/novo_arquivo.dvz', 'a') as arquivo:
         arquivo.write(vamos) 
    arquivo.close()
 
'''Metodos para transformar texto em bit e vice versa'''      
def compactar(texto):
    bytes = [chr(int(texto[i:i+8], 2)) for i in range(0,len(texto),8)]
    return "".join(bytes)

def descompactar(texto):
    bytes = [bin(ord(byte))[2:] for byte in texto]
    for i in range(0, len(bytes) - 1):
        bytes[i] = bytes[i].zfill(8)
    textoDescompactado = "".join(bytes)
    return textoDescompactado

'''Faz a inserçao de elementos e os organiza em ordem crecscente em uma lista'''            
def inserirLista(self, no):
  
       aux = self.primeiro
       anterior = None
       while (aux != None):  
                                      
           if(aux == None):
              break          
           if(no.frequencia < aux.frequencia):
              break
           anterior = aux
           aux = aux.proximo   
           self.anterior = anterior
       
       if(self.anterior == None):      
            if(self.primeiro == None):
                self.primeiro = no            
                return          
            no.proximo = self.primeiro
            self.primeiro = no
            
       elif(aux == None):        
            (self.anterior).proximo = no

       else:           
            (self.anterior).proximo = no
            no.proximo = aux
    
'''A partir de uma lista ordenada cria a arvare de huffman'''           
def criarArvoreHuffman(self, arv):
 
    if(self.primeiro == None):
        print("lista vazia")
        return
 
    else:
        aux = (self.primeiro).proximo
        no = NoArvore()
        
        valorNovoNo = (self.primeiro).frequencia + aux.frequencia
        
        no.frequencia = valorNovoNo
        no.esquerda = self.primeiro        
        self.primeiro =  None
        no.direita = aux
        self.primeiro = aux.proximo    
        aux.proximo = None
        inserirLista(self, no)
        
        if((self.primeiro) == None or (self.primeiro).proximo == None):
            arv.ptr = no
            codificarSimbolos(arv)          
            return 
        criarArvoreHuffman(self, arv)
  
'''Cada simbolo da arvore criada recebe seu valor codificado correspondente'''                
def codificarSimbolos(self):
    
    aux = self.ptr
    var = ""
    if (aux == None):
        return
    else:
        
        while (aux.simbolo == None):
           
            if (aux.esquerda != None and (aux.esquerda).visitado != True):
                n = 0
                var = var+str(n)
                aux = aux.esquerda          
               
            elif (aux.direita != None and (aux.direita).visitado != True):
                n = 1
                var = var+str(n)
                aux = aux.direita   
            elif((aux.esquerda != None and (aux.esquerda).visitado == True) and (aux.direita != None and (aux.direita).visitado == True)) :               
                break
                 
        aux.visitado = True
        if((self.ptr).visitado == True):
          return
      
        int(var)
        if(aux.simbolo != None):
             aux.codificado = var
            
        codificarSimbolos(self)      
        
'''main'''  '''Necessario informar o arquivo a ser aberto na linha 248 e 292'''  '''Informar caminho para salvar o arquivo linhas 133 e 135 '''
def principal():
    
    with open('/home/jean/Desktop/PA_arquivos/compressao//Compressor_5.txt') as arquivo:
        linhas = arquivo.read()
    
    lista = linhas
    ocorrencias = {}
    arv = Arvore()
    
    for numero in lista:
        
        if numero in ocorrencias: 
            ocorrencias[numero] += 1
        else: 
            ocorrencias[numero] = 1
            
    valores = list(ocorrencias.values())
    vocab = list(ocorrencias.keys())
    
    n = len(vocab)
    fil = listaSimples()
    
    i = 0
    while (vocab):       
        no = No()  
        no.simbolo = vocab[i]
        no.frequencia = valores[i]  
        inserirLista(fil, no)     
        i=i+1
        
        if i == n:
            break
    fil.anterior = None
    criarArvoreHuffman(fil, arv)
        
    opcao = eval(input("A arvore de Huffman foi criada/ Digite 1 para comprimir o arquivo\n"))
    if(opcao == 1):
      codificacao(arv, lista,ocorrencias, vocab, valores)
      
    print("Comprimido com sucesso/Novo arquivo .dvz salvo\n")
    opcao = eval(input("Caso deseje descompactar o arquivo digite 1\n"))
    if(opcao == 1):
     
        arv.ptr = None       
        letras = []
        numeros = []    
        with open( "/home/jean/Desktop/novo_arquivo.dvz", "r") as arq:
             linha1 = arq.readline()
             segundaLinha = arq.read()          
       
        retorno = descompactar(str(segundaLinha)) 
        segundaLinha = retorno
        
        li = str(linha1)
       
        for i in list(li):      
             try:
                 val = int(i)
                 break
             except ValueError: 
                 if(i == 'π'):                  
                     letras.append('\n') 
                     li = li.replace(i,"") 
                     continue
                 letras.append(i)
                 li = li.replace(i,"")
            
        conteudo = ""
        for i in li:    
            
            if(i != '-'):           
                conteudo = conteudo+str(i)
            else:
                numeros.append(conteudo)
                conteudo = ""
                
        numeros = [int(val) for val in numeros]
    
        n = len(letras)
        f = listaSimples()
       
        i = 0
        while (letras):       
            no = No()  
            no.simbolo = letras[i]
            no.frequencia = numeros[i]  
            inserirLista(f, no)     
            i=i+1
            
            if i == n:
                break
        f.anterior = None
       
        criarArvoreHuffman(f, arv)
        decodificacao(arv, segundaLinha)  
        print(f"A decodificacao = {arv.arvoreDecodificada}")  
        
principal()


















        
    
