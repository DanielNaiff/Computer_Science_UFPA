:- dynamic vertice/1.
:- dynamic aresta/2.
:- dynamic obj/2.
:- dynamic energia/1.
:- dynamic log/1.
:- dynamic mochila/1.
:- dynamic lanterna/1.

%iniciando o robo
pos(garagem).
energia(100).
lanterna(apagada).
mochila([]).

%definindo locais
vertice(garagem).
vertice(cozinha).
vertice(sala).
vertice(quartob).
vertice(quartoa).
vertice(banheiro).

%defininco as arestas.
aresta(garagem, cozinha).
aresta(cozinha, garagem).

aresta(cozinha, sala).
aresta(sala, cozinha).

aresta(sala, quartoa).
aresta(quartoa, sala).

aresta(sala, quartob).
aresta(quartob, sala).

aresta(quartob, banheiro).
aresta(banheiro, quartob).

%definindo
obj(carregador, garagem).
obj(cama, garagem).

obj(sofa, cozinha).
obj(chave, cozinha).
obj(armario, cozinha).

obj(chave, sala).
obj(vaso, sala).
obj(geladeira, sala).

obj(chave, quartob).
obj(chave, quartob).
obj(chave, quartob).
obj(chuveiro, quartob).
obj(armario, quartob).

obj(chave, banheiro).
obj(chave, banheiro).
obj(mesa, banheiro).
obj(tv, banheiro).

obj(chave, quartoa).
obj(chave, quartoa).
obj(chave, quartoa).
obj(fogao, quartoa).
obj(cama, quartoa).

% Adicionar vertice
add_vertice(V):-
               \+ vertice(V),
               assert(vertice(V)),
               format('Veritice ~w adicionado com sucesso.~n', [V]).
add_vertice(V):-
                vertice(V),
                format('O vertice ja existe.~n', [V]).
                
%Adcionar aresta
add_aresta(X, Y):-
              \+ aresta(X, Y),
              assert(aresta(X,Y)),
              assert(aresta(Y,X)),
              format('Aresta foi adicionada com sucesso.~n', [X,Y]).
              
add_aresta(X,Y):-
                 aresta(X,Y),
                 format('Aresta de ~w a ~w ja existe.~n', [X,Y]).
                 
%Adcionar objeto
add_obj(O,L) :-
             vertice(L),
             assert(obj(O,L)),
             format('Objeto ~w adicionado ao local ~w.~n', [O,L]).
             
add_obj(O,L):-
              \+ vertice(L),
              obj(O,L),
              format('Local ~w nao existe. ~n', [L]).
                 
%Inspecionar
inspecionar :-
            lanterna(acesa),
            pos(Local),
            findall(O, obj(O,Local), Objetos),
            format('Voce esta em ~w. Objetos: ~w. ~n ~n ~n', [Local, Objetos]),
            energia(E),
            E1 is E - 10,
            retract(energia(E)),
            format('Energia de ~w para ~w.~n', [E, E1]),
            assert(energia(E1)),
            acao_inspecionar(E1).
            registrar(inspecionar).

inspecionar :- format('A lanterna esta apagda! nao e possivel inspecionar.~n').
            
acao_inspecionar(E1) :-
                     E1 =< 0,
                     format('Energia esgotada! Não pode mais atuar no ambiente.~n'),


acao_inspecionar(E1) :-
                     E1 > 0.

                     
%Pegar objeto
pegar(O):-
          pos(Local),
          obj(O, Local),
          mochila(Mochila),
          length(Mochila, N),
          inspecionar_mochila(N,Mochila, Local,O),
          registrar_log(pegar(O)).

inspecionar_mochila(N,Mochila, Local,O):- N < 2,
                        \+member(O, Mochila),
                         retract(obj(O,Local)),
                         asserta(mochila([O, Mochila])),
                         format('Pegou o objeto ~w no local ~w. ~n', [O, Local]),
                         energia(E),
                         E1 is E - 5,
                         retract(energia(E)),
                         assertz(energia(E1)),
                         format('Energia de ~w para ~w.~n', [E, E1]),
                         acao_inspecionar(E1),
                         format('Não pode pegar o objeto ~w. Mochila cheia ou objeto repetido.~n', [O])),
                          registrar_log(pegar(O)),
                          !.
