from math import sqrt

class Data:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

def get_euclidean(a, b):
    x_dist = a.x - b.x
    y_dist = a.y - b.y
    return sqrt(x_dist**2 + y_dist**2)

training_raw = [[1.29, 1.45, 'a'], [0.07, -0.76, 'a'], [-1.09, 0.03, 'a'],
[-1.02, -1.44, 'a'], [0.9, 0.63, 'b'], [1.59, -0.41, 'b'],
[0.51, 0.44, 'b'], [-2.51, 1.04, 'b'], [0.64, 5.78, 'c'],
[0.41, 0.71, 'c'], [2.47, 1.4, 'c'], [1.82, 0.27, 'c']]

test_raw = [[0.09, 1.25, 'a'], [-0.93, 0.99, 'a'], [-0.02, 0.24, 'b'],
[4.3, 0.66, 'b'], [-0.09, 2.46, 'c'], [2.25, 0.94, 'c']]

training = []
for data in training_raw:
    training.append(Data(data[0], data[1], data[2]))

test = []
for data in test_raw:
    test.append(Data(data[0], data[1], data[2]))

test_pred = []

k = 5

for tester in test:
    classifier = []
    for trainer in training:
        classifier.append([trainer, get_euclidean(trainer, tester)])
    classifier.sort(key=lambda x: x[1])
    
    total_a, total_b, total_c = (0,0,0)
    for x in range(k):
        if classifier[x][0].c == 'a':
            total_a += 1
        elif classifier[x][0].c == 'b':
            total_b += 1
        elif classifier[x][0].c == 'c':
            total_c += 1

    # prefer in order of a, b, c if draw
    if total_a >= total_b and total_a >= total_c:
        test_pred.append(Data(tester.x, tester.y, 'a'))
    elif total_b >= total_a and total_b >= total_c:
        test_pred.append(Data(tester.x, tester.y, 'b'))
    elif total_c > total_b and total_c > total_a:
        test_pred.append(Data(tester.x, tester.y, 'c'))

print("Test:")
for x in test:
    print(x.__dict__, end=', ')

print()

print("Predicted test:")
for x in test_pred:
    print(x.__dict__, end=', ')