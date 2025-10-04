import math
def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    if isinstance(node, int):
        return node
    if maximizingPlayer:  
        maxEval = -math.inf
        for child in node:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:  
                break
        return maxEval
    else:  
        minEval = math.inf
        for child in node:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:  
                break
        return minEval
game_tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]]
]
best_value = alpha_beta(game_tree, depth=3, alpha=-math.inf, beta=math.inf, maximizingPlayer=True)
print("MAX VAL :", best_value)