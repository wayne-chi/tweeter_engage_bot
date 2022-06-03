# Tweeter Engage Bot
Hi, in this project i am developing an ETL pipeline that extracts data from Twitter, transforms it, and loads it  to to the telegram bot as a file and text. 
## Description
This bot gets a message if it is a tweeter link, pulls information concerning the people who reacted/liked, people who commented and those who retweeted. Filters the information of certain people who you wish to monitor their engagement with your tweets.\
The bot then replies with a report.
## Example Use Cases
- Companies to monitor their staffs interaction with their post
- monitor your close pals interaction with your posts
- monitor your spouse interaction with your post etc.
## Includes
This project uses the following :
  - python
- pyTelegramAPi
- TwitterAPi
- Replit/( may switch to Heroku)
## current features
- Reply twitter links with loaded information
  
## coming features
- register twitter accounts you want to monitor their interactions with your tweets.
- tweets bandwidth (number of tweets before generating reply)
- tweets reply time ( how long to wait before generating reply)
## How to use/install
- take to your replit account and add keys and value pair for the following:
  - API_KEY value is  bot abi
  - consumer_key value is consumer secret
  - consumer_key_secret value is consumer key secret
  - staffsid value is usernames seperated by comma no space
- then you click run
- alternatively put the values in the code where i commented and run. #
## Others
Feeeel freeee to contribute
