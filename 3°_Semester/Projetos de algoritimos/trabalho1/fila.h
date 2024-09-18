#ifndef FILA_H
#define FILA_H

#include <stdio.h>
#include <stdlib.h>

#define MAX_NOME 50  // Definindo o tamanho máximo para o nome

typedef char TipoItem[MAX_NOME];  // TipoItem é um array de char

typedef struct Celula *Apontador;

typedef struct Celula {
    TipoItem Item;
    Apontador Prox;
} Celula;

typedef struct TipoFila {
    Apontador Frente, Tras;
} TipoFila;

// Funções para manipulação da fila
void FFVazia(TipoFila *Fila);
int Vazia(const TipoFila *Fila);
void Enfileira(const TipoItem x, TipoFila *Fila);
TipoItem* Desenfileira(TipoFila *Fila);  // Ajustado para retornar um ponteiro
void Emparelhar(TipoFila *Homens, TipoFila *Mulheres, TipoFila *Sobressalentes);
void ImprimirFila(const TipoFila *Fila);

#endif
