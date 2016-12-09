import urllib
import json
import oauth2 as oauth
import re

CONSUMER_KEY = "GRV8wIic3kQkR0jcS83Dto0HH"
CONSUMER_SECRET = "ctxjILVxebePQ0Xy2IxuVtXhZb93Cp8KaaCEModtk6OFBSI6Sp"
ACCESS_KEY = "39668843-s7VMwJf63EnO95EgSNl7hC4sOcVSdNir9AAfV2Zn5"
ACCESS_SECRET = "5E3UkNMQFWV3u7qt2C47fpSpvMyTvYawL8ShVxeetXFkO"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

#------------------------------------------------------------------------------


leaders = {'Prime Minister Narendra Modi':'narendramodi','President-elect Trump':'realdonaldtrump','President Obama':'BarackObama','President Vladimir Putin':'PutinRF_Eng','Chancellor Angela Merkel':'AngelaMerkeICDU','President Xi Jinping':'XiJinpingOffic'}

serviceurl = "https://api.twitter.com/1.1/"

api_method = "statuses/user_timeline.json?"

for i in leaders :
    
    url = serviceurl + api_method+urllib.urlencode({'user_id':str(leaders[i]),'screen_name':str(leaders[i]),'include_rts':'false','count':'100'})

    response, data = client.request(url)

    js = json.loads(data)

    hashDict = {}

    for item in js:
        
        currentLine = item['text']                  
        words = currentLine.split()

        for w in words :             
            wC = w.strip(',')
            wC1 = wC.strip('.')                     # Clean hashtags which have a full-stop or comma at the end
            wC2 = wC1.strip()
                
            if wC2 not in hashDict:         
                hashDict[wC2] = 1                   # Add to dictionary if hashtag does not exist in it
            else:
                hashDict[wC2] = hashDict[wC2] + 1

    print '====================================================================='
    print '\t\t\t'+str(i)
    print '====================================================================='
    for h in hashDict:
        print "\t"+h+"\t\t"+str(hashDict[h])+" times"