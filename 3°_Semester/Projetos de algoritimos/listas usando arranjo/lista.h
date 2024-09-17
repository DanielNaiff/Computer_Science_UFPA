typedef int Posicao;
#define InicioVetor 0
#define MaxTam  1000

typedef struct tipoitem {
  int valor;
  /* outros componentes */
}TipoItem;

typedef struct tipolista{
  TipoItem Item[MaxTam];
  Posicao Primeiro, Ultimo;
}TipoLista;

typedef struct tipoitem2 {
    int elem;
    int count;
} TipoItem2;

typedef struct tipolista2 {
    TipoItem2 Item[MaxTam];
    Posicao Primeiro, Ultimo;
} TipoLista2;

TipoLista* InicializaLista();
void FLVazia (TipoLista* );
int Vazia (TipoLista* );
int Tamanho_lista(TipoLista* );
void Insere (TipoItem* , TipoLista* ); 
int Busca(int, TipoLista* );
TipoItem* Retira (Posicao, TipoLista* ); 
void Imprime (TipoLista* );

//TODO: funções a serem implementadas
TipoItem* InicializaTipoItem();
void ModificaValorItem (TipoItem* , int ); 
void ImprimeTipoItem(TipoItem* );

void EncontrarMaisEMenosFrequentes(TipoLista* );
void ImprimeLista2(TipoLista2* );
void ConstruirLista2(TipoLista* , TipoLista2*);
TipoLista2* InicializaLista2();