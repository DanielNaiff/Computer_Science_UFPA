public class Memento {
    private StringBuilder estado;

    public Memento(StringBuilder estado){
        this.estado = new StringBuilder(estado);
    }

    public StringBuilder getEstado(){
        return estado;
    }
}
