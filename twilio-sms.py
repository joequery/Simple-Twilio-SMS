###############################
# Middle man Flask app base
###############################
from flask import Flask, request, jsonify
import json
from twilio.rest import TwilioRestClient, TwilioException
from twilio_settings import(
    TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, FROM_NUM, ACCESS_TOKEN
)

app = Flask(__name__)

def error_resp(msg, status_code=400):
    resp = {
        'message': msg,
        'status_code': status_code
    }
    return jsonify(resp=resp)

@app.route('/sms', methods=['POST'])
def send_sms():
    resp = {}
    data = request.get_json()

    required_fields = ['body', 'to']

    if ACCESS_TOKEN is not None:
        required_fields.append('access_token')

    provided_fields = data.keys()
    missing = [f for f in required_fields if f not in provided_fields]

    if missing:
        err = "The following fields are missing: %s" % ",".join(missing)
        return error_resp(err)

    if ACCESS_TOKEN is not None and data['access_token'] != ACCESS_TOKEN:
        return error_resp('Invalid access token', 403)

    client = TwilioRestClient(TWILIO_ACCOUNT_SID , TWILIO_AUTH_TOKEN)

    if isinstance(data['to'], basestring):
        data['to'] = [data['to']]

    for phone_num in data['to']:
        try:
            client.messages.create(
                to=phone_num,
                from_=FROM_NUM,
                body=data['body']
            )
        except TwilioException, e:
            return error_resp(e.msg)

    resp['status_code'] = 200
    resp['message'] = 'success'
    return jsonify(resp=resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
