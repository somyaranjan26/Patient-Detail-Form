import pandas as pd
import os
from sklearn.tree import DecisionTreeRegressor
import pickle

os.chdir(r'C:\Users\RetailAdmin\Desktop\pro\Deployment-flask-master')
df = pd.read_csv('data1.csv' , index_col=0)
x1 = df.drop(columns = ['los'] , axis = 1)
y1  = df[['los']]
clf = DecisionTreeRegressor()
clf.fit(x1,y1)


pickle.dump(clf, open('model1.pkl','wb'))

# Loading model to compare the results
model1 = pickle.load(open('model1.pkl','rb'))
print(model1.predict([[1,0,8]]))