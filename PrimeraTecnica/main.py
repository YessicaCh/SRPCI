"""import flickrapi
import json

api_key = u'fb91239320e1029bffa5ce3d0e7cb2ff'
api_secret = u'b871195c33de07e4'

flickr = flickrapi.FlickrAPI(api_key.encode('utf-8'), api_secret.encode('utf-8'),format='parsed-json')
extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
photosCats = flickr.photos.search(text='turist', per_page=200, extras=extras)
photos = photosCats['photos']
with open('data.json', 'w') as file:
    json.dump(photos, file, indent=4)
from pprint import pprint
pprint(photos) """

#Sitios de datos https://sites.google.com/site/yangdingqi/home/foursquare-dataset     (Foursquare Dataset)

#Como hallar rating :https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4812910/figure/alg1/


#Sitios de datos https://sites.google.com/site/yangdingqi/home/foursquare-dataset  (https://sites.google.com/site/treccontext/)
#Probando
#https://www.hindawi.com/journals/cin/2016/1291358/
import json
import sys
#import pudb; pudb.set_trace()


#try:
    #qByUser = byUsrUrlObj.read()
    #qUserData = json.loads(qByUser).decode('utf-8')
    #questionSubjs = qUserData["all"]["questions"]
#with open(json_file_path, 'r') as j:
#     contents = json.loads(j.read())
with open("Foursquare_attractions_TREC-CS_v2_229.747.json.json",'r') as f:
    raw_data = f.read()
    data = json.load(f.read())
    
    #data = json.loads(raw_data.decode('utf-8-sig'))
#except ValueError:  # includes simplejson.decoder.JSONDecodeError
#    print('Decoding JSON has failed')

"""with open(sys.argv[1]) as f:
        for line in f:
            request = json.loads(line)
            if request['id'] not in responses:
                sys.stderr.write('Response for request ID is missing %s\n' % request['id'])
                exit(1)
            candidates = set([x['documentId'] for x in request['candidates']])    
            if set(responses[request['id']]['suggestions']) != candidates:
                sys.stderr.write('Candidate and suggested documents do not match for request %s\n' % request['id'])
                exit(1)

sys.stdout.write('Success.\n')"""


"""with open('Phase2_requests.json','r') as file:
    data = json.load(file)"""

#f = open("Phase2_requests.json", "r")
#content = f.read()
#jsondecoded = json.loads(content)



"""import json
with open("Phase2_requests.json") as f:
  raw_data = f.read()
data = json.loads(raw_data.decode('utf-8-sig'))
    
with open(file_path) as f:
    data = json.loads(f.read())
    print(data[0]['text']) """


























































""""#SISTEMA DE RECOMENDACION :
import pandas as pd 
import numpy as np
import warnings
import os
warnings.filterwarnings('ignore')

#listaDir = os.listdir(os.getcwd())
#print(listaDir[0])
#df = pd.read_csv('u.data', sep='\t', names=['user_id','item_id','rating','titmestamp'])

#PREPROCESAMIENTO
#Carga la data 
df = pd.read_csv('ratings.csv', sep='\t', names=['userId','movieId','rating','timestamp'])
#print(df.head(10))

#Carga archivos de los titulos 
movie_titles = pd.read_csv('movies.csv')
#print(movie_titles.head())

df = pd.merge (df, movie_titles, on = 'movieId')
#print(df.head ())

#df.describe()  #descripción de nuestro conjunto de datos

ratings = pd.DataFrame (df.groupby ('title') ['rating']. mean ()) # se agrupa de acuerdo a la calificación promedio de cada película.
#print(ratings.head ())

ratings['number_of_ratings'] = df.groupby('title')['rating'].count() # cantidad de calificaciones que obtuvo cada película.
#print(ratings.head(10))

import seaborn as sns
sns.jointplot(x='rating', y='number_of_ratings', data=ratings)

#MATRIX USER VS MOVIE WITH RATINGS 

"""
"""movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')
#movie_matrix.head()

ratings.sort_values('number_of_ratings', ascending=False).head(10)


#SUPONGAMOS 
AFO_user_rating = movie_matrix['Air Force One (1997)']
contact_user_rating = movie_matrix['Contact (1997)']

AFO_user_rating.head()
contact_user_rating.head()

similar_to_air_force_one=movie_matrix.corrwith(AFO_user_rating)

similar_to_air_force_one.head()

similar_to_contact = movie_matrix.corrwith(contact_user_rating)

similar_to_contact.head()

corr_contact = pd.DataFrame(similar_to_contact, columns=['Correlation'])
corr_contact.dropna(inplace=True)
corr_contact.head()
corr_AFO = pd.DataFrame(similar_to_air_force_one, columns=['correlation'])
corr_AFO.dropna(inplace=True)
corr_AFO.head()

corr_AFO = corr_AFO.join(ratings['number_of_ratings'])
corr_contact = corr_contact.join(ratings['number_of_ratings'])
corr_AFO .head()
corr_contact.head()

corr_AFO[corr_AFO['number_of_ratings'] > 100].sort_values(by='correlation', ascending=False).head(10)

corr_contact[corr_contact['number_of_ratings'] > 100].sort_values(by='Correlation', ascending=False).head(10) """