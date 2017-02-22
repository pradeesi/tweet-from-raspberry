##------------------------------------------
##--- Author: Pradeep Singh
##--- Blog: https://iotbytes.wordpress.com/programmatically-tweet-from-raspberry-pi-using-python-script/
##--- Date: 22nd Feb 2017
##--- Version: 1.0
##--- Python Ver: 2.7
##--- Description: This python code will tweet on twitter.
##------------------------------------------


from twitter import *

# Set the values for following variables from your Twitter Account
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# This function will tweet on Twitter
def publish_Status_On_Twitter(Twitter_Status):
	TW = Twitter(auth=OAuth(ACCESS_TOKEN,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET))
	TW.statuses.update(status=Twitter_Status)
	
# Tweet 
publish_Status_On_Twitter("My first tweet from Python!")