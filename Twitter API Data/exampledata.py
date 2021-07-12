# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:37:07 2021

@author: Taha Baturay
"""
import tweepy #tweepy kütüphanesini import ettim !

# burada twitter developer hesabımdan almış olduğum apı keyleri tanımladım ! 
consumer_key = "Hg0VQLd3f1CMd8G66nYL1KR4n"
consumer_secret = "W9EDgrlTDytqMEHyWBWQccvVrhOjSD7Dejt3ytuJlCA2HT6trI"
access_token = "3166559529-ceLoQIZtOrNzMNn97RQPNYc5ats3RV6cRvtoYKB"
access_token_secret = "tDiHsL4YHIDkM0uGNnditDjS05SfjgJ5kXYeY05g4rt5e"

# bağlantımızı aşağıdaki 3 satırda sağladık ! 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# bu aşağıdaki satırlar ile kendi hesabımının timeline'ındakı ilk 5 tweet'i getirir
tweetler = api.home_timeline(count=5) #Ana ekran akışını çağırıyoruz.
i = 1
for tweet in tweetler:
    print("%i: %s (%s): %s (%s) \n" % (i, tweet.user.name, tweet.user.screen_name, tweet.text, tweet.created_at))
    i += 1
    pass




