# Funcao Validar Meta

vendas = range(1000,3000)

print(list(vendas))

def bateu_meta(venda):
    if venda > 2500: 
        return True
    else: 
        return False
    
bateram_meta = filter(bateu_meta,vendas)

print(list(bateram_meta))


