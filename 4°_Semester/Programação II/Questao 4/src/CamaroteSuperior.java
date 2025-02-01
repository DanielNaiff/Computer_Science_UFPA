public class CamaroteSuperior extends VIP {
    private double valorAdicionalSuperior;

    public CamaroteSuperior(double valor, double valorAdicional, double valorAdicionalSuperior) {
        super(valor, valorAdicional);
        this.valorAdicionalSuperior = valorAdicionalSuperior;
    }

    @Override
    public double getValorVIP() {
        return super.getValorVIP() + valorAdicionalSuperior;
    }

    public void imprimeValor() {
        System.out.println("Valor do ingresso Camarote Superior: R$ " + getValorVIP());
    }
}