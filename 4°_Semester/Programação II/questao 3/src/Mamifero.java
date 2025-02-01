public class Mamifero extends Animal{
    private String alimento;

    public Mamifero(String nome, Double comprimento, int nPatas, String cor, String ambiente, Double velocidade, String alimento) {
        super(nome, comprimento, nPatas, cor, ambiente, velocidade);
        this.alimento = alimento;
    }

    public Mamifero(String alimento) {
        this.alimento = alimento;
    }

    @Override
    public String toString() {
        return super.toString() + "\n" +
                "Alimento: " + alimento;
    }

}
