def neural_network(inp, weights) -> list:
    prediction_h: list = [0] * len(weights[0])
    for i in range(len(weights[0])):
        ws: float = 0
        for j in range(len(inp)):
            ws += inp[j] * weights[0][i][j]
        prediction_h[i] = ws

    prediction_out: list = [0] * len(weights[1])
    for i in range(len(weights[1])):
        ws: float = 0
        for j in range(len(prediction_h)):
            ws += prediction_h[j] * weights[1][i][j]
        prediction_out[i] = ws

    return prediction_out


inp: list = [50, 165]
weights_h_1: list = [.2, .1]
weights_h_2: list = [.3, .1]

weights_out_1: list = [.4, .2]
weights_out_2: list = [.5, .3]

weights_h: list = [weights_h_1, weights_h_2]
weights_out: list = [weights_out_1, weights_out_2]

weights: list = [weights_h, weights_out]

print(neural_network(inp, weights))
