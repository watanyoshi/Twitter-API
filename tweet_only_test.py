# -*- coding: utf-8 -*-
# tweet_test.py

import oauth2

def tweet(text):
  ConsumerAPIkey = 'Your own API key of Consumer API keys' # These keys are required to use twitter API. Search info how to get them
  APIsecretkey = 'Your own API secret key of Consumer API keys'
  Accesstoken = 'Your own Access token'
  Accesstokensecret = 'Your own Access token secret'

  url = "https://api.twitter.com/1.1/statuses/update.json?status={}".format(text)
  consumer = oauth2.Consumer(key=ConsumerAPIkey, secret=APIsecretkey)
  token = oauth2.Token(key=Accesstoken, secret=Accesstokensecret)
  client = oauth2.Client(consumer, token)
  resp, content = client.request( url, method="POST")
  return content

#print (tweet("テスト")) # special characters need to be ASCII coded like %3A = ':', %23 = '#' and so on
print (tweet("BSニュースの担当キャスターをお知らせするテスト\n午前5%3A50　担当は阪田陽子キャスター\n%23BSニュース　%23阪田陽子")) # sample to post some info with special characters




