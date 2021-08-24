#import the dependencies
from sklearn.datasets import load_iris
from sklearn.svm import SVC
#load dataset
dataset = load_iris()
data = dataset.data
target = dataset.target

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit_transform(data) #check out preprocessing module of sklearn to learn more about preprocessing in ML

#now let us divide data into training and testing set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42, test_size=0.3)


#train a model
model = SVC()
model.fit(X_train,y_train)


from sklearn.metrics import accuracy_score

accuracy_score(y_test, model.predict(X_test))


model.support_vectors_.shape

model.support_vectors_

model2= SVC(kernel="rbf", gamma=0.2)
model2.fit(X_train, y_train)
model2.score(X_test, y_test)