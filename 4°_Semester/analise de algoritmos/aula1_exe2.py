def soma_quadrados_A(n):
    x = 0
    for j in range(n):
        x = x + j*j
    return x
    
def soma_quadrados_B(n):
    x = n*(n+1)*(2*n+1)
    x = x/6
    return x