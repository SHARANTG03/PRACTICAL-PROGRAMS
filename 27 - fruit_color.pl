% Facts: fruit(FruitName, Color)
fruit(apple, red).
fruit(banana, yellow).
fruit(grapes, green).
fruit(grapes, purple).
fruit(orange, orange).
fruit(mango, yellow).
fruit(cherry, red).
fruit(blueberry, blue).

% Rule to find fruits of a particular color
fruits_of_color(Color, Fruit) :-
    fruit(Fruit, Color).

% Rule to find colors of a particular fruit
colors_of_fruit(Fruit, Color) :-
    fruit(Fruit, Color).
