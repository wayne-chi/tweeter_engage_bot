import pandas as pd
from tweepy import Client

def get_id_from_link(url):
    tw = url.split('?')[0]
    twid = tw.split('/')[-1]
    return twid

def get_user_ids(client,usernames):
    responses = client.get_users(usernames =usernames).data
    for i in range(len(responses)):
        responses[i] = responses[i].id
    return responses

def check_like(client,ids,twid):
    """returns a dictionary of 1 ands and o's """
    likes = client.get_liking_users(twid,max_results=100).data
    liked=[]
    for i in range(len(likes)):
        likes[i] = likes[i].id
    
    for person_id in ids:
        liked.append(int(person_id in likes))
        
    like_dict = {'ids':ids,'liked':liked}
    return like_dict

def check_retweet(client,ids,twid):
    """ returns a dictionary of 1 ands and o's""" 
    retweeters =  client.get_retweeters(twid,max_results=100).data
    retweets=[]
    for i in range(len(retweeters)):
        retweeters[i]=retweeters[i].id
   
    for person_id in  ids:
        retweets.append(int(person_id in retweeters))
    retweet_dict= {'ids':ids,'retweets' : retweets}
    return retweet_dict
    
def check_commented(client,ids,twid):
    """twid is the id of the post"""
    commented= []
    for person_id in ids:
        tweetlist = client.get_users_tweets(person_id,max_results =100,tweet_fields= ['id'],expansions='referenced_tweets.id')
        flag=0
        try:
          tweetlist = tweetlist.includes['tweets']
          
          for i in range(len(tweetlist)):
              this_id = tweetlist[i].id
              if twid == str(this_id):
                  flag = 1
                  break
        except:
          pass
        commented.append(flag)
          
    comment_dict = {'ids':ids,'commented':commented}
    return comment_dict