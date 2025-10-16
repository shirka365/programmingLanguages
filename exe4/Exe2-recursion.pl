%Exe2
%Shir Kanner 214677213
%Shira Alkobi 326415353

reverse([],[]).
reverse([X|Y], Z) :- reverse(Y, R), append(R, [X], Z).

%-----------------------------------------------------
member(X,L):- append(_, [X|_], L).

%-----------------------------------------------------
palindrome(L):-reverse(L,L).

%-----------------------------------------------------
sorted([]).
sorted([_]).
sorted([X|[Y|Z]]):-
    X=<Y,
    sorted([Y|Z]).

%-----------------------------------------------------
permutation([], []).
permutation(L, [X|P]) :-
    append(W, [X|Y], L),
    append(W, Y, L1),
    permutation(L1, P).


