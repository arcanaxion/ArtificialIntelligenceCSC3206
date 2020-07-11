import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# import glass.csv as DataFrame
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'glass.csv')

data = pd.read_csv(file_path, names=["Id", "RI", "Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe", "Glass type"], index_col=0)

''' Instructions
1. split the data into 70% training and 30% testing data
    - use Na, Mg, Al, Si, K, Ca, Ba, and Fe (i.e. all columns except Glass type) as the input features.
    - use Glass type as the target attribute.

2. plot the accuracy of knn classifiers for all odd value of k between 3 to 100, i.e. k = 3, 5, 7, ..., 100. This is achieved by fulfilling the following tasks:
    i. create a loop to 
      A. fit the training data into knn classifiers with respective k.
      B. calculate the accuracy of applying the knn classifier on the testing data.
      C. print out the accuracy for each k.

    ii. plot a line graph with the y-axis being the accuracy for the respective k and x-axis being the value of k. You DO NOT need to save the graph.
'''

# start your code after this line
cols = ["Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe"]
x_train, x_test, y_train, y_test = train_test_split(data[cols], data["Glass type"], test_size=0.3)

k_vals = [k for k in range(3,100,2)]
accuracy = []
for k in k_vals:
  knc = KNeighborsClassifier(k)
  knc.fit(x_train, y_train)
  # y_predict = knc.predict(x_test)
  acc = knc.score(x_test,y_test)
  accuracy.append(acc)
  print("k={0}, Accuracy={1}".format(k, acc))

plt.figure("Accuracy for K Values")
plt.plot(k_vals, accuracy, marker='o')
plt.xlabel('K Value')
plt.ylabel('Accuracy')
plt.xticks(ticks=k_vals, label=k_vals)
plt.yticks(ticks=[i/10 for i in range(0,11)], label=[i/10 for i in range(0,11)])
plt.title("Accuracy for K Values")

# plt.show()