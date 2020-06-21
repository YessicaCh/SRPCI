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
u_cols = ['user_id','age','sex','occupation','zip_code']
users = pd.read_csv('ml-100k/u.user',sep='|',names=u_cols,encoding='latin-1')
#Ratings 
r_cols = ['user_id','move_id','rating','unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data',sep='\t',names=r_cols,encoding='latin-1')
#Item = peliculas 
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('ml-100k/u.item', sep='|', names=i_cols,
encoding='latin-1')

#print(users.shape)
#print(users.head())

#print(ratings.shape)
#print(ratings.head())

#print(items.shape)
#print(items.head())

#CARGA DATOS DE PRUEBA
r_cols = ['user_id', 'move_id', 'rating', 'unix_timestamp']
ratings_train = pd.read_csv('ml-100k/ua.base', sep='\t', names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv('ml-100k/ua.test', sep='\t', names=r_cols, encoding='latin-1')
ratings_train.shape, ratings_test.shape

print(ratings.shape)
print(ratings.head())
#import pudb; pudb.set_trace()
n_item_s= ratings.move_id.unique().shape[0]
#n_items = ratings.movie_id.unique().shape[0]
n_users = ratings.user_id.unique().shape[0]
#n_items = ratings.movie_id.unique().shape[0]

#MATRIZ DE USUARIO VS ITEM

data_matrix = np.zeros((n_users, n_item_s))
for line in ratings.itertuples():
    data_matrix[line[1]-1, line[2]-1] = line[3]

#Calcular 
user_similarity = pairwise_distances(data_matrix, metric='cosine')
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


print(user_prediction) 