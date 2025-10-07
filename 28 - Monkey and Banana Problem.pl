% Monkey and Banana Problem
% States: state(MonkeyPos, BoxPos, BananaPos, MonkeyHasBanana)
% Positions can be: door, window, middle

% Initial state
initial(state(door, window, middle, no)).

% Goal state
goal(state(_, _, _, yes)).

% Action: monkey moves from one position to another
action(state(MPos, BPos, BanPos, Has), move(NewPos), state(NewPos, BPos, BanPos, Has)) :-
    MPos \= NewPos.

% Action: monkey pushes the box
action(state(MPos, MPos, BanPos, Has), push(NewBoxPos), state(NewBoxPos, NewBoxPos, BanPos, Has)) :-
    MPos \= NewBoxPos.

% Action: monkey climbs the box to get banana
action(state(Pos, Pos, Pos, no), climb, state(Pos, Pos, Pos, yes)).

% Solve function using depth-first search
solve(State, []) :-
    goal(State).
solve(State, [Action|Rest]) :-
    action(State, Action, NewState),
    solve(NewState, Rest).
