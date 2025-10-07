% BIRD FLY PROGRAM
% Fact format: bird(Name, can_fly_or_not).

bird(sparrow, can_fly).
bird(eagle, can_fly).
bird(parrot, can_fly).
bird(penguin, cannot_fly).
bird(ostrich, cannot_fly).
bird(crow, can_fly).
bird(duck, can_fly).

% Rule to check if a bird can fly
can_fly(Bird) :-
    bird(Bird, can_fly),
    write(Bird), write(' can fly.'), nl.

% Rule to check if a bird cannot fly
cannot_fly(Bird) :-
    bird(Bird, cannot_fly),
    write(Bird), write(' cannot fly.'), nl.
