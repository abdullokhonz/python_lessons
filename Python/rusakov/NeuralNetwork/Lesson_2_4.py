def neural_network(inp, weights) -> list:
    prediction: list = [0] * len(weights)
    for i in range(len(weights)):
        ws: float = 0
        for j in range(len(inp)):
            ws += inp[j] * weights[i][j]
        prediction[i] = ws
    return prediction


inp: list = [50, 165, 10]

weights_1: list = [.2, .1, .05]
weights_2: list = [.3, .1, .05]
weights_3: list = [.5, .1, .05]

weights: list = [weights_1, weights_2, weights_3]
print(neural_network(inp, weights))
