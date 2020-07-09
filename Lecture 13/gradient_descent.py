# Making the imports
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Preprocessing Input data
X = np.array([0, 0.1, 0.15, 0.2, 0.25, 0.3]) 
Y = np.array([0, 0.1, 0.2, 0.1, 0.15, 0.25]) 
plt.scatter(X, Y)
plt.show()
  

# Building the model
m = 0
c = 0

L = 0.1  # The learning Rate
epochs = 10  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X

# Performing Gradient Descent 
for i in range(epochs): 
    Y_pred = m*X + c  # The current predicted value of Y
    print((-2/n) * sum(X * (Y - Y_pred)))
    print((-2/n) * sum(Y - Y_pred))
    D_m = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c
    print("m:", m, ", c:", c)
    
print (m, c)

# Making predictions
Y_pred = m*X + c

plt.scatter(X, Y)
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red') # predicted
plt.show()
