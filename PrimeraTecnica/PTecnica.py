import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm
import numpy as np 
#from sklearn.metrics import mean_squared_error
#from sklearn.model_selection import train_test_split
#from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import pairwise_distances 
#import matplotlib.pyplot as plt
import sklearn

tagdic = dict()
userdic = dict()
locdic = dict()

def asigDict(users,Tag,Loc):
    #import pudb; pudb.set_trace()
    iU=1
    iT=1
    iL=1
    for line in users.itertuples():
        """print('hi')
        print('hello')
        print('disfruta')"""
        if line[1] not in userdic:
            userdic[line[1]]=iU
            iU=iU+1

    for line in Tag.itertuples():
        if line[1] not in tagdic:
            tagdic[line[1]]=iT
            iT=iT+1
        #tagdic[line[1]]=iT+1
    for line in Loc.itertuples():
        if line[1] not in locdic:
            locdic[line[1]]=iL
            iL=iL+1

def BuilInterest(UserW,ItemsR):
    #import pudb; pudb.set_trace()
    #I(Ui,Sj) = SUMA(Wij,Rij) 
    print("Intereses")
    n_fU = UserW.shape[0];n_cU = UserW.shape[1]
    n_fI = ItemsR.shape[0];n_cI = ItemsR.shape[1]
    matrixInteres = np.zeros((n_fU,n_cI))

    for i in range(0,n_fU):
        for j in range(0,n_cI):
            for k in range(0,n_cU):
                matrixInteres[i,j]+=UserW[i,k]*ItemsR[k,j]
    return matrixInteres

def predict(ratings, similarity, type='user'):
        if type == 'user':
            mean_user_rating = ratings.mean(axis=1)
            #Usamos np.newaxis para que mean_user_rating tenga el mismo formato que ratings
            ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
            pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
        elif type == 'item':
            pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])
        return pred
def ordenar(lista):
    tam=len(lista)
    for i in range(0,tam):
        for j in range(0,tam-i-1):
            if (lista[j][1]<lista[j+1][1]):
                temp=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=temp
    return lista
def calcular_coseno(matriz,selection):
    size = 4
    lista=[]
    for i in range (0,size):
        if selection != i :
            cos_sim = dot(matriz[selection], matriz[i])/(norm(matriz[selection])*norm(matriz[i]))
            lista.append((i+1,cos_sim))
    return (ordenar(lista))


if __name__ == "__main__":

    #CARGA DE DATOS  
    #Usuario
    u_cols = ['id_person','age','gender']
    users = pd.read_csv('data/person.csv',sep=',',names=u_cols,encoding='latin-1')

    #Item = Place  
    i_cols = ['id_location', 'name_location' ,'state','lat','lng']
    items = pd.read_csv('data/location.csv', sep=',', names=i_cols,
    encoding='latin-1')
    #n_item_s = preferences.id_person.unique().shape[0]+1

    #Preferences 
    r_cols = ['id_person','id_location','group','season','trip_type','duration','tag']
    preferences = pd.read_csv('data/preferences.csv',sep=',',names=r_cols,encoding='latin-1')


    #print(users.shape)
    #print(users.head())

    #import pudb; pudb.set_trace()
    n_item_s= preferences.id_location.unique().shape[0]+1
    #n_items = ratings.movie_id.unique().shape[0]
    n_users = preferences.id_person.unique().shape[0]+1
    #n_items = ratings.movie_id.unique().shape[0]

    #print(preferences.shape)
    #print(preferences.head())

    t_cols = ['tag','count_tag']
    Etiquetas = pd.read_csv('data/tag.csv',sep=',',names=r_cols,encoding='latin-1')

    asigDict(users,Etiquetas,items)
    n_tags = len(tagdic)+1#Etiquetas.tag.unique().shape[0]

    
    #MATRIZ DE USUARIO VS TAG
    #import pudb; pudb.set_trace()
    user_tag_matrix = np.zeros((n_users, n_tags))
    for line in preferences.itertuples():
        user_tag_matrix[userdic[line[1]], tagdic[line[3]]] =  user_tag_matrix[userdic[line[1]], tagdic[line[3]]] + 1
        user_tag_matrix[userdic[line[1]], tagdic[line[4]]] =  user_tag_matrix[userdic[line[1]], tagdic[line[4]]] + 1
        user_tag_matrix[userdic[line[1]], tagdic[line[5]]] =  user_tag_matrix[userdic[line[1]], tagdic[line[5]]] + 1
        user_tag_matrix[userdic[line[1]], tagdic[line[6]]] =  user_tag_matrix[userdic[line[1]], tagdic[line[6]]] + 1
    #TF-IDF

    #MATRIZ DE TAG VS RECURSO
    #import pudb; pudb.set_trace()
    tag_loc_matrix = np.zeros((n_tags,n_item_s))
    for line in preferences.itertuples():

        tag_loc_matrix[tagdic[line[3]],locdic[line[2]]] =  tag_loc_matrix[tagdic[line[3]],locdic[line[2]]]+ 1
        tag_loc_matrix[tagdic[line[4]],locdic[line[2]]] =  tag_loc_matrix[tagdic[line[4]],locdic[line[2]]] + 1
        tag_loc_matrix[tagdic[line[5]],locdic[line[2]]] =  tag_loc_matrix[tagdic[line[5]],locdic[line[2]]]+ 1
        tag_loc_matrix[tagdic[line[6]],locdic[line[2]]] =  tag_loc_matrix[tagdic[line[6]],locdic[line[2]]]+ 1
        #user_tag_matrix[line[1], line[4]] = user_tag_matrix[line[1], line[4]] + 1
        #user_tag_matrix[line[1], line[5]] = user_tag_matrix[line[1], line[5]] + 1
        #user_tag_matrix[line[1], line[6]] = user_tag_matrix[line[1], line[6]] + 1
    
    #Construct Tourists' Interest Model of Tourist Attractions

    #CONSTRUCCION DE INTERES
    MInter = BuilInterest(user_tag_matrix,tag_loc_matrix)
    print(MInter)

    user_similarity = pairwise_distances(MInter, metric='cosine')
    #item_similarity = pairwise_distances(data_matrix.T, metric='cosine')

    user_prediction = predict(MInter, user_similarity, type='user')
    #item_prediction = predict(data_matrix, item_similarity, type='item')
    print(user_prediction)

    lista= calcular_coseno(MInter,2)
    
    #for i in range(0,len(lista)):