#include <iostream>
#include <cstdlib>
#include "fila.h"

using namespace std;

void FFVazia(TipoFila *Fila){
  Fila->Frente = (Apontador)malloc(sizeof(Celula));
  Fila->Tras = Fila->Frente;
  Fila->Frente->Prox = NULL;
}

int Vazia(TipoFila *Fila){
  return(Fila->Frente->Prox == NULL);
}

void Enfileira(TipoItem x, TipoFila *Fila){
  Fila->Tras->Prox = (Apontador) malloc(sizeof(Celula));
  Fila->Tras = Fila->Tras->Prox;
  Fila->Tras->Item = x;
  Fila->Tras->Prox = NULL;
}

TipoItem Desenfileira(TipoFila *Fila){
  Apontador q;
  if(Vazia(Fila)){
    printf("Erro: fila está vazia\n"); 
  }
  q = Fila->Frente;
  Fila->Frente = Fila->Frente->Prox;
  free(q);
  return Fila->Frente->Item;
}

int Comprimento(TipoFila *Fila) {
    int cont = 0;
    Apontador p = Fila->Frente->Prox;  
    while (p != NULL) {
        cont++;
        p = p->Prox;
    }
    return cont;
}