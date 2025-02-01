public class No {
    private No esq;
    private No dir;
    private int fb;
    private int valor;
    private int altura;

    public No(No esq, No dir, int fb, int valor, int altura) {
        this.esq = esq;
        this.dir = dir;
        this.fb = fb;
        this.valor = valor;
        this.altura = altura;
    }

    public No(){}

    public int getAltura() {
        return altura;
    }

    public No getEsq() {
        return esq;
    }

    public void setEsq(No esq) {
        this.esq = esq;
    }

    public No getDir() {
        return dir;
    }

    public void setDir(No dir) {
        this.dir = dir;
    }

    public int getFb() {
        return fb;
    }

    public int getValor() {
        return valor;
    }

    public void setValor(int valor) {
        this.valor = valor;
    }
}
