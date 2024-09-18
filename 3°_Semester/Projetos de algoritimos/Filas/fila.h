typedef int TipoChave;

typedef struct TipoItem{
  TipoChave Chave;
}TipoItem;

typedef struct Celula *Apontador;

typedef struct Celula{
  TipoItem Item;
  Apontador Prox;
}Celula;

typedef struct TipoFila{
  Apontador Frente, Tras;
}TipoFila;

void FFVazia(TipoFila *Fila);

void Enfileira(TipoItem x, TipoFila *Fila);

TipoItem Desenfileira(TipoFila *Fila);