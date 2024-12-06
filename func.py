prod = [{'cod': 123, 'nome': 'banana', 'preco': 2.25, 'quant': 8},
        {'cod': 124, 'nome': 'pera', 'preco': 2.8, 'quant': 6},
        {'cod': 125, 'nome': 'maça', 'preco': 3.2, 'quant': 12},
        {'cod': 126, 'nome': 'uva', 'preco': 45.5, 'quant': 28},
        {'cod': 127, 'nome': 'bacate', 'preco': 7, 'quant': 9}]

carrinho = []

def AdicionaProd(cod, nome, preco, quant):
    prod.append({'cod':cod, 'nome':nome, 'preco':preco, 'quant':quant})

def RemoveProd(cod):
    posicao = AchaProduto(cod)
    del(prod[posicao])
    
def ListaProd():
    for i in range(len(prod)):
        print(prod[i])
def ListarCarrinho():
    print('Carrinho: ')
    for i in range(len(carrinho)):
        print(carrinho[i])
        
def AdicionarCarrinho(cod):
    posicao = AchaProduto(cod)
    carrinho.append(prod[posicao])
    print('Produto adicionado no carrinho com sucesso')
    
def PagarCarrinho():
    precoTotal = 0
    for i in range(len(carrinho)):
        precoTotal = precoTotal + carrinho[i]['preco']
    print('Preco a ser pagado: ', precoTotal)

    for i in range(len(carrinho)):
        carrinho[i]['quant'] = carrinho[i]['quant'] - 1 
    
    LimparCarrinho()
    
def LimparCarrinho():
    for i in range(len(carrinho)):
        carrinho.pop()

def AchaProduto(cod):
    for i in range(len(prod)):
        if cod == prod[i]['cod']:
            posicao = i
            break
        else:
            posicao = -1
    if posicao == -1:
        print("Produto não encontrado.")
    else:
        return(posicao)

    

