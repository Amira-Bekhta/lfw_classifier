from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split

lfw_people = fetch_lfw_people(min_faces_per_person=100, resize=0.4)

X = lfw_people.data      
y = lfw_people.target    

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

def load_splits():
    return X_train, X_test, y_train, y_test