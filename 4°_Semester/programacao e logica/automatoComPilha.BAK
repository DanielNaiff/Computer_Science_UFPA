% Definição das transições do autômato de pilha (PDA)
q(1, 'e', 'e', '$', 2).   % Transição de 1 para 2 com a pilha '$'
q(2, '0', 'e', '0', 2).   % Transição de 2 para 2, empilhando '0'
q(2, '1', '0', 'e', 3).   % Transição de 2 para 3, substituindo '0' por 'e'
q(3, '1', '0', 'e', 3).   % Transição de 3 para 3, substituindo '0' por 'e'
q(3, 'e', '$', 'e', 4).   % Transição de 3 para 4, desempilhando '$'

% Definição do estado inicial
inicio(1).

% Definição do estado final
final(4).

% Predicado principal para testar uma entrada X
teste(X) :-
    string_chars(X, Fita),          % Converte a entrada em lista de caracteres
    inicio(No),                     % Estado inicial
    reconhecedor(No, Fita, []), !.  % Inicia o reconhecimento com a pilha vazia

% Caso base: reconhecimento bem-sucedido quando a fita está vazia
reconhecedor(No, [], []) :-
    final(No),  % Aceita a entrada se o estado final for alcançado
    !.

% Transição com a fita vazia e manipulação da pilha
reconhecedor(De, [], Pilha) :-
    q(De, 'e', L, E, Para),         % Busca transição e
    atualiza_pilha(Pilha, L, E, Nova_Pilha),  % Atualiza a pilha
    reconhecedor(Para, [], Nova_Pilha).  % Continua o reconhecimento no próximo estado

% Transição normal: consome um símbolo da fita
reconhecedor(De, Fita, Pilha) :-
    q(De, X, L, E, Para),            % Busca uma transição com um símbolo da fita
    X \== 'e',                       % Verifica se a transição não é e
    caminha(X, Fita, Nova_Fita),     % Consome o símbolo da fita
    atualiza_pilha(Pilha, L, E, Nova_Pilha),  % Atualiza a pilha
    reconhecedor(Para, Nova_Fita, Nova_Pilha).  % Continua o reconhecimento

% Transição com a fita vazia, mas a pilha é atualizada
reconhecedor(De, Fita, Pilha) :-
    q(De, 'e', L, E, Para),          % Transição e
    atualiza_pilha(Pilha, L, E, Nova_Pilha),  % Atualiza a pilha
    reconhecedor(Para, Fita, Nova_Pilha).  % Continua o reconhecimento com a fita

% Consome um símbolo da fita
caminha(H, [H | T], T).  % Se o símbolo atual da fita for H, consome o primeiro símbolo

% Atualiza a pilha: primeiro manipula a leitura, depois a escrita
atualiza_pilha(Pilha, L, D, Nova_Pilha) :-
    atualiza_leitura(Pilha, L, P1),     % Atualiza a leitura da pilha
    atualiza_escrita(P1, D, Nova_Pilha).  % Atualiza a escrita da pilha

% Atualiza a leitura da pilha
atualiza_leitura([L | Pilha], L, Pilha).  % Se o topo da pilha é L, apenas remove
atualiza_leitura(Pilha, 'e', Pilha).      % Caso contrário, mantém a pilha inalterada

% Atualiza a escrita da pilha
atualiza_escrita(Pilha, E, [E | Pilha]) :- E \== 'e', !.  % Empilha E se E não for 'e'
atualiza_escrita(Pilha, 'e', Pilha).      % Caso contrário, a pilha permanece igual

