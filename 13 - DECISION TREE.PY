from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.preprocessing import LabelEncoder
import random
X = [
    ['Sunny', 'Hot', 'High', False],
    ['Sunny', 'Hot', 'High', True],
    ['Overcast', 'Hot', 'High', False],
    ['Rain', 'Mild', 'High', False],
    ['Rain', 'Cool', 'Normal', False],
    ['Rain', 'Cool', 'Normal', True],
    ['Overcast', 'Cool', 'Normal', True],
    ['Sunny', 'Mild', 'High', False]
]
y = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No']
for i in range(len(X[0])):
    le = LabelEncoder()
    col = [row[i] for row in X]
    enc = le.fit_transform(col)
    for j in range(len(X)):
        X[j][i] = enc[j]
model = DecisionTreeClassifier(splitter="random", random_state=random.randint(0, 1000))
model.fit(X, y)
print(export_text(model, feature_names=['Outlook', 'Temp', 'Humidity', 'Windy']))
