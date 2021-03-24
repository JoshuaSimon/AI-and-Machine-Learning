kind_fakt(otto,katrin,franz).
kind_fakt(maria,katrin,franz).
kind_fakt(eva,anna,otto).
kind_fakt(hans,anna,otto).
kind_fakt(isolde,anna,otto).
kind_fakt(klaus,maria,ottob).

kind(X,Z,Y) :- kind_fakt(X,Y,Z).
kind(X,Z,Y) :- kind_fakt(X,Z,Y).

nachkomme(X,Y) :- kind_fakt(X,Y,Z).
nachkomme(X,Y) :- kind(X,U,V), nachkomme(U,Y).

% Anfragen
% ?- kind(eva,otto,anna).
% ?- nachkomme(klaus,katrin). % Nun kein Fehler durch endlose rekursive Aufrufe.

% List mit den Kindern und ihren Eltern.
?- kind_fakt(X,Y,Z), write(X), write(' ist Kind von '), write(Y), 
write(' und '), write(Z), write('.'), nl, fail.