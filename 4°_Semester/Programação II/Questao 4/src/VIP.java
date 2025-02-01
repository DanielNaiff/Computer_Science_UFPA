public class VIP extends Ingresso {
    private double valorAdicional;

    public VIP(double valor, double valorAdicional) {
        super(valor);
        this.valorAdicional = valorAdicional;
    }

    public double getValorVIP() {
        return getValor() + valorAdicional;
    }

    @Override
    public void imprimeValor() {
        System.out.println("Valor do ingresso VIP: R$ " + getValorVIP());
    }
}
