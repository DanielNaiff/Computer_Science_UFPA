import java.util.List;

public class Pokemon {
    private String nome;
    private String tipo;
    private String status;
    private int hp;
    private List<Ataque> ataques;

    public Pokemon(String nome, String tipo, String status, int hp, List<Ataque> ataques) {
        this.nome = nome;
        this.tipo = tipo;
        this.status = status;
        this.hp = hp;
        this.ataques = ataques;
    }

    public void usarAtaque(int index) {
        if (index >= 0 && index < ataques.size()) {
            Ataque ataque = ataques.get(index);
            System.out.println(nome + " usou " + ataque.getNome() + " causando " + ataque.getDano() + " de dano!");
        }
    }

    public void mostrarStatus() {
        System.out.println("Status de " + nome + ": " + status);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public int getHp() {
        return hp;
    }

    public void setHp(int hp) {
        this.hp = hp;
    }

    public List<Ataque> getAtaques() {
        return ataques;
    }

    public void setAtaques(List<Ataque> ataques) {
        this.ataques = ataques;
    }
}
