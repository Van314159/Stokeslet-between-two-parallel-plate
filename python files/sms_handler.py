from flask import Flask, request
import redis
from twilio.twiml.messaging_response import MessagingResponse

twilio_account_sid = 'ACXXXXX'
my_number = '+15905195378'
valid_courses = {'CS 101', 'CS 201'}
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
app = Flask(__name__)

def respond(user, body):
    response = MessagingResponse()
    response.message(body=body)
    return str(response)

@app.route('/sms', methods=['POST'])
def handle_sms():
    user = request.form['From']
    course = request.form['Body'].strip().upper()
    if course not in valid_courses:
        return respond(user, body='Hm, our school doesn\'t have that class. Try something else.')
    else:    
        reids_client.sadd(course, user.encode('utf-8'))
        return respond(user, body=('Sweet action. We\'ll let you know when there are seats avaiable in {course}')) 
    
if __name__ == '__main__':
    app.run(debug=True)