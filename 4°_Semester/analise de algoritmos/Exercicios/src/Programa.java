import java.util.*;

public class Programa {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        scanner.nextLine(); // Consumir a linha em branco após o número de países

        // Lista para armazenar os dados de países e suas medalhas
        List<String[]> paises = new ArrayList<>();

        // Leitura dos dados dos países
        for (int i = 0; i < N; i++) {
            String nome = scanner.nextLine();  // Lê o nome do país
            int ouro = scanner.nextInt();      // Lê o número de medalhas de ouro
            int prata = scanner.nextInt();     // Lê o número de medalhas de prata
            int bronze = scanner.nextInt();    // Lê o número de medalhas de bronze
            scanner.nextLine(); // Consumir a linha em branco após os números

            // Armazenar os dados em um array de String (nome e medalhas)
            paises.add(new String[]{nome, String.valueOf(ouro), String.valueOf(prata), String.valueOf(bronze)});
        }

        // Ordenação dos países
        paises.sort((p1, p2) -> {
            // Comparar pelas medalhas de ouro (decrescente)
            int ouro1 = Integer.parseInt(p1[1]);
            int ouro2 = Integer.parseInt(p2[1]);
            if (ouro1 != ouro2) {
                return Integer.compare(ouro2, ouro1);
            }

            // Se ouro for igual, comparar pelas medalhas de prata (decrescente)
            int prata1 = Integer.parseInt(p1[2]);
            int prata2 = Integer.parseInt(p2[2]);
            if (prata1 != prata2) {
                return Integer.compare(prata2, prata1);
            }

            // Se prata também for igual, comparar pelas medalhas de bronze (decrescente)
            int bronze1 = Integer.parseInt(p1[3]);
            int bronze2 = Integer.parseInt(p2[3]);
            if (bronze1 != bronze2) {
                return Integer.compare(bronze2, bronze1);
            }

            // Se tudo for igual, ordenar alfabeticamente pelo nome
            return p1[0].compareTo(p2[0]);
        });

        // Exibir os resultados ordenados
        for (String[] p : paises) {
            System.out.println(p[0] + " " + p[1] + " " + p[2] + " " + p[3]);
        }
    }
}
