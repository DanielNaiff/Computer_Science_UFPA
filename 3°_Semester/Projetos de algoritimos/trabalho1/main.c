#include "fila.h"

int main() {
    TipoFila Homens, Mulheres, Sobressalentes;
    TipoItem pessoa;
    char genero;

    FFVazia(&Homens);
    FFVazia(&Mulheres);
    FFVazia(&Sobressalentes);

    // Adicionando pessoas automaticamente
    const char* nomes[] = {"Joana", "Francisco", "João", "Samuel", "Maria", "Davi", "Cristiano", "Beatriz"};
    const char generos[] = {'M', 'H', 'H', 'H', 'M', 'H', 'H', 'M'};

    for (int i = 0; i < 8; i++) {
        snprintf(pessoa, MAX_NOME, "%s", nomes[i]);
        genero = generos[i];
        if (genero == 'H') {
            Enfileira(pessoa, &Homens);
        } else if (genero == 'M') {
            Enfileira(pessoa, &Mulheres);
        }
    }

    // Adicionando novas pessoas pelo usuário
    printf("Digite o nome das pessoas e o gênero (H ou M) ou 'sair' para finalizar:\n");
    while (1) {
        printf("Nome: ");
        fgets(pessoa, MAX_NOME, stdin);
        pessoa[strcspn(pessoa, "\n")] = 0;  // Remove newline character

        if (strcmp(pessoa, "sair") == 0) {
            break;
        }

        printf("Gênero (H ou M): ");
        scanf(" %c", &genero);
        getchar(); // Clear newline from input buffer

        if (genero == 'H') {
            Enfileira(pessoa, &Homens);
        } else if (genero == 'M') {
            Enfileira(pessoa, &Mulheres);
        } else {
            printf("Gênero inválido\n");
        }
    }

    Emparelhar(&Homens, &Mulheres, &Sobressalentes);

    printf("Sobressalentes:\n");
    ImprimirFila(&Sobressalentes);

    return 0;
}
