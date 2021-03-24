% Findet das Maximum aus zwei Zahlen. Optimiert mit
% Cut-Operator "!", um unnötiges Backtracking zu
% vermeiden.

max(X,Y,X) :- X >= Y, !.
max(X,Y,X).

% Anfrage
?- max(3,2,Z), Z > 10.