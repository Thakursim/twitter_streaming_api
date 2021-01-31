from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import credentials
import pandas as pd
import tweepy

class TweetListener(StreamListener):

    def __init__(self, auth):
        self.user_id_list = []
        self.screen_name_list =[]
        self.tweets_count_list = []
        self.links_count_list = []
        self.auth = auth
        self.data = {"id":self.user_id_list, "name":self.screen_name_list, "tweets_count":self.tweets_count_list}
        self.data_link = {"links":self.links_count_list} 
        return super(StreamListener, self).__init__()

    def on_data(self, data):
        data_dict = json.loads(data)
        link = data_dict["entities"]["urls"]
        for x in link:
            print(x["expanded_url"].split("/", 3)[2]) 
        link_len = len(link)
        self.links_count_list.append(link_len)    
        self.user_id_list.append(data_dict["user"]["id"])
        api = tweepy.API(self.auth)
        user = api.get_user(data_dict["user"]["screen_name"])
        statuses_count = user.statuses_count
        self.tweets_count_list.append(statuses_count)
        self.screen_name_list.append(data_dict["user"]["screen_name"])
        self.df = pd.DataFrame(self.data, columns=["id", "name", "tweets_count"])
        self.lf = pd.DataFrame(self.data_link, columns=["links"]) 
        self.df.style.set_caption("User Report")
        print(self.df)
        print ("\n\n\n\n")
        print(self.lf)
        return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    
    auth = OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
    listener = TweetListener(auth)
    stream = Stream(auth, listener)
    keyword = input("Enter a keyword: ")

    stream.filter(track=[keyword])
     


