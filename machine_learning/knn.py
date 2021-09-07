from sklearn.datasets import load_iris
dataset = load_iris()
X = dataset.data
y = dataset.target

#standardize the data to make sure each feature contributes equally to the distance
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_processed = ss.fit_transform(X)

#split dataset into train and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.3, random_state=42)

#fit the dataset
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors= 5, metric="minkowski", p=2)
model.fit(X_train, y_train)

model.score(X_test, y_test)