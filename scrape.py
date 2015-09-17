from bs4 import BeautifulSoup as bs
from flask import Flask, request, redirect
import requests
import twilio
import twilio.twiml
from twilio.rest import TwilioRestClient

import requests
import time
app = Flask(__name__)

client = TwilioRestClient()



@app.route("/", methods=['GET', 'POST'])
def search():
    """respond to incoming requests"""
    try:
        symbol=request.form['Body']
    except:
        pass
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
        client.messages.create(
        	to="5107120735",
        	from_="+16507310668",
        	body="The ticker symbol you sent is invalid or isn't listed on google finance",
        )

if __name__ == '__main__':
    app.run(debug=True)
