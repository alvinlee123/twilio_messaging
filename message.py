from twilio.rest import TwilioRestClient 
from bs4 import BeautifulSoup as bs 
# put your own credentials here 
ACCOUNT_SID = "AC6ac1b036ec6592332e66c53bca225861" 
AUTH_TOKEN = "6262d115a335b5ee58230da65d0920e8" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to="5107120735", 
	from_="+16507310668", 
	body="Hi there",  
)
