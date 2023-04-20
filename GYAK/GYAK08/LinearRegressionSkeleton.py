import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr

    def fit(self, X: np.array, y: np.array):

        self.X_train = X
        self.y_train = y
        self.c = 0
        self.m = 0
        n = float(len(self.X_train)) # Number of elements in X
        # Performing Gradient Descent 
        losses = []
        for i in range(self.epochs): 
            y_pred = self.m*self.X_train + self.c  # The current predicted value of Y

            residuals = self.y_train - y_pred
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(self.X_train * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            self.m = self.m - self.lr * D_m  # Update m
            self.c = self.c - self.lr * D_c  # Update c
            if i % 100 == 0:
                print(np.mean(self.y_train-y_pred))

    def predict(self, X):
        return self.m*X + self.c
    def evaluate(self,y_pred,y_test) -> float:
        return np.mean((y_pred - y_test)**2)
         
