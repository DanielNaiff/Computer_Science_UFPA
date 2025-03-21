:- dynamic vertice/1.
:- dynamic aresta/2.

vertice(garagem).
vertice(cozinha).
vertice(sala).
vertice(quartob).
vertice(banheiro).
vertice(quartoa).

aresta(garagem, cozinha).
aresta(cozinha, garagem).

aresta(cozinha, sala).
aresta(sala, cozinha).

aresta(sala, quartob).
aresta(quartob, sala).

aresta(quartob, banheiro).
aresta(banheiro, quartob).

aresta(sala, quartoa).
aresta(quartoa, sala).

obj(cama, quarto_a).
obj(fogao, quarto_a).
obj(chave, quarto_a).
obj(chave, quarto_a).
obj(chave, quarto_a).
obj(geladeira, sala).
obj(vaso, sala).
obj(chave, sala).
obj(armario, cozinha).
obj(sofa, cozinha).
obj(chave, cozinha).
obj(chuveiro, quarto_b).
obj(armario, quarto_b).
obj(chave, quarto_b).
obj(chave, quarto_b).
obj(chave, quarto_b).
obj(chave, banheiro).
obj(chave, banheiro).
obj(mesa, banheiro).
obj(tv, banheiro).
obj(carregador, garagem).
obj(cama, garagem).

pos(garagem).
armazem([]).
lanterna(acesa).
bateria(100).


add_vertice(V):- \+ vertice(V),
                 assert(vertice(V)),
                 format('Local inserido').
                 
add_vertice(V):- vertice(V),
                 format('Nao foi possivel adicionar local').
                 
add_aresta(A,B):- \+ aresta(A,B),
                   assert(aresta(A, B)),
                   assert(aresta(B, A)),
                   format('Aresta inserid').
                   
add_aresta(A,B):- aresta(A,B),
                   format('nao foi possivel inserir aresta').
                   
add_obj(O, L):- vertice(L),
                    assert(obj(O, L)),
                    format('Obejto inserido'), !.
                    
add_obj(O, L):- \+ vertice(L),
                    format('Nao foi possivel inerir onjeto'), !.
                    
inspecionar:- lanterna(acesa),
              energia(inspecionar),
              pos(Local),
              findAll(O, obj(O, Local), Objetos),
              format('Local do robo: ~w.~n'[Local]),
              format('Lista de objetos: ~w.~n', [Objetos]), !.
              
inspecionar:- lanterna(apagada),
              format('A lanterna esta apagada!'),!.
              
inspecionar:- bateria(N),
              N =< 0,
              format('A enerfia nao e suficiente!'),!.
              
energia(Acao):- Acao == inspecionar,
                bateria(N),
                N > 0,
                N1 is N -10,
                format('Energia diminuir de ~w para ~w.~n',[N, N1]).
                

