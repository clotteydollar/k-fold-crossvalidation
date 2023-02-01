
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("workshop.csv")

veiwhead =data.head()

print(veiwhead)

y = data['class']

X = data.drop(['class'],axis=1)

print(f'X:{X.shape}')