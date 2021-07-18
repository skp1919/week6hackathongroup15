from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from pandas import read_csv
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier

# define a Gaussain NB classifier
# clf = GaussianNB()

# Logistic regression classifier
# clf = LogisticRegression(penalty='l2',C=1.0, max_iter=10000)

# DecisionTree Classifier
clf = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2)

# SVM classifier
# clf = SVC(kernel='poly', degree=3, max_iter=300000)

# K Neighbors
# clf = KNeighborsClassifier(n_neighbors=12)

# K Neighbors - Euclidean
# clf = KNeighborsClassifier(n_neighbors=7,p=2)

# K Neighbors - Manhattan
# clf = KNeighborsClassifier(n_neighbors=7,p=1)

# Stochastic Gradient Descent
# clf = SGDClassifier(loss='modified_huber',shuffle=True,random_state=101)

# Random Forest
# clf = RandomForestClassifier(n_estimators=70, oob_score=True, n_jobs=-1,random_state=101, max_features=None, min_samples_leaf = 30)

enc = OrdinalEncoder()
lenc = LabelEncoder()

# define the class encodings and reverse encodings
classes = {0: "Good", 1: "Bad"}
r_classes = {y: x for x, y in classes.items()}

# function to train and load the model during startup
def load_model():
    # load the dataset from the official sklearn datasets
    df=read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data",sep=" ",header=None)
    
    #Prepare Data
    # split the data frame into inputs and outputs
    last_ix = len(df.columns) - 1
    X, y = df.drop(last_ix, axis=1), df[last_ix]

    # Categorical features has to be converted into integer values for the model to process. 
    #This is done through ordinal encoding.
    enc.fit(X)
    X = enc.transform(df.drop(last_ix, axis=1))
    # label encode the target variable to have the classes 0 and 1
    y = lenc.fit_transform(y)

    #print(X.shape, y.shape, Counter(y))
    
    #Splitting the data for training and testing
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
    
    #train
    clf.fit(X_train, y_train)
    
    # calculate the print the accuracy score
    acc = accuracy_score(y_test, clf.predict(X_test))
    print(f"Model trained with accuracy: {round(acc, 3)}")


# function to predict the credit score using the model
def predict(query_data):
    pred_data = list(query_data.dict().values())
    transformed_pred_data = enc.transform([pred_data])
    print(transformed_pred_data)
    print(transformed_pred_data.shape)
    prediction = clf.predict(transformed_pred_data.reshape(1,-1))
    p1 = lenc.inverse_transform(prediction)
    print("p1: ", p1[0])
    print(f"Model prediction: {classes[p1[0]-1]}")
    return classes[p1[0]-1]