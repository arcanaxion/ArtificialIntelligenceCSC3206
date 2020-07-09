from sklearn.model_selection import train_test_split
from sklearn import datasets
import pandas as pd
import sys
from matplotlib import pyplot as plt

def model(x, m, c):
    return m*x + c

def cost(y, yh):
    return sum((y-yh)**2)/y.size

def derivatives(x, y, yh):
    n = x.size
    deriv_m = (-2/n) * sum(x * (y - yh))
    deriv_c = (-2/n) * sum((y - yh))

    return {'m': deriv_m, 'c': deriv_c}

diabetes = datasets.load_diabetes()

pt = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = pd.DataFrame(diabetes.target, columns=['target'])

X_train, X_test, y_train, y_test = train_test_split(pt, y)

learningrate = 0.1
m = []
c = []
J = []
m.append(0)
c.append(0)

J.append(cost(y_train['target'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))))

J_min = 0.01
del_J_min = 0.0001
max_iter = 10000

plt.scatter(X_train['bmi'], y_train['target'], color='red')
plt.title('Training data')
plt.xlabel('BMI')
line = None

for n in range(max_iter):
    yh = X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))
    deriv = derivatives(X_train['bmi'], y_train['target'], yh)
    m.append(m[-1] - learningrate * deriv['m'])
    c.append(c[-1] - learningrate * deriv['c'])
    J_val = cost(y_train['target'], yh)
    J.append(J_val)

    if J_val <= J_min:
        break
    print('.', end='')
    sys.stdout.flush()

    if line:
        line[0].remove()
    line = plt.plot(X_train['bmi'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1])), '-', color='green')
    plt.pause(0.001)

y_train_pred = X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))
y_test_pred = X_test['bmi'].apply(lambda x: model(x, m[-1], c[-1]))
print('\nAlgorithm terminated with')
print(f'  {len(J)} iterations,')
print(f'  m {m[-1]}')
print(f'  c {c[-1]}')
print(f'  training cost {J[-1]}')
testcost = cost(y_test['target'], y_test_pred)
print(f'  testing cost {testcost}')

plt.figure()
plt.scatter(X_test['bmi'], y_test['target'], color='red')
plt.plot(X_test['bmi'], \
         X_test['bmi'].apply(lambda x: model(x, m[-1], c[-1])), \
         '-', color='green')
plt.title('Testing data')
plt.show()