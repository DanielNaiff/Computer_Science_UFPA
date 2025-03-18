:-dynamic mulher/1.
:-dynamic homem/1.
:-dynamic genitor/2.

start():- write('Digite o valor de x: '), nl,
    read(X),nl,
    write(X),nl.

mulher(pam).
mulher(ann).
mulher(liz).
mulher(pat).
homem(tom).
homem(bob).
homem(jim).
genitor(pam, bob).
genitor(tom, bob).
genitor(tom, liz).
genitor(bob, ann).

