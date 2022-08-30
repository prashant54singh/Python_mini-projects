#import notification from plyer module
# from random_word import RandomWords
import json
from plyer import notification
#import time
import time
# import random

import requests
# r=RandomWords()
# words = ("Rock", "Paper", "scissor","rain","sun","sunny","tree","jungle")
# word=random.choice(words)
# rnd=json.loads(rd)
# val=(rd.get("word"))
# print(word)
url = 'https://kanjialive-api.p.rapidapi.com/api/public/search/rain/'

headers = {
	"X-RapidAPI-Key": "aab3399f00msh57322c108e08b90p1a8ca8jsn10b9764e8abb",
	"X-RapidAPI-Host": "kanjialive-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
data = response.text
gg=json.loads(data)
values=gg[0].get("kanji")
print(values)
#Use while loop to create notifications indefinetly
while(True):
    #notification
    notification.notify(
        title = "Today's kanji of the day is",
        message ='''雨 - Rain 'stroke': 8''',
		app_icon = "C:/Users/Harsh/Downloads/favicon.ico",
        timeout = 60
    )
    #System pause the execution of this programm for 60 minutes
    time.sleep(60*60)

		