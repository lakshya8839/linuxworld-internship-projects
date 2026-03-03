from twilio.rest import Client

# Replace with your Twilio credentials
account_sid = 'get from twilio'
auth_token = 'get from twilio'
twilio_number = 'get from twilio(your no.)'         # Your Twilio number
recipient_number = 'Reciever no(get verified 1st from twilio)'  # Phone number to call (with country code)

# Initialize client
client = Client(account_sid, auth_token)

# Create the call with a text-to-speech message
call = client.calls.create(
    twiml='<Response><Say voice="alice" language="en-IN">Hello, this is an automated message sent using Python. Have a great day! This side is Lakshya , this is our task of voice-call</Say></Response>',
    to=recipient_number,
    from_=twilio_number
)

print("Call initiated. SID:", call.sid)
