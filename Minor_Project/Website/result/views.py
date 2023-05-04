from django.shortcuts import render

# Create your views here.
def result(request):
    def machine_learning_model(request):
        import PyPDF2
    import numpy as np
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score

    def find_value(i,text):
        index=text.find(i)
        index=index+len(i)
        end=index
        while text[end] != '\n':
            end+=1
        li_value = text[index:end]
        value_list = li_value.split() 
        if(value_list[0]==':'):
            value_list.remove(value_list[0])
        temp_value = value_list[0]
        temp_dict={"m":1,"f":0,"asymptomatic":0,"atypical":1,
                "non-anginal":2,"typical":3,"yes":1,"no":0,
                "down":0,"flat":1,"upsloping":2,"fixed":1,"normal":2,"reversible":3}
        if(temp_value[-1]==';'):
            temp_value=temp_value[:-1]
        new_temp_value=temp_value
        if(temp_value in list(temp_dict.keys())):
            new_temp_value=temp_dict[temp_value]
        return new_temp_value

    df=pd.read_csv("Heart_minor.csv",index_col=0)
    pdf = open("report4.pdf","rb")
    reader = PyPDF2.PdfReader(pdf)
    attributes = ["age","sex","chest pain","cholesterol","(fasting)","thalach","angina:","old-peak","slope","(ca)","thalassemia","target"]
    df.columns = attributes
    attributes = attributes[:-1]
    text=""
    page=reader.pages[0]
    text=page.extract_text().lower()

    values = {}
    for i in attributes:
        if(i in text):
            value = find_value(i,text)
            values[i]=float(value)
        else:
            values[i]=-1

    for i in values.keys():
        if(values[i]==-1):
            df.drop(columns=[i],inplace=True)

    x = df.iloc[:,:-1].values
    y = df.iloc[:,-1].values
    rand_int = np.random.randint(1,100)
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=rand_int)
    ss = StandardScaler()
    x_train_ss = ss.fit_transform(x_train)
    x_test_ss = ss.transform(x_test)
    KNN = KNeighborsClassifier(n_neighbors=13,metric="minkowski",p=2)
    KNN.fit(x_train_ss,y_train)
    y_pred = KNN.predict(x_test_ss)

    input_list = list(map(float,[values[x] for x in values.keys() if(values[x])!=-1]))

    label = KNN.predict(ss.transform([input_list]))
    if(label==0):
        output="Don't Have"
    if(label==1):
        output = "Have"
    output=f"\nWith {round(accuracy_score(y_test,y_pred)*100,2)} accuracy our Doctor Believes that you {output} a Heart Disease."
    return render(request, 'result/result.html')