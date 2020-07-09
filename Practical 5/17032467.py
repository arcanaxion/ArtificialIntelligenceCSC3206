import pandas as pd
import numpy as np
from matplotlib import pyplot as pt

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'iris.data')

df = pd.read_csv(file_path)

df.columns = ["sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"]
df['class value'] = pd.factorize(df['class'])[0]

# question 5
print("\n######\nQUESTION 5\n######")
g = df.groupby('class')

# question 6
print("\n######\nQUESTION 6\n######")
print(g.get_group('Iris-setosa'))

# question 7
print("\n######\nQUESTION 7\n######")
for group in g.groups:
    print("Group name: {0}\n{1}\n".format(group, g.get_group(group).describe()))

# question 8
print("\n######\nQUESTION 8\n######")
pt.figure()
pt.scatter(df['sepal length in cm'], df['sepal width in cm'], color='r')
pt.title('Scatter plot')
pt.xlabel('sepal length in cm')
pt.ylabel('sepal width in cm')
pt.show()

# question 9
print("\n######\nQUESTION 9\n######")
df.to_string()
df.iterrows()