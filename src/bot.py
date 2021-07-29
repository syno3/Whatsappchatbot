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

    if not incoming_msg:
        responded = True
        if responded:
            ### code to generte text
            response = openai.Completion.create(
            engine="davinci",
            prompt= str(incoming_msg),
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
            ##stop=["\n", " Human:", " AI:"]
            )

            response_message = response.choices[0].text
            msg.body(response_message)

    else:
        error = 'please send me a text'
        msg.body(error)

    return str(resp)


if __name__ == '__main__':
    app.run()