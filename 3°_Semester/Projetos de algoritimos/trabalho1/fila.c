#include "fila.h"

// Inicializa uma fila vazia
void FFVazia(TipoFila *Fila) {
    Fila->Frente = Fila->Tras = (Celula *)malloc(sizeof(Celula));
    if (Fila->Frente == NULL) {
        printf("Erro ao alocar memória\n");
        exit(EXIT_FAILURE);
    }
    Fila->Frente->Prox = NULL;
}

// Verifica se a fila está vazia
int Vazia(const TipoFila *Fila) {
    return Fila->Frente == Fila->Tras;
}

// Adiciona um item à fila
void Enfileira(const TipoItem x, TipoFila *Fila) {
    Fila->Tras->Prox = (Celula *)malloc(sizeof(Celula));
    if (Fila->Tras->Prox == NULL) {
        printf("Erro ao alocar memória\n");
        exit(EXIT_FAILURE);
    }
    Fila->Tras = Fila->Tras->Prox;
    for (int i = 0; i < MAX_NOME; i++) {
        Fila->Tras->Item[i] = x[i];  // Copia o array de caracteres
    }
    Fila->Tras->Prox = NULL;
}

// Remove um item da fila
TipoItem* Desenfileira(TipoFila *Fila) {
    if (Vazia(Fila)) {
        printf("Erro: fila está vazia\n");
        exit(EXIT_FAILURE);
    }
    Celula *q = Fila->Frente;
    TipoItem *item = &Fila->Frente->Prox->Item;
    Fila->Frente = Fila->Frente->Prox;
    free(q);
    return item;
}

// Emparelha homens e mulheres e coloca os sobrantes na fila de sobressalentes
void Emparelhar(TipoFila *Homens, TipoFila *Mulheres, TipoFila *Sobressalentes) {
    while (!Vazia(Homens) && !Vazia(Mulheres)) {
        TipoItem *homem = Desenfileira(Homens);
        TipoItem *mulher = Desenfileira(Mulheres);
        printf("Par: Homem %s e Mulher %s\n", *homem, *mulher);
    }

    // Se houver homens sobrando, coloque-os na fila de sobressalentes
    while (!Vazia(Homens)) {
        TipoItem *homem = Desenfileira(Homens);
        Enfileira(*homem, Sobressalentes);
    }

    // Se houver mulheres sobrando, coloque-as também na fila de sobressalentes
    while (!Vazia(Mulheres)) {
        TipoItem *mulher = Desenfileira(Mulheres);
        Enfileira(*mulher, Sobressalentes);
    }
}

// Imprime o conteúdo da fila
void ImprimirFila(const TipoFila *Fila) {
    Celula *c = Fila->Frente->Prox;
    while (c != NULL) {
        printf("%s ", c->Item);
        c = c->Prox;
    }
    printf("\n");
}
