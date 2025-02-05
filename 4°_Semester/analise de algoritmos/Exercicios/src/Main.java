import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int K = scanner.nextInt();

        List<String> alunos = new ArrayList<>();

        scanner.nextLine();
        for (int i = 0; i < N; i++) {
            alunos.add(scanner.nextLine());
        }

        Collections.sort(alunos);

        System.out.println(alunos.get(K - 1));
    }
}
