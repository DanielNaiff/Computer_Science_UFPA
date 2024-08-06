#ifndef CONTATOS_H
#define CONTATOS_H

#include <string>

typedef int Posicao;
#define InicioVetor 0
#define MaxTam 1000

using namespace std;

typedef struct data{
  int Dia;
  int Mes;
}Data;

typedef struct tipocontato{
  string Nome;
  string Telefone;
  string Celular;
  string Email;
  Data DataAniversario;
}TipoContato;

typedef struct tipolista{
  TipoContato Contatos[MaxTam];
  Posicao Primeiro, Ultimo;
}TipoLista;


TipoLista* InicializaLista();
void InsereContato (TipoContato* ,TipoLista* );
void ListarContatos (TipoLista* );
int BuscarContato(string ,TipoLista* );
int RemoverContato (string , TipoLista* ); 
TipoLista* AtualizaContato(string,TipoContato*, TipoLista* );
void RemoveDuplicados (TipoLista* ); 
void LiberaAgenda (TipoLista* );
void Pulalinha();

#endif