
from sklearn import datasets
from sklearn import svm
from wunder import weather


def Preprocesamiento():
    print('hi')



if __name__ == "__main__":

    print("Hello world")


    #Load dataset
    #cancer = datasets.load_breast_cancer()

    # print the names of the 13 features
    #print("Features: ", cancer.feature_names)

    # print the label type of cancer('malignant' 'benign')
    #print("Labels: ", cancer.target_names)

    #Create a svm Classifier
    #clf = svm.SVC(kernel='linear') # Linear Kernel


    extractor = weather.Extract(api_key)
    [location,current] = extractor.features("MA/Boston",(('geolookup',''),('now','')))
    print("Current Temperature in %s is: %s" %(location.data.city,current.temp_f))

    #Train the model using the training sets
    #clf.fit(X_train, y_train)

    #Predict the response for test dataset
    #y_pred = clf.predict(X_test)
