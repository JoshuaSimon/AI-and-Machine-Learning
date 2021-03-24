% Liste mit Head (erstes Elemente) und Tail (Rest).
liste([A,2,2,B,3,4,5]).
?- liste([H|T]).

% Baumstrukturen (geschachtelte Listen).
liste([a, [b,e,f,g], [c,h], d]).

% Programm zum Anhängen von Listen.
append([],L,L).
append([X|L1],L2,[X|L3]) :- append(L1,L2,L3).
?- append([a,b,c],[d,1,2],Z).
?- append(X,[1,2,3],[4,5,6,1,2,3]).

% Programm zum Umkehren der Elemente in einer Liste (naive).
nrev([],[]).
nrev([H|T], R) :- nrev(T,RT), append(RT,[H],R).

% Programm zum Umkehren der Elemente in einer Liste (besser).
accrev([],A,A).
accrev([H|T],A,R) :- accrev(T,[H|A],R).