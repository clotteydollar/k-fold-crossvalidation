
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
data = pd.read_csv("workshop.csv")

veiwhead =data.head()

print(veiwhead)

y = data['class']

X = data.drop(['class'],axis=1)

print(f'X:{X.shape}')


## creating test and train data
X_train, X_test , y_train, y_test = train_test_split(X,y, test_size=0.20, random_state=101)

print(f'X_train:{X_train.shape}')
print(f'X_test:{X_test.shape}')
print(f'y_train:{y_train.shape}')
print(f'y_test:{y_test.shape}')