import json
import sys
import csv


#Sitios de datos https://sites.google.com/site/yangdingqi/home/foursquare-dataset     (Foursquare Dataset)

#Como hallar rating :https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4812910/figure/alg1/


#Sitios de datos https://sites.google.com/site/yangdingqi/home/foursquare-dataset  (https://sites.google.com/site/treccontext/)
#Probando
#https://www.hindawi.com/journals/cin/2016/1291358/
#import pudb; pudb.set_trace()

dictTag = dict()

def addTag(tag):
    if tag in dictTag:
        dictTag[tag]= dictTag[tag]+1
    else :
        dictTag[tag]=1

if __name__ == "__main__":
    Data = []
    for line in open('Phase2_requests.json', 'r'):
        Data.append(json.loads(line))

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
    print(list_tag)

    """with open('data/tag.csv', 'wb') as csvfile:
        for v in dictTag:
            string = v+":"+str(dictTag[v])
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerows(string)"""
    
    with open('data/tag.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(list_tag)
    #import pudb; pudb.set_trace()
    #print('hello')
    #print('hi')
