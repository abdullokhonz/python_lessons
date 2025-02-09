def neural_network(inp, weights) -> float:
    prediction: float = 0
    for i in range(len(inp)):
        prediction += inp[i] * weights[i]
    return prediction


out_1: float = neural_network([150, 40], [.2, .3])
out_2: float = neural_network([160, 70], [.2, .3])

print(out_1)
print(out_2)
