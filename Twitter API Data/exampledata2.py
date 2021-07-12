# -*- coding: utf-8 -*-

# Bu kod onepage olarak yazılmıştır diğer bir py dosyasından kalıtılmadı ! 

"""
Created on Mon May 31 00:28:05 2021

@author: Taha Baturay
"""
# =============================================================================
#  WOEİD (32 bitlik konum tanımlayan referans kodu ! )
#  Twitter API’ına erişerek belli bir bölgeye ait gündemi görmek mümkün. 
#  Bunun için de trends_place adlı metoddan faydalanıyoruz.
#  Bu metoda geçilen id ülkeyi belirtmek için kullanılıyor.
#  Burada konumlara id vermek için Yahoo! 
#  Where on Earth ID (WOEID) sistemi kullanılıyor.
#  Buradan baktığımızda İstanbul’un kodunun 2344116 olduğunu görüyoruz. 
# 
# =============================================================================

import tweepy # tweepy kütüphanesini import ediyorum

# twitter api keylerini değişken değerlerine atadım ve tekrardan tokenleri girdim 
consumer_key = "Hg0VQLd3f1CMd8G66nYL1KR4n"
consumer_secret = "W9EDgrlTDytqMEHyWBWQccvVrhOjSD7Dejt3ytuJlCA2HT6trI"
access_token = "3166559529-ceLoQIZtOrNzMNn97RQPNYc5ats3RV6cRvtoYKB"
access_token_secret = "tDiHsL4YHIDkM0uGNnditDjS05SfjgJ5kXYeY05g4rt5e"

# burada bağlantı kodlarımızı yazıyorum ! 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# burada (aşağıda) trend topics (tt) etiketleri ile gündemde olan veriler var!

gundem = api.trends_place(id = "2344116")[0] # id lokasyonu İstanbul'dur.
for trend in gundem['trends']:
     print ("%s (%s)" % (trend['name'], trend['tweet_volume']))























