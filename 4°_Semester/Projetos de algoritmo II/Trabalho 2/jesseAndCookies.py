#conta principal: danielnaiff344

class HeapMinima:
    def __init__(self):
        self.heap = []
    
    def inserir(self, valor):
        self.heap.append(valor)
        self._ajustar_cima(len(self.heap) - 1)
    
    def remover(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        topo = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._ajustar_baixo(0)
        return topo
    
    def _ajustar_cima(self, indice):
        pai = (indice - 1) // 2
        while indice > 0 and self.heap[indice] < self.heap[pai]: 
            self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
            indice = pai
            pai = (indice - 1) // 2
    
    def _ajustar_baixo(self, indice):
        tamanho = len(self.heap)
        while True:
            esquerda = 2 * indice + 1
            direita = 2 * indice + 2
            menor = indice
            if esquerda < tamanho and self.heap[esquerda] < self.heap[menor]: 
                menor = esquerda
            if direita < tamanho and self.heap[direita] < self.heap[menor]:  
                menor = direita
            if menor == indice:
                break
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            indice = menor
    
    def topo(self):
        return self.heap[0] if self.heap else None
    
    def tamanho(self):
        return len(self.heap)

def cookies(k, A):
    heap = HeapMinima()
    
    for valor in A:
        heap.inserir(valor)
    
    contagem = 0
    
    if heap.topo() >= k:
        return 0
    
    while heap.tamanho() > 1 and heap.topo() < k:
        primeiro = heap.remover()
        segundo = heap.remover()
        
        novo_cookies = primeiro + 2 * segundo
        
        heap.inserir(novo_cookies)
        
        contagem += 1
    
    if heap.topo() >= k:
        return contagem
    return -1

if __name__ == "__main__":
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    print(cookies(k, A))
