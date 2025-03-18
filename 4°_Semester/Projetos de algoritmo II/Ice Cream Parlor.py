def quaisSabores(custos, dinheiro):
    mapa_custos = {}
    
    for i, custo in enumerate(custos):
        complemento = dinheiro - custo
        if complemento in mapa_custos:
            print(mapa_custos[complemento], i + 1)
            return
        mapa_custos[custo] = i + 1
        

t = int(input())
for _ in range(t):
    dinheiro = int(input())
    n = int(input())
    custos = list(map(int, input().split()))
    quaisSabores(custos, dinheiro)