inspecionar_mochila(N):- N => 2,
                        format('Não pode pegar o objeto ~w. Mochila cheia ou objeto repetido.~n', [O])),
                        registrar_log(pegar(O)),!.
                        
% Soltar objeto
soltar(O):-
           mochila(Mochila),
           member(O, Mochila),
           pos(Local),
           select(O, Mochila, NovaMochila),
           retract(mochila(Mochila)),
           assert(mochila(NovaMochila))
           assert(obj(O, Local)),
           format('Soltou o objeto ~w no local ~w.~n', [O,Local]),
           energia(E),
           E1 is E - 5,
           retract(energia(E)),
           assert(energia(E)),
           acao_inspecionar(E1)
           regitrar_log(soltar(O)), !.
soltar(O) :-
    format('Objeto ~w não está na mochila.~n', [O]).
    
%Acao lanterna
ligar_lanterna:- \+ lanterna(acesa),
                 retract(lanterna(apagada)),
                 assert(lanterna(acesa)),
                 format('Lanterna ligada.~n').
                 registrar_log(ligar_lanterna),!.

ligar_lanterna:- format('Lanterna ja esta ligada!.~n').
                 registrar_log(ligar_lanterna),!.
                 
desligar_lanterna:- \+ lanterna(apagada),
                 retract(lanterna(acesa)),
                 assert(lanterna(apagada)),
                 format('Lanterna desligada.~n').
                 registrar_log(desligar_lanterna),!.

desligar_lanterna:- format('Lanterna ja esta desligada!.~n').
                 registrar_log(desligar_lanterna),!.
                 
%mochila
mochila:-
         mochila(Mochila),
         \+lista_vazia(Mochila),
         format('Objetos na mochila: ~w.~n', [Mochila]).
         registrar_log(mochila).

mochila:-
         mochila(Mochila),
         lista_vazia(Mochila),
        format('A mochila está vazia.~n')
         registrar_log(mochila).
         
lista_vazia([]).

%caminhar
caminha(Destino):-
                  pos(Origem),
                  aresta(Origem, Destino),
                  lanterna(apagada),
                  energia(E),
                  E > 0,
                  E1 is E - 5,
                  retract(energia(E)),
                  assert(energia(E1)),
                  retract(pos(Origem)),
                  assert(pos(Destino)),
                  format('O robô caminhou de ~w para ~w.~n', [Origem, Destino]),
                  registrar_log(caminhar(Destino)),!.


caminha(Destino):-
                  pos(Origem),
                  aresta(Origem, Destino),
                  lanterna(acesa),
                  energia(E),
                  E > 0,
                  E1 is E - 10,
                  retract(energia(E)),
                  assert(energia(E1)),
                  retract(pos(Origem)),
                  assert(pos(Destino)),
                  format('O robô caminhou de ~w para ~w.~n', [Origem, Destino]),
                  registrar_log(caminhar(Destino)),!.

caminha(Destino):-
                  energia(E),
                  E < 0,
                  format('Não é possível caminhar para ~w , pois o robo esta sem energia.~n', Destino).
                  registrar_log(caminhar(Destino)),!.
caminhar(Destino) :-
    format('Não é possível caminhar para ~w.~n', Destino).
    
%carregar

carrega:-
         pos(Local),
         obj(carregador, Local),
         retract(energia(_)),
         assert(energia(100)),
         format('Robô carregado para 100%.~n'),
         registrar_log(carregar),!.
carregar :-
    format('Não há carregador no local onde o robô está.~n').
    

status_robo :-
    pos(Local),
    energia(E),
    lanterna(L),
    mochila(Mochila),
    length(Mochila, N),
    format('Robô está em ~w, lanterna: ~w, energia: ~w, ~n Qtd objetos na mochila: ~w.~n ~n', [Local, L, E, N]),
    !.
    
%log
log:-
     findall(Acao, log(Acao), Acoes),
     lista_acoes(Acoes).
     
lista_acoes([]).
listar_acoes([Acao|Restante]):-
                               format(' - ~w~n', [Acao]),
                                listar_acoes(Restante).

         
                     
% Registar log de ações
registrar_log(Acao):-
                     assert(log(Acao)),
                     format('Acao registrada: ~w. ~n ~n', [Acao]).
               

