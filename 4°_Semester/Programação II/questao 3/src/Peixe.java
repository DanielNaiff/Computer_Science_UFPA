public class Peixe extends Animal {
    private String caract;

    public Peixe(String nome, Double comprimento, int nPatas, String cor, String ambiente, Double velocidade, String caract) {
        super(nome, comprimento, nPatas, cor, ambiente, velocidade);
        this.caract = caract;
    }

    public Peixe(String caract) {
        this.caract = caract;
    }

    public String getCaract() {
        return caract;
    }

    public void setCaract(String caract) {
        this.caract = caract;
    }

    @Override
    public String toString() {
        return super.toString() + "\n" +
                "Caracteristicas: " + caract;
    }

}
