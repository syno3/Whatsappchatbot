### we import required modules
try:
    from flask import Flask, request
    import requests
    from twilio.twiml.messaging_response import MessagingResponse
    import openai
    import logging
    import time
    import json
## checking for errors
except ImportError:
    logging.warning('please run pip install -r requirements.txt')

app = Flask(__name__)

## loading the openai key
with open('OPENAI_API_KEY.json') as f:
    data = json.load(f)

openai.api_key = data["OPENAI_API_KEY"]
### testing if the API key works
try: 
    response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)
except Exception as e:
    print(e)

## initializing the flask app
@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()