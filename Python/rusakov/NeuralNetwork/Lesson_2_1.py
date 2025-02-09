def neural_network(inp, weight) -> float:
    prediction: float = inp * weight
    return prediction


out_1: float = neural_network(150, .2)
out_2: float = neural_network(160, .2)

print(out_1)
print(out_2)
