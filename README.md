Simple Twilio SMS endpoint
==========================

This is a simple flask app for sending text messages.

Setup
-----

Step 1. Create a virtualenv and install the requirements.

Step 2. Copy `twilio_settings.sample.py` to `twilio_settings.py`

Step 3. Edit the values in `twilio_settings.py` to match your Twilio account
credentials.

Step 4. Run the `twilio-sms.py` file

Usage
-----

An endpoint is setup at '/sms'. Send a POST request with header
`Content-Type: application/json`. The POST data should be in the form

    {
        'to': '5555555555',
        'body': 'This is the text message!'
    }

or

    {
        'to': ['5555555555'],
        'body': 'This is the text message sent to multiple numbers!'
    }
or

    {
        'to': ['5555555555', '9999999999'],
        'body': 'This is the text message sent to multiple numbers!'
    }

### Restricting access

If you do not want your sms endpoint accessible to everyone, you can alter the
`ACCESS_TOKEN` variable in `twilio_settings.py` to be a random string. The
client sending the POST request should include `access_token` in their data, and
the value should match what you assigned to `ACCESS_TOKEN`. For example,


    {
        'to': ['5555555555', '9999999999'],
        'body': 'This is the text message sent to multiple numbers!',
        'access_token': 'SomeRandomString'
    }

### Example request

Suppose you're using the requests library:

```python
import requests
import json

url = "http://localhost:5000/sms"
data = {
    'to': ['5555555555'],
    'body': 'This is the text message'
}
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)
```
