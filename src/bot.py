### we import required modules
try:
    from flask import Flask, request, session
    import requests
    from twilio.twiml.messaging_response import MessagingResponse
    import openai
    import logging
    import time
    import json
    from gpt import ask, append_interaction_to_chat_log
## checking for errors
except ImportError:
    logging.warning('please run pip install -r requirements.txt')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'etfjghgjyfjcgnfdkj'

## initializing the flask app
@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    resp = MessagingResponse()
    msg = resp.message()
    chat_log = session.get('chat_log')

    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)
    ##resp.message(answer)
    msg.body(answer)
    
    return str(resp)

if __name__ == '__main__':
    app.run()