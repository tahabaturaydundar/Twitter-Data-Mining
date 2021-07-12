# -*- coding: utf-8 -*-
"""
Created on Mon May 31 01:00:42 2021

@author: Taha Baturay
"""
# =============================================================================
# 
# Diyelim ki bir kaç hesabın ayrıntılarını yazdırmak istiyoruz. 
# Bunun için get_user metodunu kullanacağız. 
# Bu metoddan bir user nesnesi döner.
#
# =============================================================================

import tweepy; #tweepy kütüphanesi import edildi ! 


# twitter api'den alınan tokenler değişkenlere atandı ! 
consumer_key = "Hg0VQLd3f1CMd8G66nYL1KR4n"
consumer_secret = "W9EDgrlTDytqMEHyWBWQccvVrhOjSD7Dejt3ytuJlCA2HT6trI"
access_token = "3166559529-ceLoQIZtOrNzMNn97RQPNYc5ats3RV6cRvtoYKB"
access_token_secret = "tDiHsL4YHIDkM0uGNnditDjS05SfjgJ5kXYeY05g4rt5e"

# twitter api bağlantı kodları ! 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Kullanıcı İşlemlerinden Örnekler ! 

hesap_listesi = ["cagatayulusoyy", "SeckinOzdemir", "KeremBursin", "MYildirimResmi", "tnrolmez", "burakozcivit", "TSayisman", "Aras_B_iynemli"]
for hesap in hesap_listesi:
    kullanici = api.get_user(id=hesap)
    print("Kullanıcı adı: @%s [%s] (Takip ettikleri: %i, Takip eden: %i)" % (kullanici.screen_name, kullanici.id, kullanici.friends_count, kullanici.followers_count))
    print(kullanici.description)
    print("-------------------------------------\n")


