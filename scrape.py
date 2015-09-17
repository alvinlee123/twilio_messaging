from bs4 import BeautifulSoup as bs
from flask import Flask, request, redirect
import twilio.twiml

import requests
import time
app = Flask(__name__)
ACCOUNT_SID = "AC6ac1b036ec6592332e66c53bca225861"
AUTH_TOKEN = "SecretSauce"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)



@app.route("/", methods=['GET', 'POST'])
def search():
    """respond to incoming requests"""

    symbol=request.values.get('Body', None)
    search_url='http://www.google.com/finance?q='+symbol
    try:
        url=requests.get(search_url).text
        soup=bs(url)
        price=soup.find('span',{'class':'pr'})
        message=  "%s price right now is %s"%(symbol,price.text.split()[0])
        client.messages.create(
        	to="5107120735",
        	from_="+16507310668",
        	body=message,
        )
    except:
        pass

if __name__ == '__main__':
    app.run(debug=True)
