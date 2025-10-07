% -----------------------------
% Facts: define vowels
% -----------------------------
vowel(a). vowel(e). vowel(i). vowel(o). vowel(u).
vowel(A) :- char_type(A, upper), char_lower(A, L), vowel(L).

% -----------------------------
% Rule: count vowels in a list of characters
% -----------------------------
count_vowels([], 0).
count_vowels([H|T], Count) :-
    vowel(H),                     % if H is a vowel
    count_vowels(T, Rest),
    Count is Rest + 1.
count_vowels([H|T], Count) :-
    \+ vowel(H),                  % if H is not a vowel
    count_vowels(T, Count).

% -----------------------------
% Helper: convert string to list of characters and count vowels
% -----------------------------
vowel_count(String, Count) :-
    string_chars(String, CharList),
    count_vowels(CharList, Count).
