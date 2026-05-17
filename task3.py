% ─── Facts: parent(Parent, Child) ───────────────────────────────────────────
% Grandparent generation
parent(robert, david).
parent(victoria, emily).
parent(helen, david).
parent(helen, emily).

% Parent generation
parent(david, mark).
parent(david, laura).
parent(catherine, mark).
parent(catherine, laura).
parent(emily, paul).
parent(emily, olivia).
parent(michael, paul).
parent(michael, olivia).

% Child (grandchild) generation
parent(mark, thomas).
parent(mark, sarah).
parent(laura, benjamin).

% Gender facts
male(robert). male(david). male(michael).
male(mark). male(paul). male(thomas). male(benjamin).
female(victoria). female(helen). female(emily).
female(catherine). female(laura). female(olivia). female(sarah).

% ─── Rules ───────────────────────────────────────────────────────────────────
grandparent(GP, GC) :- parent(GP, P), parent(P, GC).
grandchild(GC, GP)  :- grandparent(GP, GC).

father(F, C) :- parent(F, C), male(F).
mother(M, C) :- parent(M, C), female(M).

sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y)  :- sibling(X, Y), female(X).

uncle(U, N) :- brother(U, P), parent(P, N).
aunt(A, N)  :- sister(A, P), parent(P, N).

cousin(X, Y) :- parent(PX, X), parent(PY, Y), sibling(PX, PY).

ancestor(A, D) :- parent(A, D).
ancestor(A, D) :- parent(A, X), ancestor(X, D).

% ─── Example queries (run in SWI-Prolog) ─────────────────────────────────────
% ?- grandparent(robert, mark).      % true
% ?- grandchild(thomas, david).      % true
% ?- uncle(U, paul).                 % U = mark
% ?- cousin(mark, paul).             % true
% ?- findall(C, parent(david, C), L). % L = [mark, laura]