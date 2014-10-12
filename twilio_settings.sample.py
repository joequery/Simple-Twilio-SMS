TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
FROM_NUM = 'YOUR_TWILIO_PHONE_NUMBER'

# Leave ACCESS_TOKEN as None if you do not want to restrict access to your sms
# endpoint. If you would like to restrict access to only clients who know the
# access token, assign a random string to ACCESS_TOKEN. Clients sending a POST
# request to the SMS endpoint should provide 'access_token' data that matches
# the ACCESS_TOKEN provided below.
ACCESS_TOKEN = None # optional
