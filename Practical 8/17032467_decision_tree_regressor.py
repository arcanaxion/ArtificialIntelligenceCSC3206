import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
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

    dtr = DecisionTreeRegressor(max_depth=depth)
    
    dtr.fit(diabetes['train']['attributes'], diabetes['train']['target'])
    
    predicts = dtr.predict(diabetes['test']['attributes'])
    
    print(pd.DataFrame(list(zip(diabetes['test']['target'].diseaseProgression,predicts)), 
                  columns=['target', 'predicted']))
    
    accuracy = dtr.score(diabetes['test']['attributes'],
                    diabetes['test']['target'].diseaseProgression)
    
    train_accuracy = dtr.score(diabetes['train']['attributes'],diabetes['train']['target'].diseaseProgression)
    train_acc.append(train_accuracy)
    test_acc.append(accuracy)

plt.figure()
plt.plot(depth_list, train_acc, label='Train accuracy', marker='o')
plt.plot(depth_list, test_acc, label='Test accuracy', marker='o')
plt.xlabel('Depth')
plt.ylabel('Accuracy')
plt.xticks(ticks=depth_list, labels=depth_list)
plt.title('Depth vs Accuracy')
plt.legend()
plt.show()