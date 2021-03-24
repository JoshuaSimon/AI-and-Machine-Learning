/* 
Starte prolog in einer Shell mit "swipl".
Lade eine Datei auf demselben Verzeichnis mit "[filename]."
Datei ist die Dateiendung wegzulassen. Hier also "[verw1]."
*/

kind(otto,katrin,franz).
kind(maria,katrin,franz).
kind(eva,anna,otto).
kind(hans,anna,otto).
kind(isolde,anna,otto).
kind(klaus,maria,ottob).

kind(X,Z,Y) :- kind(X,Y,Z).

nachkomme(X,Y) :- kind(X,Y,Z).
nachkomme(X,Y) :- kind(X,U,V), nachkomme(U,Y).

% Anfragen
% ?- kind(eva,otto,anna).
% ?- nachkomme(X,Y).
% ?- nachkomme(klaus,Y).
% ?- nachkomme(klaus,katrin). % Führt zu einem endlos rekursiven aufruf, da Symmetrie nicht implementiert.