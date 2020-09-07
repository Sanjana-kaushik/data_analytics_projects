#!/usr/bin/env python
# coding: utf-8

# In[39]:


from twython import Twython
import pandas as pd


# In[40]:


App_key = 'Jc0ZXKyzYqFkUcEgrDYzpaHtT'
App_secret = 'dKWJwvET08EcVvhiqBsf96i70559tcniLuZYjNLFNR8AQKL9Mc'
Auth_token = '115364146-agUw68MoUz1rnPBI2sbKs8ng83ap7x5alHMMRwti'
Auth_t_secret = 'NhDB6EM9x92zx6ByEwvfONRX5wleLstt6UvoeqcBaDUB7'

twitter = Twython(App_key,App_secret,Auth_token,Auth_t_secret)


# In[41]:


twitter


# In[42]:


search = twitter.search(q='machine')


# In[43]:


print(search)


# In[44]:


print(search['statuses'])


# In[45]:


print(search['statuses'][0]['text'])


# In[46]:


from twython import TwythonStreamer


# In[47]:


tweets = []
class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if data['user']['lang'] == 'en':
            tweets.append(data)
            print("received tweet #" ,len(tweets))
        if len(tweets)>=15:
            self.disconnect()
    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


# In[48]:


stream = MyStreamer(App_key,App_secret,Auth_token,Auth_t_secret)


# In[49]:


stream.statuses.filter(track ='endgame')


# In[50]:


tweets[0]


# In[51]:


avengers = []
for i in range(len(tweets)):
    avengers.append(tweets[i]['user']['followers_count'])


# In[53]:


df = pd.Series(avengers)


# In[54]:


df


# In[55]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[62]:


sns.countplot(df)


# I have taken the followers_count to find out the followers of the members who have tweeted about the avengers endgame. I have to say that this assignment was very interesting and easy to understand.  
