import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Ataque ataque1 = new Ataque("Raio", 40, "Elétrico");
        Ataque ataque2 = new Ataque("Choque do Trovão", 60, "Elétrico");

        Pokemon pikachu = new Pokemon(
                "Pikachu",
                Tipo.ELETRICO.name(),
                Status.DORMINDO,
                100,
                Arrays.asList(ataque1, ataque2)
        );

        pikachu.usarAtaque(0);
        pikachu.mostrarStatus();
    }
}
