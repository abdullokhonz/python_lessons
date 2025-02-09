def neural_network(inp, weights) -> list:
    prediction: list = [0, 0]
    for i in range(len(weights)):
        prediction[i] += inp * weights[i]
    return prediction


print(neural_network(.65, [.2, .1]))
