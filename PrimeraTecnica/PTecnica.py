import pandas as pd
import numpy as np
#from sklearn.metrics import mean_squared_error
#from sklearn.model_selection import train_test_split
#from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import pairwise_distances 
#import matplotlib.pyplot as plt
import sklearn

#Carga de datos 
#Usuario
u_cols = ['id_person','age','gender']
users = pd.read_csv('data/person.csv',sep=',',names=u_cols,encoding='latin-1')

#Item = Place  
i_cols = ['id_location', 'name_location' ,'state','lat','lng']
items = pd.read_csv('data/location.csv', sep=',', names=i_cols,
encoding='latin-1')

#Preferences 
r_cols = ['id_person','id_location','group','season','trip_type','duration','tag']
preferences = pd.read_csv('data/preferences.csv',sep=',',names=r_cols,encoding='latin-1')
#print(users.shape)
#print(users.head())

#print(preferences.shape)
#print(preferences.head())

#print(items.shape)
#print(items.head())

#CARGA DATOS DE PRUEBA
#r_cols = ['user_id', 'move_id', 'rating', 'unix_timestamp']
#ratings_train = pd.read_csv('ml-100k/ua.base', sep='\t', names=r_cols, encoding='latin-1')
#ratings_test = pd.read_csv('ml-100k/ua.test', sep='\t', names=r_cols, encoding='latin-1')
#ratings_train.shape, ratings_test.shape


#import pudb; pudb.set_trace()
n_item_s= preferences.id_location.unique().shape[0]
#n_items = ratings.movie_id.unique().shape[0]
n_users = preferences.id_person.unique().shape[0]
#n_items = ratings.movie_id.unique().shape[0]

#MATRIZ DE USUARIO VS TAG

#import pudb; pudb.set_trace()
#Tag
print(preferences.shape)
print(preferences.head())

t_cols = ['tag','count_tag']
Tag = pd.read_csv('data/tag.csv',sep=',',names=r_cols,encoding='latin-1')
n_tags = Tag.tag.unique().shape[0]

user_tag_matrix = np.zeros((n_users, n_tags))

tagdic = dict()
userdic = dict()
iU=0
iT=0
for line in users.itertuples():
     userdic[line[1]]=iU+1

for line in Tag.itertuples():
    tagdic[line[1]]=iT+1

#for line in preferences.itertuples():
#    user_tag_matrix[userdic[line[1]], tagdic[line[3]]] = user_tag_matrix[line[1], line[3]] + 1
    #user_tag_matrix[line[1], line[4]] = user_tag_matrix[line[1], line[4]] + 1
    #user_tag_matrix[line[1], line[5]] = user_tag_matrix[line[1], line[5]] + 1
    #user_tag_matrix[line[1], line[6]] = user_tag_matrix[line[1], line[6]] + 1


#Calcular 
"""user_similarity = pairwise_distances(data_matrix, metric='cosine')
item_similarity = pairwise_distances(data_matrix.T, metric='cosine')



def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        #Usamos np.newaxis para que mean_user_rating tenga el mismo formato que ratings
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])
    return pred


user_prediction = predict(data_matrix, user_similarity, type='user')
item_prediction = predict(data_matrix, item_similarity, type='item')


print(user_prediction) """