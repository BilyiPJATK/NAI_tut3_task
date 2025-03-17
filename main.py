learning_rate=0.01
epochs=1000
weights = []
bias = 0

def predict(x):
    weighted_sum = sum(w * xi for w, xi in zip(weights, x)) + bias
    return 1 if weighted_sum >= 0 else 0


def updateWeightsAndBias(x, y):
    global weights, bias

    error = y - predict(x)

    for i in range(len(weights)):
        weights[i] += learning_rate * error * x[i]
    bias += learning_rate * error



updateWeightsAndBias([0.5, -0.5], 0.1)

x = [1, 2]
prediction = predict(x)
print("Prediction:", prediction)