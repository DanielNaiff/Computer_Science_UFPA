import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        EditorDeTexto editor = new EditorDeTexto();

        while (true) {
            System.out.println("Editor de Texto:");
            System.out.println("Texto Atual: " + editor.mostrarTexto());
            System.out.println("Escolha uma ação:");
            System.out.println("1. Adicionar texto");
            System.out.println("2. Desfazer (Ctrl + Z)");
            System.out.println("3. Sair");
            System.out.print("Digite a opção: ");
            int opcao = scanner.nextInt();
            scanner.nextLine();  // Consumir o newline

            if (opcao == 1) {
                System.out.print("Digite o texto a ser adicionado: ");
                String texto = scanner.nextLine();
                editor.adicionarTexto(texto);
            } else if (opcao == 2) {
                editor.desfazer();
            } else if (opcao == 3) {
                break;
            } else {
                System.out.println("Opção inválida!");
            }
        }

        scanner.close();
    }
}
