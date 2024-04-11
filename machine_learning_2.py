import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from joblib import dump

# Step 1: Import libraries

# Step 2: Read the csv files and create pandas dataframes
legitimate_df = pd.read_csv("structured_data_legitimate.csv")
phishing_df = pd.read_csv("structured_data_phishing.csv")

# Step 3: Combine legitimate and phishing dataframes, and shuffle
df = pd.concat([legitimate_df, phishing_df], axis=0)
df = df.sample(frac=1)

# Step 4: Remove 'URL' and remove duplicates, then create X and Y for the models
df = df.drop('URL', axis=1)
df = df.drop_duplicates()
X = df.drop('label', axis=1)
Y = df['label']

# Step 5: Split data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=10)

# Step 6: Create ML models using sklearn
svm_model = svm.LinearSVC()
rf_model = RandomForestClassifier(n_estimators=60)
dt_model = tree.DecisionTreeClassifier()
ab_model = AdaBoostClassifier()
nb_model = GaussianNB()
nn_model = MLPClassifier(alpha=1)
kn_model = KNeighborsClassifier()

# Step 7: Train the models
svm_model.fit(x_train, y_train)
rf_model.fit(x_train, y_train)
dt_model.fit(x_train, y_train)
ab_model.fit(x_train, y_train)
nb_model.fit(x_train, y_train)
nn_model.fit(x_train, y_train)
kn_model.fit(x_train, y_train)

# Step 8: Make predictions using each model
svm_predictions = svm_model.predict(x_test)
rf_predictions = rf_model.predict(x_test)
dt_predictions = dt_model.predict(x_test)
ab_predictions = ab_model.predict(x_test)
nb_predictions = nb_model.predict(x_test)
nn_predictions = nn_model.predict(x_test)
kn_predictions = kn_model.predict(x_test)

# Step 9: Combine predictions
combined_predictions = np.vstack((svm_predictions, rf_predictions, dt_predictions,
                                  ab_predictions, nb_predictions, nn_predictions,
                                  kn_predictions)).T

# Step 10: Take majority vote
final_predictions = np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis=1, arr=combined_predictions)

# Step 11: Evaluate performance
tn, fp, fn, tp = confusion_matrix(y_true=y_test, y_pred=final_predictions).ravel()
accuracy = (tp + tn) / (tp + tn + fp + fn)
precision = tp / (tp + fp)
recall = tp / (tp + fn)

print("Final model accuracy: ", accuracy)
print("Final model precision: ", precision)
print("Final model recall: ", recall)

# Save the ensemble model
dump(final_predictions, 'ensemble_model.pkl')
