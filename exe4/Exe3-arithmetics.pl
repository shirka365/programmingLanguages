%Exe3
%Shir Kanner 214677213
%Shira Alkobi 326415353

scum(1,1).
scum(N, Res) :-
    N > 1,
    N1 is N - 1,
    scum(N1, Temp),
    Res is Temp + N.

sumDigits(0,0).
sumDigits(Num, Sum):-
    Num > 0,
    Num1 is Num//10,
    sumDigits(Num1, Temp),
    D is Num mod 10,
    Sum is Temp + D.

%-----------------------------------------------------
split(0, []).
split(N, Res):-
    N > 0,
    N1 is N // 10,
    D is N mod 10,
    split(N1, R1),
    append(R1,[D],Res).

create([], 0).
create([X|Rest], N):-
    create(Rest, Temp),
    N is X + Temp * 10.

reverse_num(N,N_rev):-
    split(N,N_List),
    create(N_List, N_rev).

%-----------------------------------------------------
intersection([], _, []).
intersection([X|Y], L2, [X|Z]) :-
    member(X, L2),
    intersection(Y, L2, Z).
intersection([X|Y], L2, Z) :-
    \+ member(X, L2),
    intersection(Y, L2, Z).

minus([], _, []).
minus([X|Y], L2, Z) :-
    member(X, L2),
    minus(Y, L2, Z).
minus([X|Y], L2, [X|Z]) :-
    \+ member(X, L2),
    minus(Y, L2, Z).


    


    