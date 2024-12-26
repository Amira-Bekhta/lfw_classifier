from load_data import load_splits
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier 
import joblib
X_train, X_test, y_train, y_test = load_splits()

# GaussianNB classifier
model_0 = GaussianNB()
model_0.fit(X_train, y_train)
joblib.dump(model_0, "models/model(GaussianNB).pkl")

# KNN
model_1 = KNeighborsClassifier(n_neighbors=15)
model_1.fit(X_train, y_train)
joblib.dump(model_1, "models/model(KNeighborsClassifier).pkl")

# SVC
model_2 = SVC(kernel='rbf', C=1, random_state=42)
model_2.fit(X_train, y_train)
joblib.dump(model_2, "models/model(SVC).pkl")

# Decision tree
model_3 = DecisionTreeClassifier()
model_3.fit(X_train, y_train)
joblib.dump(model_3, "models/model(DecisionTreeClassifier).pkl")