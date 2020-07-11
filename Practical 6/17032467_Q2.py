from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
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

X_train, X_test, y_train, y_test = train_test_split(pt, y, test_size=0.2, random_state=1)
regrmodel = linear_model.LinearRegression()
regrmodel.fit(X_train[['bmi']], y_train['target'])
y_train_pred = regrmodel.predict(X_train[['bmi']])
y_test_pred = regrmodel.predict(X_test[['bmi']])

y_train_pred = pd.Series(y_train_pred)
y_train_pred.index = y_train.index

y_test_pred = pd.Series(y_test_pred)
y_test_pred.index = y_test.index

print('sklearn')
print(f'  m {regrmodel.coef_}')
print(f'  c {regrmodel.intercept_}')
traincost = cost(y_train['target'], y_train_pred)
testcost = cost(y_test['target'], y_test_pred)
print(f'  training cost: {traincost}')
print(f'  testing cost: {testcost}')

plt.figure()
plt.scatter(X_train['bmi'], y_train['target'], color='red')
plt.plot(X_train['bmi'], y_train_pred, '-', color='green')
plt.title('Training data (sklearn)')
plt.xlabel('BMI')

plt.figure()
plt.scatter(X_test['bmi'], y_test['target'], color='red')
plt.plot(X_test['bmi'], y_test_pred, '-', color='green')
plt.title('Testing data (sklearn)')
plt.xlabel('BMI')
plt.show()