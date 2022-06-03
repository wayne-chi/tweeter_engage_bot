import os
from  functions import *
import pandas as pd
from tweepy import Client


def  create_reply(url):
  usernames = os.environ['staffsid'].strip().split(',')
  # print(usernames)
  consumer_key= os.environ['consumer_key']
  consumer_key_secret=os.environ['consumer_key_secret']
  bearer_token=os.environ['bearer_token']
  consumer_secret=consumer_key_secret

  client = Client(bearer_token= bearer_token,
                      consumer_key = consumer_key,
                      consumer_secret = consumer_secret)
## starrt  
  #twitter id link
  twid = get_id_from_link(url)
  ids = get_user_ids(client,usernames)
  
  phonebook = pd.DataFrame({'ids':ids,'usernames':usernames})
  liked_dict = pd.DataFrame(check_like(client,ids,twid) )
  retweeted_dict = pd.DataFrame( check_retweet(client,ids,twid) )
  commented_dict = pd.DataFrame(check_commented(client,ids,twid) )


  ## joinss
  df = phonebook.merge(liked_dict,on = 'ids',how= 'left')
  df = df.merge(retweeted_dict,on = 'ids',how = 'left')
  df = df.merge(commented_dict,on = 'ids',how = 'left')
  df['total'] = df['total'] = df['liked']+df['retweets']+df['commented']
  df.to_csv('data.csv')
  # df.to_excel('data.xlsx')
  def printstring(x):
    ret = '{:18}: {:1} : {:1} : {:1} : {:1}'.format(x.usernames,x.liked,x.retweets,x.commented,x.total)
    return ret
  last_col =  '{:5}:{:5} :{:7} :{:7} :{:5}'.format('name','liked','retweet','comment','total')
  df[last_col]= df.apply(printstring, axis = 1)
  final_string = last_col+'\n'+'\n'.join(list(df[last_col]))
  
  return final_string


  
  
  

