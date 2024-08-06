#include "agenda.h"
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int main() {
  int op=9;
  TipoLista *Lista;
  Lista = InicializaLista();
  while (op!=7) {
    Pulalinha();
    cout << "1 - Inserir Contato\n";
    cout << "2 - Listar Contatos\n";
    cout << "3 - Buscar Contato\n";
    cout << "4 - Editar Contato\n";
    cout << "5 - Remover Contato\n";
    cout << "6 - Remover Contatos Duplicados\n";
    cout << "7 - Sair\n";
    cout << "Opcao? ";
    cin >> op;

    (void)system("clear");
      
    switch (op) {

    case 1: { // inserir contato
          string nome, telefone, celular, email;

          cout << "Nome do Contato: ";
          cin >> nome;
          while (nome.length() > 40) {
              cout << "Nome muito grande: ";
              cin >> nome;
          }

          cout << "Telefone do Contato: ";
          cin >> telefone;
          while (telefone.length() > 15) {
              cout << "Telefone muito grande: ";
              cin >> telefone;
          }

          cout << "Celular do Contato: ";
          cin >> celular;
          while (celular.length() > 15) {
              cout << "Celular muito grande: ";
              cin >> celular;
          }

          cout << "Email do Contato: ";
          cin >> email;
          while (email.length() > 40) {
              cout << "Email muito grande: ";
              cin >> email;
          }

          int dia, mes;

          cout << "Dia de Aniversario do contato [1-30]: ";
          cin >> dia;
          while (dia < 1 || dia > 30) {
              cout << "Dia inválido: ";
              cin >> dia;
          }

          cout << "Mes de Aniversario do contato [1-12]: ";
          cin >> mes;
          while (mes < 1 || mes > 12) {
              cout << "Mes inválido: ";
              cin >> mes;
          }

          TipoContato* Contato = new TipoContato;
          Contato->Nome = nome;
          Contato->Telefone = telefone;
          Contato->Celular = celular;
          Contato->Email = email;
          Contato->DataAniversario = { dia, mes };

          InsereContato(Contato, Lista);
        
          Pulalinha();
          cout << "Contato inserido com sucesso na agenda" << endl;

          delete Contato; // Liberando memória alocada
          break;
      }    
      
      case 2: {// Imprime Agenda 
      (void)system("clear");
      ListarContatos(Lista);
      break;
      }

      
      case 3: {//  mostrar os valores da lista
        (void)system("clear");
          string nome;
        cout << "Qual o nome voce busca?: ";
        cin >> nome;
        BuscarContato(nome, Lista);
        break;
      }
        
      case 4:  //  Editar contato
          {
          (void)system("clear");
          string nomeAtual;
          cout << "Qual o nome do contato para atualizar?";
          cin >> nomeAtual;
          
          
          if(BuscarContato(nomeAtual, Lista)){
              string Novonome, telefone, celular, email;

                cout << "Novo nome do Contato: ";
                cin >> Novonome;
                while (Novonome.length() > 40) {
                    cout << "Nome muito grande";
                    cin >> Novonome;
                }

                cout << "Novo telefone do Contato: ";
                cin >> telefone;
                while (telefone.length() > 15) {
                    cout << "Telefone muito grande";
                    cin >> telefone;
                }

                cout << "Novo celular do Contato: ";
                cin >> celular;
                while (celular.length() > 15) {
                    cout << "Celular muito grande ";
                    cin >> celular;
                }

                cout << "Novo email do Contato: ";
                cin >> email;
                while (email.length() > 40) {
                    cout << "Email muito grande";
                    cin >> email;
                }

                int dia, mes;

                cout << "Dia de Aniversario do contato [1-30]: ";
                cin >> dia;
                while (dia < 1 || dia > 30) {
                    cout << "Dia inválido";
                    cin >> dia;
                }

                cout << "Mes de Aniversario do contato [1-12]: ";
                cin >> mes;
                while (mes < 1 || mes > 12) {
                    cout << "Mes inválido";
                    cin >> mes;
                }

                TipoContato* Contato = new TipoContato;
                Contato->Nome = Novonome;
                Contato->Telefone = telefone;
                Contato->Celular = celular;
                Contato->Email = email;
                Contato->DataAniversario = { dia, mes };

                
                Lista = AtualizaContato(nomeAtual,Contato, Lista);

                Pulalinha();
                cout << "Contato atualizado com sucesso na agenda" << endl;

                // delete Contato; // Liberando memória alocada
                

              
          }
        break;
      }
      case 5: //  Remover
          {
            string nome;
            cout << "Qual o nome do contato para remover?";
            cin >> nome;
            RemoverContato(nome, Lista);
            break;
          }
      case 6: //  Remover Contatos Duplicados
        (void)system("clear");
        cout << "Contatos Duplicados Removidos \n" ;
        RemoveDuplicados(Lista);
        break;
      case 7: // abandonar o programa
          cout << "\nObrigado por usar o programa!\n";
        exit(0);
    }
  }
}