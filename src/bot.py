### we import required modules
try:
    from flask import Flask, request, session
    import requests
    from twilio.twiml.messaging_response import MessagingResponse
    import openai
    import logging
    import time
    import json
    from openai import ask, append_interaction_to_chat_log
## checking for errors
except ImportError:
    logging.warning('please run pip install -r requirements.txt')

app = Flask(__name__)


## initializing the flask app
@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')

    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)

    r = MessagingResponse()
    r.message(answer)
    return str(r)

if __name__ == '__main__':
    app.run()