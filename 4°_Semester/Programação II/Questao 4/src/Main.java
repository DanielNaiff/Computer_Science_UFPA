import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Definir preço básico
        double precoNormal = 50.0;
        double precoVIP = 100.0;
        double adicionalVIP = 50.0;
        double adicionalCamaroteSuperior = 30.0;

        System.out.println("Escolha o tipo de ingresso: ");
        System.out.println("1 - Ingresso Normal");
        System.out.println("2 - Ingresso VIP");
        int tipoIngresso = scanner.nextInt();

        Ingresso ingresso = null;

        if (tipoIngresso == 1) {
            ingresso = new Normal(precoNormal);
            ingresso.imprimeValor();
        } else if (tipoIngresso == 2) {
            System.out.println("Escolha o tipo de Camarote: ");
            System.out.println("1 - Camarote Inferior");
            System.out.println("2 - Camarote Superior");
            int tipoCamarote = scanner.nextInt();

            if (tipoCamarote == 1) {
                System.out.println("Digite a localização do Camarote Inferior: ");
                String localizacao = scanner.next();
                ingresso = new CamaroteInferior(precoVIP, adicionalVIP, localizacao);
                ((CamaroteInferior) ingresso).imprimeLocalizacao();
                ingresso.imprimeValor();
            } else if (tipoCamarote == 2) {
                ingresso = new CamaroteSuperior(precoVIP, adicionalVIP, adicionalCamaroteSuperior);
                ingresso.imprimeValor();
            }
        }

        System.out.println("Escolha o combo de pipoca: ");
        System.out.println("1 - Pequena (R$ 10)");
        System.out.println("2 - Média (R$ 15)");
        System.out.println("3 - Grande (R$ 20)");
        int tipoPipoca = scanner.nextInt();

        double valorPipoca = 0;
        if (tipoPipoca == 1) {
            valorPipoca = 10;
        } else if (tipoPipoca == 2) {
            valorPipoca = 15;
        } else if (tipoPipoca == 3) {
            valorPipoca = 20;
        }

        double valorFinal = ingresso.getValor() + valorPipoca;
        System.out.println("Valor do ingresso: R$ " + ingresso.getValor());
        System.out.println("Valor do combo de pipoca: R$ " + valorPipoca);
        System.out.println("Valor final da compra: R$ " + valorFinal);

        scanner.close();
    }
}
