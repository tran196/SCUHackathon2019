from azure.cognitiveservices.search.newssearch import NewsSearchAPI
from msrest.authentication import CognitiveServicesCredentials

from pandas import DataFrame

import json

subscription_key = '2db741825a6e49b9b86bc63d41337bcc'
search_term = "shaken baby syndrome california"
client = NewsSearchAPI(CognitiveServicesCredentials(subscription_key))
news_result = client.news.search(query=search_term, market="en-us", count=1000)

numberOfArticles = len(news_result.value)     #How many news results the search came up with

# print(news_result.value[0].name)     #test print
# print(news_result.value[1].name)     #test print


rows = numberOfArticles
cols = 3 # name, description, url
result = [[0 for x in range(cols)] for x in range(rows)]        #create a 2d array


for i in range(rows):
  for j in range(cols):
        if j == 0:      #for name of article
            result[i][0] = news_result.value[i].name
        elif j == 1:    #for description of article
            result[i][1] = news_result.value[i].description
        elif j == 2:    #for url of article
            result[i][2] = news_result.value[i].url
        
df = DataFrame(result, columns = ["Name", "Description", "URL"])

print(df)

df.to_csv("test.csv", sep="*", encoding="utf-8")

outputFile = open("search.txt", "w+")

for x in range(rows):
    outputFile.write(result[x][0]+"*")
    outputFile.write(result[x][1]+"*")
    outputFile.write(result[x][2])
    outputFile.write("\n")

outputFile.close()
