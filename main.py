def entrada():
    
    A = [] 
    ''' Matriz triangular inferior (uma lista de lista)'''
    
    B = [] 
    ''' Vetor independente que armazena os coefientes independentes'''
    
    
    print("Informe a dimensão da matriz: ")
    n = input()
    try:
        n = int(n)
        if(n <= 0):
            return 1
    except ValueError:
        return 1
        
    '''Necessário a dimensão da matriz para estabelecer o numero de repetições para fazer o input tanto na matriz quando no vetor'''
    
    
    '''Percorre dois laços do mesmo tamanho da dimensão previamente informada => A = nXn'''
    '''Esse procedimento permite incluir os dados linha por linha na matriz'''
    for i in range(n):
        line = []
        for j in range(n):
            if (i >= j):
                try:
                    print("Informe o coeficiente da A{}{}: ".format(i+1, j+1))
                    line.append(float(input()))
                    if( i == j and line[j] == 0):
                        return 5
                except ValueError:
                    return 3
                if( i == 0 and j == 0 and line[0] == 0):
                    return 2
            else:
                line.append(0.0)
        A.append(line)
    
    
    '''Como o vetor independente so tem apenas uma coluna, só é necessário a utilização de um laço para preenche-lo'''
    for i in range(n):
        try:
            print('Informe o coeficiente da variável B{}: '.format(i+1))
            B.append(float(input()))
        except ValueError:
            return 4
    return (A, B)
    
def sistema_triangular(A, B):
    '''O algoritmo utilizado para a resolução do sistema triangular inferior foi o de
        substituições sucessivas. 
    '''
    X = []
    n = len(B)
    
    '''Inicializão do vetor X com zeros para evitar utilizar espaços na memória previmente utilizados'''
    for i in range (0,n):
        X.append(0)
        
    '''O primeiro termo nada mais é que a divisão do primeiro termo do vetor independete pelo primeiro termo da matriz triangular inferior'''    
    X[0] = (B[0]/A[0][0])
    
    
    
    for i in range (1, n):
        soma = 0.0
        for j in range(0, i):
            soma = soma + A[i][j]*X[j]
        X[i] = (B[i] - soma)/A[i][i]
    return X

def exibe(A, B, X):
   
    n = len(B)
    resultado = ''
    for i in range(0, n):
        for j in range(0, n):
            if( i < j):
                if( j != n-1):
                    resultado +='{:6.1f} {} '.format(0.0, '+')
                if ( j == n-1):
                    resultado +='{:6.1f} '.format(0.0)
                                
            elif( j != n-1):
                if(A[i][j] < 0):
                    resultado +='({:6.2f})*X{} {} '.format(A[i][j], j+1, '+')
                else:
                    resultado +='{:6.2f}*X{} {} '.format(A[i][j], j+1, '+')
            elif( j == n-1):
                if(A[i][j] < 0):
                    resultado +='({:6.2f})*X{} '.format(A[i][j], j+1)
                else:
                    resultado +='{:6.2f}*X{} '.format(A[i][j], j+1)
        if(i != n-1):
            resultado += '{}{}{}\n'.format('=',' ',B[i])
        if( i == n-1):
            resultado += '{}{}{}\n'.format('=',' ',B[i])
    resultado_variaveis = ""
    for i in range(0, n):
        if(i != n-1):
            resultado_variaveis += 'X{} = {:.2f}; '.format(i+1, X[i])
        if(i == n-1):
            resultado_variaveis += 'X{} = {:.2f}'.format(i+1, X[i])
    return resultado + '\n' + resultado_variaveis

def test():
    resultado = ''
    aux = entrada()

    if(aux == 1):
        resultado += '\nTEST0 FAILURE: A dimensão da matriz é um inteiro positivo não nulo \n'
    elif(aux == 2):
        resultado += '\nTEST1 FAILURE: O primeiro termo da matriz não pode ser nulo\n'
    elif(aux == 3):
        resultado +='\nTEST2 FAILURE: Os coeficientes da matriz não podem ser caracteres\n'
    elif(aux == 4):
        resultado += '\nTEST3 FAILURE: Os coeficientes do vetor independente não podem ser caracteres\n'
    elif(aux == 5):
        resultado +='\nTEST4 FAILURE: Os coeficientes da diagonal principal da matriz não podem ser nulos\n'
    else:
        A = aux[0]
        B = aux[1]
        X = sistema_triangular(A, B)
        resultado += "\n----------------------------------------------------\n"
        resultado += exibe(A, B, X)
        resultado += "\n----------------------------------------------------\n"
        resultado += '\nTEST0 SUCCESS\nTEST1 SUCCESS\nTEST2 SUCCESS\nTEST3 SUCCESS\nTEST4 SUCCESS\n'
    return resultado

print(test())
