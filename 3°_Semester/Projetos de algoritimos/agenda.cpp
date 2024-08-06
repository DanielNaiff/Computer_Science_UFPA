#include <iostream>
#include <cstdlib>
#include "agenda.h"

using namespace std;


TipoLista* InicializaLista(){
    TipoLista* lista = new TipoLista;
    lista->Ultimo = 0; // Inicializa o contador Ultimo
    return lista;
}

void InsereContato(TipoContato* Contato, TipoLista *Lista){
  if (Lista ->Ultimo >= MaxTam)
    cout << "Agenda está cheia" << endl;
  else{ 
    Lista ->Contatos[Lista->Ultimo] = *Contato; 
    Lista->Ultimo++;
  } 
}

void ListarContatos(TipoLista *Lista){
  if (Lista == NULL){
    cout << "Lista não foi inicializada" << endl;
    return;
  }
  if (Lista ->Ultimo == 0){
    cout << "Agenda está vazia" << endl;
  }

  else {
    cout << "=========Contatos na Agenda=========: "  << endl;
    for (int i = 0; i < Lista->Ultimo; i++){
      cout << "Nome: " << Lista->Contatos[i].Nome << endl;
      cout << "Telefone: " << Lista->Contatos[i].Telefone << endl;
      cout << "Celular: " << Lista->Contatos[i].Celular << endl;
      cout << "Email: " << Lista->Contatos[i].Email << endl;
      cout << "Data de Aniversário: " << Lista->Contatos[i].DataAniversario.Dia << "/"<< Lista->Contatos[i].DataAniversario.Mes << endl;

      cout << "\n================================== "  << endl;
    }
  }
}

int BuscarContato(string Nome,TipoLista *Lista){
  int cont = 0;
  for (int i = 0; i < Lista->Ultimo; i++){
    if (Nome == Lista->Contatos[i].Nome){
      cout << "\n================================== "  << endl;
      cout << "Nome: " << Lista->Contatos[i].Nome << endl;
      cout << "Telefone: " << Lista->Contatos[i].Telefone << endl;
      cout << "Celular: " << Lista->Contatos[i].Celular << endl;
      cout << "Email: " << Lista->Contatos[i].Email << endl;
      cout << "Data de Aniversário: " << Lista->Contatos[i].DataAniversario.Dia << "/"<< Lista->Contatos[i].DataAniversario.Mes << endl;
      cout << "\n================================== "  << endl;
      cont++;
    }
  }

  if (cont == 0){
    cout << "Contato não encontrado" << endl;
    return 0;
  }
  return 1;
}

int RemoverContato(string Nome,TipoLista *Lista){
  int cont = 0;
  for (int i = 0; i < Lista->Ultimo; i++){
    if (Nome == Lista->Contatos[i].Nome)
    {
      cout << "\n================================== "  << endl;
      cout << "Nome: " << Lista->Contatos[i].Nome << endl;
      cout << "Telefone: " << Lista->Contatos[i].Telefone << endl;
      cout << "Celular: " << Lista->Contatos[i].Celular << endl;
      cout << "Email: " << Lista->Contatos[i].Email << endl;
      cout << "Data de Aniversário: " << Lista->Contatos[i].DataAniversario.Dia << "/"<< Lista->Contatos[i].DataAniversario.Mes << endl;
      cout << "\n================================== "  << endl;
      cont++;
       for (; i < Lista->Ultimo; i++)
       {
        Lista->Contatos[i] = Lista->Contatos[i+1];
        Lista->Ultimo--;
       }
    }

  if (cont == 0){
    cout << "Contato não encontrado" << endl;
    return 0;
                }
  
}
return 1;}

TipoLista* AtualizaContato(string Nome,TipoContato* Contato, TipoLista *Lista){
  for (int i = 0; i < Lista->Ultimo; i++){
    if (Nome == Lista->Contatos[i].Nome)
    {
      Lista->Contatos[i] = *Contato;
    }
  }
  return Lista;
}

void RemoveDuplicados(TipoLista *Lista){
  for (int i = 0; i < Lista->Ultimo; i++){
    for (int j = i+1; j < Lista->Ultimo; j++){
      if (Lista->Contatos[i].Nome == Lista->Contatos[j].Nome){
        for (; j < Lista->Ultimo; j++){
          Lista->Contatos[j] = Lista->Contatos[j+1];
          Lista->Ultimo--;
        }
      }
    }
  }
}

void LiberaAgenda(TipoLista *Lista){
  delete Lista;
}

void Pulalinha(){
  cout << "\n";
}