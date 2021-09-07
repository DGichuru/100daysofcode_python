import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read.csv("data/Titanic/train.csv")

df.head()

df.describe()

#preprocessing
X=pd.DataFrame()
X['Pclass'] = df['Pclass']
X['Sex'] = df['Sex']
X['Age'] = df['Age']
X['Survived'] = df['Survived']
X = X.dropna(axis=0)

X.head()

#separate the data and target vars
y = X['Survived']
X = X.drop(['Survived'],axis = 1)

X['Sex'] = pd.get_dummies(X.Sex)['male'] # 1 for male else 0

scaler = StandardScaler()
X= scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
 
#Train the model 

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

#checking accuracy on the training set

model.score(X_train, y_train)

pred = model.predict(X_test)




