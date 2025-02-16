import java.util.ArrayList;
import java.util.List;

public class EditorDeTexto {
    private StringBuilder texto;
    private List<Memento> historico;

    public EditorDeTexto() {
        texto = new StringBuilder();
        historico = new ArrayList<>();
    }

    public void adicionarTexto(String novoTexto) {
        salvarEstado();
        texto.append(novoTexto);
    }

    public void desfazer() {
        if (!historico.isEmpty()) {
            Memento memento = historico.remove(historico.size() - 1);
            texto = memento.getEstado();
        }
    }

    public String mostrarTexto() {
        return texto.toString();
    }

    private void salvarEstado() {
        Memento memento = new Memento(new StringBuilder(texto));
        historico.add(memento);
    }
}
