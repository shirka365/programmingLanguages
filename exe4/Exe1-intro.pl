%Exe1
%Shir Kanner 214677213
%Shira Alkobi 326415353

female(phoebe).
female(shlomit).
female(shira).
female(noa).
female(naama).
female(eti).
female(dana).

male(shimon).
male(shlomo).
male(ron).
male(shay).
male(yehonatan).
male(david).

%assumption - the male is first in the predicate
married(shimon, phoebe).
married(shlomo, shlomit).
married(shay, eti).
married(david, noa).

parent(phoebe, shlomit).
parent(shimon, shlomit).
parent(phoebe, eti).
parent(shimon, eti).
parent(shlomit, shira).
parent(shlomo, shira).
parent(shlomit, ron).
parent(shlomo, ron).
parent(shlomit, noa).
parent(shlomo, noa).
parent(ron, naama).
parent(eti, yehonatan).
parent(shay, yehonatan).
parent(yehonatan, dana).


father(X,Y):- parent(X,Y), male(X).

mother(X,Y):- parent(X,Y), female(X).

son(X,Y):- parent(Y,X), male(X).

daughter(X,Y):- parent(Y,X), female(X).

grandfather(X,Y):- parent(X,Z), parent(Z,Y), male(X).

grandmother(X,Y):- parent(X,Z), parent(Z,Y), female(X).

grandson(X,Y):- parent(Y,Z), parent(Z,X), male(X).

granddaughter(X,Y):- parent(Y,Z), parent(Z,X), female(X).

sibling(X,Y):- parent(Z,X), parent(Z,Y), X\=Y.

non_blood_uncle(X,Y):- 
    male(X), 
    parent(Z,Y), 
    sibling(Z,W),
    married(X,W).

son_of_aunt(X,Y):-
    male(X),
    female(Z),
    parent(Z,X),
    parent(W,Y),
    sibling(Z,W).

brother_in_law(X,Y):-
    male(X),
    married(X,Z),
    sibling(Z,Y).

niece(X,Y):-
    female(X),
    parent(Z,X),
    sibling(Z,Y).

cousin(X,Y):-
    parent(Z,X),
    parent(W,Y),
    sibling(Z,W).

second_cousin(X,Y):-
    parent(Z,X),
    parent(W,Y),
    cousin(Z,W).
