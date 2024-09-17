#include <iostream>
#include <cstdlib>
#include "lista.h"
#include <map>
#include <utility> 
#include <map>
#include <limits>

using namespace std;

/* Inicializa uma lista */
TipoLista* InicializaLista(){
  TipoLista* lista = (TipoLista*)malloc(sizeof(TipoLista));
  return lista;
}

/* Faz a lista ficar vazia */
void FLVazia (TipoLista* Lista) {
  Lista->Primeiro = InicioVetor;
  Lista->Ultimo = Lista->Primeiro; 
}

/*Verifica se a lista está vazia*/
int Vazia (TipoLista* Lista){
  return (Lista->Primeiro == Lista->Ultimo); 
}

/* Insere x após o último elemento da lista */
void Insere (TipoItem* x, TipoLista *Lista) {
  if (Lista ->Ultimo >= MaxTam)
    cout << "Lista está cheia" << endl;
  else{ 
    Lista ->Item[Lista->Ultimo] = *x; 
    Lista->Ultimo++;
  } 
}

int Busca(int chave, TipoLista* lista){
  for(int i = 0; i < lista->Ultimo; i++){
    if(lista->Item[i].valor == chave){
      return 1;
      break;
    }else{
      return 0;
    }
  }
  return 0;
}

int Tamanho_lista(TipoLista* Lista){
  if (Lista == NULL)
    return -1;
  else 
    return Lista->Ultimo;
}

/*Retorna o item x que está na posição p da lista, retirando-o da lista e deslocando os itens a partir da posição p+1 para as posições anteriores */
TipoItem* Retira (Posicao p, TipoLista* Lista) {
  int Aux; 
  TipoItem* item;
  item = (TipoItem*) malloc(sizeof(TipoItem)); 
  if (Vazia(Lista) || p >= Lista->Ultimo){
    cout << "A posição não existe!" << endl;
    return NULL; 
  }
  *item = Lista->Item[p]; 
  Lista->Ultimo--; 
  for (Aux = p; Aux < Lista->Ultimo; Aux++)
    Lista->Item[Aux] = Lista->Item[Aux+1]; 
  return item;
}

/*Imprime os itens da lista na ordem de ocorrência */ 
void Imprime (TipoLista* Lista){
  if (Tamanho_lista(Lista) == 0){
    cout << "Lista vazia" << endl << endl;
  }else{
    cout << "Valores na lista" << endl;
    cout << "p - key" << endl;
      for (int Aux = Lista->Primeiro; Aux < Lista->Ultimo; Aux++){
        cout << Aux << " - " << Lista->Item[Aux].valor  << endl;
      } 
      cout << endl;
  }
}

TipoItem* InicializaTipoItem() {
    TipoItem* item = (TipoItem*) malloc(sizeof(TipoItem));
    if (item == NULL) {
        cout << "Erro ao alocar memória para TipoItem" << endl;
        exit(1);
    }
    item->valor = 0;  // Inicializa o valor com 0, você pode mudar para outro valor padrão se desejar
    return item;
}

/* Modifica o valor de um TipoItem */
void ModificaValorItem(TipoItem* item, int valor) {
    if (item != NULL) {
        item->valor = valor;
    } else {
        cout << "TipoItem não inicializado" << endl;
    }
}

/* Imprime o valor de um TipoItem */
void ImprimeTipoItem(TipoItem* item) {
    if (item != NULL) {
        cout << "Valor do TipoItem: " << item->valor << endl;
    } else {
        cout << "TipoItem não inicializado" << endl;
    }
}

void EncontrarMaisEMenosFrequentes(TipoLista* lista) {
    if (Vazia(lista)) {
        cout << "A lista está vazia." << endl;
        return;
    }

    map<int, int> contagem;
    
    // Contar a frequência de cada elemento
    for (int i = lista->Primeiro; i < lista->Ultimo; ++i) {
        contagem[lista->Item[i].valor]++;
    }

    // Encontrar o elemento com mais e menos ocorrências
    int max_freq = numeric_limits<int>::min();
    int min_freq = numeric_limits<int>::max();
    int mais_frequente = 0;
    int menos_frequente = 0;

    for (const auto& par : contagem) {
        if (par.second > max_freq) {
            max_freq = par.second;
            mais_frequente = par.first;
        }
        if (par.second < min_freq) {
            min_freq = par.second;
            menos_frequente = par.first;
        }
    }

    cout << "Elemento mais frequente: " << mais_frequente << " com " << max_freq << " ocorrências." << endl;
    cout << "Elemento menos frequente: " << menos_frequente << " com " << min_freq << " ocorrências." << endl;
}

TipoLista2* InicializaLista2() {
    TipoLista2* lista = (TipoLista2*)malloc(sizeof(TipoLista2));
    if (lista == NULL) {
        cout << "Erro ao alocar memória para TipoLista2" << endl;
        exit(1);
    }
    FLVazia((TipoLista*)lista); // Utilize a função FLVazia para inicializar os índices
    return lista;
}

void ConstruirLista2(TipoLista* lista1, TipoLista2* lista2) {
    if (Vazia(lista1)) {
        cout << "Lista L1 está vazia." << endl;
        return;
    }

    map<int, int> contagem;
    
    // Contar a frequência de cada elemento em L1
    for (int i = lista1->Primeiro; i < lista1->Ultimo; ++i) {
        contagem[lista1->Item[i].valor]++;
    }

    // Construir a lista L2
    FLVazia((TipoLista*)lista2);
    for (const auto& par : contagem) {
        TipoItem2 item;
        item.elem = par.first;
        item.count = par.second;
        Insere((TipoItem*)&item, (TipoLista*)lista2); // Insere em lista2
    }
}
void ImprimeLista2(TipoLista2* lista2) {
    if (Tamanho_lista((TipoLista*)lista2) == 0) {
        cout << "Lista L2 vazia" << endl << endl;
    } else {
        cout << "Valores na lista L2" << endl;
        cout << "Elemento - Contagem" << endl;
        for (int i = lista2->Primeiro; i < lista2->Ultimo; ++i) {
            cout << lista2->Item[i].elem << " - " << lista2->Item[i].count << endl;
        }
        cout << endl;
    }
}
