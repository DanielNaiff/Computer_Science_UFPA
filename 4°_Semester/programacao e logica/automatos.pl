inicio(q0).
final(q2).
p(q0, 'a', q1).
p(q1, 'a', q1).
p(q1, 'b', q1).
p(q1, 'b', q2).

teste(X): string_chars(X, Fita),
          inicio(No),
          reconhecedor(No, Fita).
          
reconhecedor(No, []):- final(No), !.

reconhecedor(De, []):- p(De,E,Para),
                       reconhecedor(Para, []).
                       
reconhecedor(No, Fita):- (p(De, X, Para); p(De, E, Para)),
                         caminhar(X, Fita, Nova_Fita),
                         reconhecedor(Para, Nova_Fita).
                         
caminha(H, [H|T], T).
