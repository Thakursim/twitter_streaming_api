# Twitter Streaming API
 
This API gives you the data directly from Twitter as and when it is posted. Here I have used DataFrame to show the output in terminal. 

Clone this repository using this command:-

   `https://github.com/Thakursim/twitter_streaming_api`

# Getting up and running.

This steps will get you up and running with a local development environment. Use this command to get into the working directory.

`cd twitter_streaming_api`

We assume you have the following installed:

  - pip
  - virtualenv
First make sure to create and activate a virtialenv, then open a terminal at the project root and install the requirements for local development.

```
     pip install -r requirements.txt
```

Now if you run this file **streamer.py** using the given command, then you will be asked for keyword which will be used by Twitter to give the result.

```
python streamer.py
```

Now the API is running and you will be able to see **Id, Name, and Tweet_count** of the user who is using that keyword in his/her tweet. You can also see the count of the links present in that tweet along with the domain name. 

Thank You 💙




