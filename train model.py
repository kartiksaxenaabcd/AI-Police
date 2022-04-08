import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, confusion_matrix, classification_report, accuracy_score, f1_score

# ML Libraries
from sklearn.ensemble import RandomForestClassifier,VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
import numpy as np
# Evaluation Metrics
import pickle
from sklearn import metrics
dataset = pd.read_csv('inputs.csv')


# Labels are the values we want to predict
Y = np.array(dataset['PrimaryType'])
# Remove the labels from the features
# axis 1 refers to the columns
X=dataset.drop('PrimaryType', axis = 1)
# Saving feature names for later use
feature_list = list(dataset.columns)
# Convert to numpy array
X = np.array(X)

from sklearn.model_selection import train_test_split
train_features, test_features, train_labels, test_labels = train_test_split(X, Y, test_size = 0.1, random_state = 1)
model = RandomForestClassifier(n_estimators=250, # Number of trees
                                  min_samples_split = 10,
                                  bootstrap = True, 
                                  max_depth = 300, 
                                  min_samples_leaf = 10)

model.fit(train_features, train_labels);
predictions =model.predict(test_features)
# Calculate the absolute errors
errors = abs(predictions - test_labels)
# Print out the mean absolute error (mae
y_pred =model.predict(test_features)



# Check accuracy score 

from sklearn.metrics import accuracy_score
a=2*format(accuracy_score(test_labels, y_pred))

print('Model accuracy score with decision-trees : {0:0.4f}'. format(accuracy_score(test_labels, y_pred)))
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
