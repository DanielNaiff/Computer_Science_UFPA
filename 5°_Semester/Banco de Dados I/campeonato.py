import graphviz

# Criação do diagrama MER com Graphviz
mer = graphviz.Digraph('MER_Campeonato_Futebol', format='png')
mer.attr(rankdir='LR', size='8,5')

# Entidades
entidades = {
    'Time': ['id_time (PK)', 'nome', 'cidade', 'estado', 'ano_fundacao'],
    'Jogador': ['id_jogador (PK)', 'nome', 'data_nascimento', 'nacionalidade', 'posicao'],
    'Estadio': ['id_estadio (PK)', 'nome', 'capacidade', 'localizacao'],
    'Jogo': ['id_jogo (PK)', 'data', 'placar_mandante', 'placar_visitante'],
    'Campeonato': ['id_campeonato (PK)', 'nome', 'ano', 'tipo'],
}

for entidade, atributos in entidades.items():
    mer.node(entidade, label=f'''<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">
        <TR><TD BGCOLOR="lightblue"><B>{entidade}</B></TD></TR>
        {''.join(f'<TR><TD>{attr}</TD></TR>' for attr in atributos)}
    </TABLE>>''', shape='plaintext')

# Relacionamentos com atributos
relacionamentos = {
    'Participa': (['data_entrada', 'data_saida'], ['Jogador', 'Time']),
    'Ocupa': ([], ['Jogo', 'Estadio']),
    'Disputa': (['fase', 'rodada'], ['Jogo', 'Campeonato']),
    'Mandante': ([], ['Time', 'Jogo']),
    'Visitante': ([], ['Time', 'Jogo']),
    'Classificacao': (['pontos', 'vitorias', 'empates', 'derrotas', 'saldo_gols', 'gols_pro', 'gols_contra'], ['Time', 'Campeonato'])
}

for rel, (attrs, ents) in relacionamentos.items():
    attr_text = ''.join(f'<TR><TD>{a}</TD></TR>' for a in attrs)
    mer.node(rel, label=f'''<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">
        <TR><TD BGCOLOR="lightgray"><B>{rel}</B></TD></TR>
        {attr_text}
    </TABLE>>''', shape='plaintext')
    for ent in ents:
        mer.edge(rel, ent)

# Gerar imagem
mer.render('mer_campeonato_futebol', cleanup=True)
