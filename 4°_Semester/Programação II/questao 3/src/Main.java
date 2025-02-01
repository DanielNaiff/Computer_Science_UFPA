public class Main {
    public static void main(String[] args) {
        Animal camelo = new Mamifero("Camelo", 150.0, 4, "Amarelo", "Terra", 2.0, "Plantas");
        Animal tubarao = new Peixe("Tubarao", 300.0, 0, "Cinzento", "Mar", 1.5, "Barbatanas");
        Animal urso = new Mamifero("Urso-do-canada", 180.0, 4, "Vermelho", "Terra", 0.5, "Mel");

        System.out.println(camelo);
        System.out.println("-=-=-=-=-=-=-=-=-=-=-=-=-");
        System.out.println(tubarao);
        System.out.println("-=-=-=-=-=-=-=-=-=-=-=-=-");
        System.out.println(urso);
    }
}