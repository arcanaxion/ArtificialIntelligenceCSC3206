import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import os 
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))

header = ["Index", "A", "B", "C", "D", "E"]
posneg = pd.read_csv(os.path.join(dir_path, "posneg.csv"), header=0, names=header)

feature_cols = ["A", "B", "C", "D"]
X = posneg[feature_cols]
val, label = pd.factorize(posneg['E'])
y = pd.DataFrame(val)

dtc = DecisionTreeClassifier(criterion='gini')
dtc.fit(X, y)

plt.figure(figsize=[10,10])
tree = plot_tree(dtc, feature_names=feature_cols, 
                 class_names=label, filled=True, rounded=True)
plt.show()
r = export_text(dtc, feature_names=feature_cols)
print(r)