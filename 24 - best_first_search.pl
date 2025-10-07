% -----------------------------
% GRAPH AND HEURISTICS
% -----------------------------

% edge(Node1, Node2, Cost)
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 4).
edge(b, e, 2).
edge(c, f, 5).
edge(d, goal, 0).
edge(e, goal, 0).
edge(f, goal, 0).

% heuristic(Node, HValue)  (estimated cost to goal)
heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 2).
heuristic(d, 1).
heuristic(e, 1).
heuristic(f, 0).
heuristic(goal, 0).

% -----------------------------
% BEST-FIRST SEARCH
% -----------------------------
best_first_search(Start, Goal, Path) :-
    heuristic(Start, H),
    bfs([[Start, H]], Goal, RevPath),
    reverse(RevPath, Path).

% BFS Helper
bfs([[Goal, _]|_], Goal, [Goal]).
bfs([[Node, _]|RestQueue], Goal, [Node|Path]) :-
    findall([Next, H], (edge(Node, Next, _), heuristic(Next, H)), Children),
    sort(2, @=<, Children, SortedChildren),       % sort by heuristic
    append(SortedChildren, RestQueue, NewQueue),
    bfs(NewQueue, Goal, Path).
