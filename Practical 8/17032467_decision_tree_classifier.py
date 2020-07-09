import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

iris = datasets.load_iris()
iris = {
    'attributes': pd.DataFrame(iris.data, columns=iris.feature_names),
    'target': pd.DataFrame(iris.target, columns=['species']),
    'targetNames': iris.target_names
}
diabetes = datasets.load_diabetes()
diabetes = {
    'attributes': pd.DataFrame(diabetes.data, columns=diabetes.feature_names),
    'target': pd.DataFrame(diabetes.target, columns=['diseaseProgression'])
}

for dt in [iris, diabetes]:
    x_train, x_test, y_train, y_test = train_test_split(dt['attributes'], dt['target'], test_size=0.2, random_state=1)
    dt['train'] = {
    'attributes': x_train,
    'target': y_train
    }
    dt['test'] = {
    'attributes': x_test,
    'target': y_test
    }
    
depth_list = [1,2,3,5,7,20]
train_acc = []
test_acc = []

for depth in depth_list:    

    dtc = DecisionTreeClassifier(criterion='gini', max_depth=depth)
    
    dtc.fit(iris['train']['attributes'], iris['train']['target'])
    
    predicts = dtc.predict(iris['test']['attributes'])
    
    print(pd.DataFrame(list(zip(iris['test']['target'].species,predicts)), columns=['target', 'predicted']))
    
    accuracy = dtc.score(iris['test']['attributes'],iris['test']['target'].species)
    
    train_accuracy = dtc.score(iris['train']['attributes'],iris['train']['target'].species)
    train_acc.append(train_accuracy)
    test_acc.append(accuracy)

plt.figure()
plt.plot(depth_list, train_acc, label='Train accuracy', marker='o')
plt.plot(depth_list, test_acc, label='Test accuracy', marker='o')
plt.xlabel('Depth')
plt.ylabel('Accuracy')
plt.title('Depth vs Accuracy')
plt.legend()
plt.show()