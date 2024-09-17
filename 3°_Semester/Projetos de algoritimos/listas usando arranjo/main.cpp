#include <iostream>
#include <cstdlib>
#include "lista.h"

using namespace std;

int main(void) {
    int valor, op;
    TipoLista* list1;
    TipoLista2* list2;

    list1 = InicializaLista();
    list2 = InicializaLista2();

    while (1) {
        cout << "1 - Inserir elemento em L1\n";
        cout << "2 - Remover elemento de L1\n";
        cout << "3 - Mostrar L1\n";
        cout << "4 - Consultar elemento em L1\n";
        cout << "5 - Tamanho de L1\n";
        cout << "6 - Tornar L1 vazia\n";
        cout << "7 - Encontrar elementos mais e menos frequentes em L1\n";
        cout << "8 - Gerar e mostrar L2\n";
        cout << "9 - Sair\n";
        cout << "Opcao? ";
        scanf("%d", &op);

        int ret = 0; // Declarar a variável ret

        switch (op) {
            case 1: // Inserir elemento em L1
                cout << "Qual o valor para ser inserido? ";
                cin >> valor;
                TipoItem* item;
                item = (TipoItem*)malloc(sizeof(TipoItem));
                item->valor = valor;
                Insere(item, list1);
                cout << "Valor inserido com sucesso na lista L1" << endl << endl;
                free(item);
                break;
            case 2: // Remover elemento de L1
                cout << "Qual a posição entre [" << InicioVetor << " e " << list1->Ultimo - 1 << "] para ser removido o elemento? ";
                cin >> valor;
                TipoItem* it;
                it = Retira(valor, list1);
                if (it != NULL) {
                    cout << "Valor " << it->valor << " removido da lista L1" << endl << endl;
                    free(it);
                }
                break;
            case 3: // Mostrar L1
                Imprime(list1);
                break;
            case 4: // Consultar elemento em L1
                cout << "Qual o valor para consultar? ";
                cin >> valor;
                ret = Busca(valor, list1);
                if (ret == 1) {
                    cout << "Valor " << valor << " encontrado na lista L1" << endl << endl;
                } else {
                    cout << "Valor " << valor << " não encontrado na lista L1" << endl << endl;
                }
                break;
            case 5: // Tamanho de L1
                cout << "Lista L1 vazia?: " << Vazia(list1) << endl;
                cout << "Tamanho de L1: " << Tamanho_lista(list1) << endl << endl;
                break;
            case 6: // Tornar L1 vazia
                FLVazia(list1);
                cout << "Lista L1 ficou vazia" << endl << endl;
                break;
            case 7: // Encontrar mais e menos frequentes em L1
                EncontrarMaisEMenosFrequentes(list1);
                break;
            case 8: // Gerar e mostrar L2
                ConstruirLista2(list1, list2);
                ImprimeLista2(list2);
                break;
            case 9: // Sair
                free(list1);
                free(list2);
                exit(0);
        }
    }
}