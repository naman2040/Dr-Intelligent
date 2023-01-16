
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df=pd.read_csv("Heart_minor.csv")

x = df.iloc[:,1:-1].values
y = df.iloc[:,-1].values 

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
ss = StandardScaler()

x_train_ss = ss.fit_transform(x_train)
x_test_ss = ss.transform(x_test)

KNN = KNeighborsClassifier(n_neighbors=13,metric="minkowski",p=2)
KNN.fit(x_train_ss,y_train)
y_pred = KNN.predict(x_test_ss)

print("Please Enter your Report Details : \nAGE, SEX, CP, CHOL, FBS, THALACH, EXANG, OLDPEAK, SLOPE, CA, THAL : ")
age,sex,cp,chol,fbs,thalach,exang,oldpeak,slope,ca,thal = list(map(float,input().split(" ")))
label = KNN.predict(ss.transform([[age,sex,cp,chol,fbs,thalach,exang,oldpeak,slope,ca,thal]])) 

if(label==0):
    output="Don't Have"
if(label==1):
    output = "Have"

print(f"With {round(accuracy_score(y_test,y_pred)*100,2)} accuracy our Doctor Believes that you {output} a Heart Disease.")
