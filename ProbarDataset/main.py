import json
import sys
import csv
import random 
import operator


#Sitios de datos https://sites.google.com/site/yangdingqi/home/foursquare-dataset     (Foursquare Dataset)

#Como hallar rating :https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4812910/figure/alg1/


#Sitios de datos https://sites.google.com/site/yangdingqi/home/foursquare-dataset  (https://sites.google.com/site/treccontext/)
#Probando
#https://www.hindawi.com/journals/cin/2016/1291358/
#import pudb; pudb.set_trace()

dictTag = dict()
listTagA = ['Culture','History','Museums','Art','Galleries']
def addTag(tag):
    if tag in dictTag:
        dictTag[tag]= dictTag[tag]+1
    else :
        dictTag[tag]=1
def DataPrimeraTecnica(Data):
    location = []
    person = []
    preference = []
    listTagA = ['Culture','History','Museums','Art','Galleries']
    #import pudb; pudb.set_trace()
    for i in range(0,len(Data)): #len(Data)
        l = [Data[i]['body']['location']['id'],Data[i]['body']['location']['name'],Data[i]['body']['location']['state'],Data[i]['body']['location']['lat'],Data[i]['body']['location']['lng']]
        location.append(l)
        p = [Data[i]['body']['person']['id'],Data[i]['body']['person']['age'],Data[i]['body']['person']['gender']]
        person.append(p)
        
        listPreferences = Data[i]['body']['person']['preferences']
        for j in range(0,len(listPreferences)):
            tags = listPreferences[j]['tags']
            for tag in tags:
                if tag in listTagA:
                    pref =[Data[i]['body']['person']['id'],
                        Data[i]['body']['location']['id'],
                        Data[i]['body']['group'],
                        Data[i]['body']['season'],
                        Data[i]['body']['trip_type'],
                        Data[i]['body']['duration'],tag]
                    addTag(pref[2])
                    addTag(pref[3])
                    addTag(pref[4])
                    addTag(pref[5])
                    preference.append(pref)

                """pref =[i,
                            Data[i]['body']['location']['id'],
                            listPreferences[j]['rating'],
                            tag,
                            Data[i]['body']['group'],
                            Data[i]['body']['season'],
                            Data[i]['body']['trip_type'],
                            Data[i]['body']['duration'],
                            listPreferences[j]['documentId']]
                    preference.append(pref)"""
    with open('../data/location.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(location)

    with open('../data/person.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(person)



    with open('../data/preferences.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(preference)

    #print(dictTag)
    list_tag = []
    for l in dictTag:
        list_tag.append([l,dictTag[l]])
    #print(list_tag)

    """with open('data/tag.csv', 'wb') as csvfile:
        for v in dictTag:
            string = v+":"+str(dictTag[v])
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerows(string)"""
    
    with open('data/tag.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(list_tag)
def context(season,tag):
    
    season = season
    TimeofDay = ''
    #Temperature = 0
    #Weather = 
    if tag == 'Beer':
        TimeofDay = 'night' 
    if tag == 'Restaurants'or tag == 'Restaurant':
        TimeofDay = 'morning' 
    else:
        TimeofDay = "afternoon"
    return [season,TimeofDay]
    
def TagRelevant(CollecTag):
    #import pudb; pudb.set_trace()
    Dictag = dict()
    for tag in CollecTag:
        if tag not in Dictag:
            Dictag[tag]= 1
        else:
            Dictag[tag]= Dictag[tag]+1
    Dictag_sort = sorted(Dictag.items(), key=operator.itemgetter(1), reverse=True)
    return Dictag_sort
    #print(Dictag_sort)

def DataSegundaTecnica(Data):
    Pu = []  #Coleccion de datos de usuario individual 
    Vu = []
    loc = []
    listTagA = ['Culture','History','Museums','Art','Galleries','Beer','Shopping']
    for i in range(0,len(Data)): #len(Data)
        #l =[Data[i]['body']['location']['id'],]
        #IdUser = #random.randrange(90)
        IdUser = Data[i]['body']['person']['id']  
        l = [Data[i]['body']['location']['id'],Data[i]['body']['location']['name'],Data[i]['body']['location']['state'],Data[i]['body']['location']['lat'],Data[i]['body']['location']['lng']]
        loc.append(l)
        CollecTag = [] 
        for j in range(0,len(Data[i]['body']['person']['preferences'])):
            for tag in Data[i]['body']['person']['preferences'][j]['tags']:
                CollecTag.append(tag)
                if tag in listTagA:
                    #p = (u, loc, t, tag) 
                    p = [IdUser,
                        Data[i]['body']['location']['id'],
                        0,
                        tag]
                    Pu.append(p)
                    #v = (u, l, cx, etiqueta, t), 
                    v = [IdUser,
                        Data[i]['body']['location']['id'],
                        context(Data[i]['body']['season'],tag),
                        tag]
                    Vu.append(v) 
        import pudb; pudb.set_trace()
        Tagl=TagRelevant(CollecTag)
    #import pudb; pudb.set_trace() 
    with open('../data/location.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(loc)

    with open('../data/Pu.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(Pu)
    with open('../data/Vu.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(Vu)
    
if __name__ == "__main__":
    Data = []
    for line in open('Phase2_requests.json', 'r'):
        Data.append(json.loads(line))

    #DataPrimeraTecnica(Data)
    DataSegundaTecnica(Data)
    #import pudb; pudb.set_trace()
    #print('hello')
    #print('hi')
    
    #TRANSFORMANDO PARA LA SEGUNDA TECNICA LA DATA 
    #import pudb; pudb.set_trace()
    
