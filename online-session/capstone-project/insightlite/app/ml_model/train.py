import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from joblib import dump

# Dummy synthetic dataset
# priority, est_days, hist_rate → delayed?
X = np.array([
    [1, 1, 0.2], [2, 1, 0.3], [3, 2, 0.4],
    [4, 2, 0.5], [5, 3, 0.6],
    [1, 1, 0.1], [2, 2, 0.2], [3, 3, 0.5],
    [4, 4, 0.7], [5, 5, 0.9],
])

y = np.array([0, 0, 0, 1, 1, 0, 0, 1, 1, 1])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
dump(model, "model.pkl")
print("MODEL TRAINED & SAVED!")
