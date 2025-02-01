public abstract class Animal {
    private String nome;
    private Double comprimento;
    private int nPatas;
    private String cor;
    private String ambiente;
    private Double velocidade;

    public Animal(String nome, Double comprimento, int nPatas, String cor, String ambiente, Double velocidade) {
        this.nome = nome;
        this.comprimento = comprimento;
        this.nPatas = nPatas;
        this.cor = cor;
        this.ambiente = ambiente;
        this.velocidade = velocidade;
    }

    public Animal(){}

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Double getComprimento() {
        return comprimento;
    }

    public void setComprimento(Double comprimento) {
        this.comprimento = comprimento;
    }

    public int getnPatas() {
        return nPatas;
    }

    public void setnPatas(int nPatas) {
        this.nPatas = nPatas;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getAmbiente() {
        return ambiente;
    }

    public void setAmbiente(String ambiente) {
        this.ambiente = ambiente;
    }

    public Double getVelocidade() {
        return velocidade;
    }

    public void setVelocidade(Double velocidade) {
        this.velocidade = velocidade;
    }

    @Override
    public String toString() {
        return "Animal: " + nome + "\n" +
                "Comprimento: " + comprimento + " cm\n" +
                "Patas: " + nPatas + "\n" +
                "Cor: " + cor + "\n" +
                "Ambiente: " + ambiente + "\n" +
                "Velocidade: " + velocidade + "m/s";
    }

}
