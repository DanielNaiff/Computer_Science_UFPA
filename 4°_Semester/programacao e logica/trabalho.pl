:- dynamic robo/2.
:- dynamic pessoa/3.
:- dynamic maca/1.
:- dynamic log/1.

%inicializando o robo

robo(hub, 100).
maca([]).

% Definindo os locais do ambiente
vertice(hub).
vertice(calcada).
vertice(cozinha, incendio).
vertice(quarto1).
vertice(quarto2).
vertice(banheiro).

% Definindo as arestas
aresta(calcada, hub).
aresta(hub, calcada).

aresta(hub, cozinha).
aresta(cozinha, hub).

aresta(hub, quarto1).
aresta(quarto1, hub).

aresta(hub, quarto2).
aresta(quarto2, hub).

aresta(banheiro, quarto1).
aresta(quarto1, banheiro).

% Definindo pessoas
pessoa(p1,hub,100).

pessoa(p2,hub,100).

pessoa(p3,cozinha,100).

pessoa(p4,quarto1,100).

pessoa(p5,quarto2,100).

pessoa(p6,banheiro,100).

%inspecionar
inspecionar:- robo(Local,_),
              findall(Pessoa-Oxigenio, pessoa(Pessoa, Local,Oxigenio), Pessoas),
              length(Pessoas, NumPessoas),
              NumPessoas >= 1,
              format('Voce esta em ~w e este local possui ~w pessoa(s).~n',[Local, NumPessoas]),
              exibir_oxigenacao(Pessoas),
              registrar_acoes(inspecionar),!.
              
exibir_oxigenacao([]).

exibir_oxigenacao([Pessoa-Oxigenio| Resto]):- format('Pessoa: ~w - Oxigênio: ~w.~n',[Pessoa, Oxigenio]),
                                              exibir_oxigenacao(Resto),!.
              
%pegar pessoa
pegar(P):- robo(Local,_),
           pessoa(P, Local, O),
           maca([]),
           retract(pessoa(P, Local, O)),
           assert(pessoa(P, maca, O)),
           retract(maca([])),
           assert(maca([P])),
           format('Pegou a pessoa ~w do local ~w.~n', [P,Local]).
           registrar_acoes(pegar),!.
           
pegar(P):- maca(Pessoas),
           length(Pessoas, N),
           N >= 1,
           format('A maca ja possui uma pessoa').
           registrar_acoes(pegar),!.

pegar(P): format('A pessoa ~w nao esta no local',[P]),!.
           
soltar(P):- maca([P]),
            robo(Local,_),
            pessoa(P, maca, _),
            retract(maca([P])),
            assert(maca([])),
            retract(pessoa(P, maca,_)),
            assert(pessoa(P, Local, _)),
            format('voce soltou a pessao ~w no local ~w.~n', [P, Local]),
            registrar_acoes(soltar),!.

soltar(P):- format('A pessoa ~w nao esta na maca',[P]),!.

            

%logs
registrar_acoes(Acao):- assert(log(Acao)),
                        format('Acao registrada ~w.~n',[Acao]).
                          
log:- findall(Acao, log(Acao), Acoes),
      length(Acoes, N),
      N == 0,
      format('Nao ha nenhuma acao para mostrar').
      
log:- findall(Acao, log(Acao), Acoes),
      length(Acoes, N),
      N > 0,
      listar_acoes(Acoes).

listar_acoes([]).
listar_acoes([Acao| Restante]):- format(' - ~w~n',[Acao]),
                                 listar_acoes(Restante).

