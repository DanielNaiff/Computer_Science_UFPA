 inicio(q0).
 final(q2).
 p(q0,a,q0).
 p(q0,e,q1).
 p(q1,b,q1).
 p(q1,e,q2).
 p(q2,a,q2).
 
 teste(X) :- string_chars(X, Fita),
    inicio(No),
    reconhecedor(No, Fita), !.
    
 reconhecedor(No,[]) :- final(No), !.
 
 reconhecedor(De,[]) :-   p(De, e, Para),
                        reconhecedor(Para, []).
        
 reconhecedor(De,Fita) :- (p(De, X, Para); p(De, e, Para)),
        caminha(X, Fita, Nova_Fita),
        reconhecedor(Para, Nova_Fita).
        
 caminha(H,[H | T],T).
