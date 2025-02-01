public class CamaroteInferior extends VIP {
    private String localizacao;

    public CamaroteInferior(double valor, double valorAdicional, String localizacao) {
        super(valor, valorAdicional);
        this.localizacao = localizacao;
    }

    public void imprimeLocalizacao() {
        System.out.println("Localização do ingresso: Camarote Inferior - " + localizacao);
    }
}