from azure.cognitiveservices.search.newssearch import NewsSearchAPI
from msrest.authentication import CognitiveServicesCredentials

subscription_key = '2db741825a6e49b9b86bc63d41337bcc'
search_term = "shaken baby syndrome california"
client = NewsSearchAPI(CognitiveServicesCredentials(subscription_key))
news_result = client.news.search(query=search_term, market="en-us", count=1000)