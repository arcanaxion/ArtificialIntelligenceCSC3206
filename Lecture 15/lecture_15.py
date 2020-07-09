from math import sqrt

class Data:
    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        self.p = p

def get_euclidean(a, b):
    x_dist = a.x - b.x
    y_dist = a.y - b.y
    return sqrt(x_dist**2 + y_dist**2)

def calc_RMSE(y, y_pred):
    sqr_err = 0
    for x in range(len(y)):
        sqr_err += (y[x].p - y_pred[x].p) ** 2
    return sqrt(sqr_err/len(y))

training_raw = [[0.13, 0.850, 0.050], [0.760, 0.260, 0.074],
[0.5, 0.450, 0.187], [0.650, 0.79, 0.012], [0.09, 0.03, 1.398],
[0.84, 0.43, 0.025], [0.76, 0, 0.101], [0.45, 0.72, 0.054],
[0.23, 0.95, 0.019], [0.9, 0.03, 0.035]]

test_raw = [[0.13, 0.85, 0.05], [0.76, 0.26, 0.074], 
[0.5, 0.45, 0.187], [0.65, 0.79, 0.012]]

training = []
for data in training_raw:
    training.append(Data(data[0], data[1], data[2]))

test = []
for data in test_raw:
    test.append(Data(data[0], data[1], data[2]))

test_pred = []

k = 3

for tester in test:
    classifier = []
    for trainer in training:
        classifier.append([trainer, get_euclidean(trainer, tester)])
    classifier.sort(key=lambda x: x[1])

    p = 0
    for i in range(k):
        p += classifier[i][0].p
    p /= k
    test_pred.append(Data(tester.x, tester.y, p))

print("Test:")
for x in test:
    print(x.__dict__, end=', ')

print()

print("Predicted test:")
for x in test_pred:
    print(x.__dict__, end=', ')

print()

print("RMSE: ", calc_RMSE(test, test_pred))
