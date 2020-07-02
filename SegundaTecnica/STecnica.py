import pandas as pd
import json
import csv
from sklearn import datasets
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC

data = dict()

def CargaData():
    #CARGA DE DATOS  
    #p = (u, loc, t, tag) 
    i_cols = ['id_person','id_location','time','tag']
    Pu = pd.read_csv('../data/Pu.csv',sep=',',names=i_cols,encoding='latin-1')

   #v = (u, l, cx, etiqueta, t),
    j_cols = ['id_person', 'id_location' ,'context','tag','t']
    Vu = pd.read_csv('../data/Vu.csv', sep=',', names=j_cols,encoding='latin-1')
    #n_item_s = preferences.id_person.unique().shape[0]+1
   
    #location
    r_cols = ['id_location', 'name_location' ,'state','lat','lng']
    Loc = pd.read_csv('../data/location.csv',sep=',',names=r_cols,encoding='latin-1')
    
    CollAtrPu = dict()
    #import pudb; pudb.set_trace()
    for line in Vu.itertuples():
        if line[1] not in CollAtrPu:

            CollAtrPu[line[1]]=[line[2]]
            #CollAtrPu[line[1]][line[2]]= 1
        else:
            
            if line[2] not in CollAtrPu[line[1]]:
                CollAtrPu[line[1]].append(line[2])
            #else:
                #CollAtrPu[line[1]][line[2]]=CollAtrPu[line[1]][line[2]] + 1
            #CollAtrPu[line[1]].append()
    #import pudb; pudb.set_trace()
    #print("hello")
    print(CollAtrPu )
   

    ##########
    #attraction collection
    #L = {l1, l2, ..., lN} denota una colección de atracción de tamaño N.
    #  Cada atracción l representa un centro de agrupación extraído de la colección que contiene 
    #información de ubicación loc.
    # Lu denota la colección de atracciones que el usuario ha visitado. 
    # La atracción no es solo  lugar turístico tradicional,también podría ser un jardín, un centro comercial o una calle. 
    

if __name__ == "__main__":
    CargaData()
    """ iris = datasets.load_iris()
    X, y = iris.data, iris.target
    linearSVC = LinearSVC(random_state=0, multi_class='ovr') #svm 
    ovr = OneVsRestClassifier(linearSVC).fit(X, y)
    ovr.n_classes_
    ovr.estimators_
    """

"""# logistic regression for multi-class classification using a one-vs-rest
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
# define dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)
# define model
model = LogisticRegression()
# define the ovr strategy
ovr = OneVsRestClassifier(model)
# fit model
ovr.fit(X, y)
# make predictions
yhat = ovr.predict(X)

# logistic regression for multi-class classification using a one-vs-rest
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
# define dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)
# define model
model = LogisticRegression()
# define the ovr strategy
ovr = OneVsRestClassifier(model)
# fit model
ovr.fit(X, y)
# make predictions
yhat = ovr.predict(X) """

    #cancer = datasets.load_breast_cancer()

    # print the names of the 13 features
    #print("Features: ", cancer.feature_names)

    # print the label type of cancer('malignant' 'benign')
    #print("Labels: ", cancer.target_names)

    #Create a svm Classifier
    #clf = svm.SVC(kernel='linear') # Linear Kernel


    #extractor = weather.Extract(api_key)
    #[location,current] = extractor.features("MA/Boston",(('geolookup',''),('now','')))
    #print("Current Temperature in %s is: %s" %(location.data.city,current.temp_f))

    #Train the model using the training sets
    #clf.fit(X_train, y_train)

    #Predict the response for test dataset
    #y_pred = clf.predict(X_test)
